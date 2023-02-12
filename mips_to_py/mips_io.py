from .mips_constructs import Register, Address, MemoryLocation


class Print:
    INCLUDE = (
        """print_str:
                lw $a0, 0($sp)
                li $v0, 4
                syscall
                jr $ra""",

        """print_int:
                lw $a0, 0($sp)
                lw $a0, ($a0)
                li $v0, 1
                syscall
                jr $ra
        """
    )
    REQUIRE = tuple()
    return_type = MemoryLocation

    def __init__(self, *args, namespace=None, **kwargs):
        self.args = args

        self.namespace = namespace

        self.end = namespace.get(kwargs.get("end", ""), "\n")
        self.sep = namespace.get(kwargs.get("sep", ""), " ")

        if len(self.sep) > 1:
            self.sep = self.sep[0]

        if len(self.end) > 1:
            self.end = self.end[0]

    def print_register_int(self, register):
        return f"""
                   move $a0, {register}
                   li $v0, 1
                   syscall"""

    def print_string(self, address_label):
        """Print string stored in memory location"""

        return f"""
                   la $t1, {address_label}
                   sw $t1, 0($sp)    
                   jal print_str"""

    def print_referenced_string(self, address_label):
        """Print string stored in indirect referenced memory location

        Args:
            address_label (Address) : points to another addresss containing the actual string"""

        return f"""
                   lw $t1, {address_label}
                   sw $t1, 0($sp)    
                   jal print_str"""

    def print_character(self, character):
        """Print immediate character"""

        return f"""
                   li $a0, {ord(character)}
                   li $v0, 11
                   syscall"""

    def print_immediate_int(self, number, format="DEC"):
        """Print immediate int"""

        if format == "DEC":
            code = 1
        elif format == "HEX":
            code = 34
        elif format == "BIN":
            code = 35

        return f"""
                   li $a0, {number}
                   li $v0, {code}
                   syscall"""

    def print_immediate_float(self, number):
        """Print immediate float"""

        return f"""
                   li $f12, {number}
                   li $v0, 2
                   syscall"""

    def print_int(self, address):
        "Print int stored in memory location"

        return f"""
                   la $t1, {address}
                   sw $t1, 0($sp)    
                   jal print_int"""

    def print_list(self, content):
        """Print list stored in memeory location"""

        code = []

        code.append(self.print_character("["))

        list_repr = Print(*content, namespace=self.namespace,
                          end="\0", sep=",").mips_code()
        code.append(list_repr)

        code.append(self.print_character("]"))

        return "\n".join(code)

    def mips_code(self):
        code = []
        for index, arg in enumerate(self.args):
            # meaning the argument is address of some object
            # not an immediate value
            if isinstance(arg, Address):
                content = self.namespace[arg]

                if isinstance(content, int):
                    code.append(self.print_int(arg))

                elif isinstance(content, Address):
                    code.append(self.print_referenced_string(arg))

                elif isinstance(content, str):
                    code.append(self.print_string(arg))

                elif isinstance(content, MemoryLocation):
                    code.append(self.print_referenced_string(arg))

                elif isinstance(content, (tuple, list)):
                    code.append(self.print_list(content))

            # meaning arg is an immediate value (integer)
            elif isinstance(arg, int):
                code.append(self.print_immediate_int(arg))

            elif isinstance(arg, Register):
                code.append(self.print_register_int(arg))

            # separate printed arguments by space
            if index < len(self.args) - 1:
                code.append(self.print_character(self.sep))

        code.append(self.print_character(self.end))

        return "\n".join(code)


class Input:
    INCLUDE = (
        """input:                
                li $a0, 200     # allocate heap
                li $v0, 9
                syscall
                
                move $t1, $v0   # address of input string
                
                move $a0, $t1   # get user input
                li $a1, 200
                li $v0, 8
                syscall
                    
                move $v0, $t1 	# return address of input string
                
                jr $ra""",
    )

    REQUIRE = (
        Print,
    )
    return_type = MemoryLocation

    def __init__(self, *args, namespace=None, **kwargs):
        self.args = args

        self.namespace = namespace

    def mips_code(self):
        prompt = Print(*self.args, namespace=self.namespace,
                       end=" ").mips_code()

        take_input = """
                   jal input"""

        return "\n\n".join([prompt, take_input])
