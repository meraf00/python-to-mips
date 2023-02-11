import dis
from collections import defaultdict
from .mips_instructions import Assign, Add, Subtract
from .mips_constructs import Register, RegisterTracker, Address
from .consts import PREDEFINED_DATA_SEGMENTS, BUILT_INS

class Compiler:
    def __init__(self, py_source_code):
        self.py_source_code = py_source_code
        self.stack = []
        self.namespace = {}
        self.data_type_counter = defaultdict(int)
        self.registers = RegisterTracker(self.stack)

        self.instructions = []
        
    def get_instruction(self, function):
        if function in BUILT_INS:
            return BUILT_INS.get(function)

    def generate_data_segment(self, include_predefined=True):        
        data = [".data"]

        for label, value in PREDEFINED_DATA_SEGMENTS.items():
            if isinstance(value, str):
                mips_code = f'\t{label}: .asciiz "{value}"'
                data.append(mips_code)

        for label, value in self.namespace.items():
            if isinstance(value, int):
                mips_code = f'\t{label}: .word {value}'
                data.append(mips_code)

            elif isinstance(value, str):
                mips_code = f'\t{label}: .asciiz "{value}"'
                data.append(mips_code)
            
            elif isinstance(value, (list, tuple)):
                elements = " ".join(map(str, value))
                mips_code = f'\t{label}: .word {elements}'
                data.append(mips_code)

            elif isinstance(value, Address):
                mips_code = f'\t{label}: .word {value}'
                data.append(mips_code)

        return "\n".join(data)

    def generate_text_segment(self):
        libraries = set()
        
        functions = ["# Functions"]
        
        code = ["main: # (Entry Point)"]

        for ins in self.instructions:            
            libraries.add(ins.__class__)
            mips_code = ins.mips_code()
            code.append(mips_code)
        
        include = ["# Library"]
        for library in libraries:
            include.append("\n".join(library.INCLUDE))    

        text_segment = [".text", "j main # jump to main (entry point)"]
        text_segment.extend(include)
        text_segment.extend(functions)
        text_segment.extend(code)

        return "\n\n".join(text_segment)

    def compile(self):
        python_code = self.py_source_code
        namespace = self.namespace
        instructions = self.instructions
        registers = self.registers
        data_type_counter = self.data_type_counter
        stack = self.stack

        for ins in dis.get_instructions(python_code):
            print(ins)
            print(stack,  namespace, end="\n\n")
            if ins.opname == "LOAD_NAME":
                name = Address(ins.argval)
                if name in namespace or name in BUILT_INS:
                    stack.append(name)
            
            elif ins.opname in set(("STORE_NAME", "STORE_FAST", "STORE_GLOBAL")):
                address = Address(ins.argval)        
                value = stack.pop()
                
                # update variable
                if address in namespace:
                    instructions.append(Assign(address, value, namespace))            
                
                elif isinstance(value, Address):  
                    # allow indirect reference to strings
                    if isinstance(namespace[value], str):
                        namespace[address] = value                
                    
                    # indirect reference to tuples and lists is not allowed
                    else:
                        namespace[address] = namespace[value]   

                # store value of operation to memory (return value of operation is stored in register)
                elif isinstance(value, Register):
                    namespace[address] = value.dtype()
                    instructions.append(Assign(address, value, namespace))
                
                else:
                    namespace[address] = value

            elif ins.opname == "LOAD_CONST":
                value = ins.argval

                if isinstance(value, str):
                    address = Address(f"str_literal_{data_type_counter['str']}")
                    data_type_counter['str'] += 1

                    namespace[address] = value
                    stack.append(address)
                
                elif isinstance(value, tuple):   
                    # python doesn't build tuple unless list is inside it
                    # so we should bu
                    # ild it ourselves if string is contained inside tuple
                    str_exist = False
                    list_exist = False
                    for element in value:
                        if isinstance(element, str):
                            str_exist = True
                        elif isinstance(element, list):
                            list_exist = True
                        
                        if str_exist and list_exist: break
                    
                    # we will need to build the tuple ourselves in this case
                    if str_exist and not list_exist:
                        new_tuple = []
                        for element in value:
                            if isinstance(element, str):
                                address = Address(f"str_literal_{data_type_counter['str']}")
                                data_type_counter['str'] += 1

                                namespace[address] = element
                                stack.append(address)

                                new_tuple.append(address)

                            else:
                                new_tuple.append(element)
                        
                        value = tuple(new_tuple)
                    
                    address = Address(f"tuple_{data_type_counter['tuple']}")
                    data_type_counter['tuple'] += 1

                    namespace[address] = value
                    stack.append(address)
                    

                elif isinstance(value, (int, float)):
                    stack.append(value)
                
            elif ins.opname == "BUILD_LIST" or ins.opname == "BUILD_TUPLE":
                list_length = ins.arg
                
                if list_length == 0:
                    continue

                list_elements = stack[-list_length:]
                
                for _ in range(list_length):
                    stack.pop()

                naming = "list" if ins.opname == "BUILD_LIST" else "tuple"
                address = Address(f"{naming}_{data_type_counter[naming]}")
                data_type_counter[naming] += 1

                namespace[address] = list_elements
                stack.append(address)
            
            elif ins.opname == "CALL_FUNCTION":
                argc = ins.arg
                args = stack[-argc:]
                
                for _ in range(argc):
                    stack.pop()

                function = stack.pop()

                instruction_class = self.get_instruction(function)  
                instruction = instruction_class(*args, namespace=namespace)
                instructions.append(instruction)  

            elif ins.opname == "CALL_FUNCTION_KW":                
                keys = namespace[stack[-1]]             
                
                argc = ins.arg
                kwargc = len(keys)
                
                args = stack[-(argc+kwargc-1):-(kwargc+1)]
                kwargs_values = stack[-(kwargc+1):-1]
                
                kwargs = {}
                for key, value in zip(keys, kwargs_values):
                    kwargs[key] = value

                print(stack, "\n",args, "\n",kwargs)
                
                for _ in range(argc + kwargc - 1):            
                    stack.pop()
                

                function = stack.pop()        

                instruction_class = self.get_instruction(function)  
                instruction = instruction_class(*args, namespace=namespace, **kwargs)
                instructions.append(instruction)  

            elif ins.opname in set(("BINARY_ADD", "BINARY_SUBTRACT")): 
                right_operand = stack.pop()
                left_operand = stack.pop()

                if isinstance(right_operand, Address):
                    dtype = right_operand.resolve_type(namespace)
                elif isinstance(right_operand, Register):
                    dtype = right_operand.dtype
                else:
                    dtype = type(right_operand)

                result_register = registers.allocate_register(dtype)
                stack.append(result_register)

                if ins.opname == "BINARY_ADD":
                    instruction = Add(left_operand, right_operand, result_register, namespace=namespace)

                if ins.opname == "BINARY_SUBTRACT":
                    instruction = Subtract(left_operand, right_operand, result_register, namespace=namespace)

                instructions.append(instruction)
    
    def to_mips(self):
        self.compile()

        text_segment = self.generate_text_segment()
        data_segment = self.generate_data_segment()

        mips = [text_segment, data_segment]

        return "\n\n".join(mips)