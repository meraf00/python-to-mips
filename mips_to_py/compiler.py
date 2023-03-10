import dis
from collections import defaultdict
from .mips_instructions import Assign, Add, Exit, Subtract, Multiply, Divide
from .mips_conditionals import Compare, Conditional
from .mips_constructs import Label, MemoryLocation, Register, RegisterTracker, Address
from .consts import PREDEFINED_DATA_SEGMENTS, BUILT_INS


class Compiler:
    def __init__(self, py_source_code):
        self.py_source_code = py_source_code
        self.stack = []
        self.namespace = {}
        self.data_type_counter = defaultdict(int)
        self.label_counter = defaultdict(int)
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

            elif isinstance(value, MemoryLocation):
                mips_code = f'\t{label}: .word {value}'
                data.append(mips_code)

        return "\n".join(data)

    def generate_text_segment(self):
        libraries = set()

        functions = ["# Functions"]

        code = ["main: # (Entry Point)"]

        for ins in self.instructions:
            libraries.add(ins.__class__)
            libraries.union(ins.REQUIRE)
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
        label_counter = self.label_counter

        label_dict = {}
        stack = self.stack

        instruction_iter = dis.get_instructions(python_code)

        for ins in instruction_iter:
            print(ins)
            if ins.is_jump_target:
                if ins.offset not in label_dict:
                    label_name = f"conditional_label_{label_counter['conditional_label']}"
                    label_dict[ins.offset] = Label(label_name)
                    label_counter["conditional_label"] += 1

                instructions.append(label_dict[ins.offset])

            if ins.opname == "LOAD_NAME":
                name = Address(ins.argval)
                if name in namespace or name in BUILT_INS:
                    stack.append(name)

            elif ins.opname in ("STORE_NAME", "STORE_FAST", "STORE_GLOBAL"):
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
                    address = Address(
                        f"str_literal_{data_type_counter['str']}")
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

                        if str_exist and list_exist:
                            break

                    # we will need to build the tuple ourselves in this case
                    if str_exist and not list_exist:
                        new_tuple = []
                        for element in value:
                            if isinstance(element, str):
                                address = Address(
                                    f"str_literal_{data_type_counter['str']}")
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

                stack.append(Register("$v0", instruction_class.return_type))

            elif ins.opname == "CALL_FUNCTION_KW":
                keys = list(namespace[k] for k in namespace[stack[-1]])
                
                argc = ins.arg
                kwargc = len(keys)

                args = stack[-(argc+ 2 * kwargc - 1 ):-(2 * kwargc + 1)]
                kwargs_values = stack[-(2 * kwargc + 1):-1]

                kwargs = {}
                for key, value in zip(keys, kwargs_values):
                    kwargs[key] = value

                print(stack, "\n?", args, "\n?", kwargs)

                for _ in range(argc + 2*kwargc - 1):
                    stack.pop()
                
                function = stack.pop()

                instruction_class = self.get_instruction(function)
                instruction = instruction_class(
                    *args, namespace=namespace, **kwargs)
                instructions.append(instruction)

            elif ins.opname in ("BINARY_ADD", "BINARY_SUBTRACT", "BINARY_MULTIPLY", "BINARY_FLOOR_DIVIDE"):
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
                    instruction = Add(left_operand, right_operand,
                                      result_register, namespace=namespace)

                if ins.opname == "BINARY_SUBTRACT":
                    instruction = Subtract(
                        left_operand, right_operand, result_register, namespace=namespace)

                if ins.opname == "BINARY_MULTIPLY":
                    instruction = Multiply(
                        left_operand, right_operand, result_register, namespace=namespace)

                if ins.opname == "BINARY_FLOOR_DIVIDE":
                    instruction = Divide(
                        left_operand, right_operand, result_register, namespace=namespace)

                instructions.append(instruction)

            elif ins.opname == "COMPARE_OP":
                right_operand = stack.pop()
                left_operand = stack.pop()
                operation = ins.argval

                instructions.append(
                    Compare(left_operand, right_operand, operation, namespace=namespace))
                stack.append(Register("$v0", int))

            elif ins.opname in ("POP_JUMP_IF_FALSE", "POP_JUMP_IF_TRUE", "JUMP_FORWARD", "FOR_ITER", "JUMP_ABSOLUTE"):
                if ins.argval not in label_dict:
                    label_name = f"conditional_label_{label_counter['conditional_label']}"
                    label_dict[ins.argval] = Label(label_name)
                    label_counter["conditional_label"] += 1

                else:
                    label_name = label_dict[ins.argval].label

                instructions.append(
                    Conditional(ins.opname, jump_to=label_name, label_counter=label_counter, namespace=namespace))

            elif ins.opname == "RETURN_VALUE":
                instructions.append(Exit())

            print(stack,  namespace, end="\n\n")

    def to_mips(self):
        self.compile()

        text_segment = self.generate_text_segment()
        data_segment = self.generate_data_segment()

        mips = [text_segment, data_segment]

        return "\n\n".join(mips)
