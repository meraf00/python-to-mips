from .mips_constructs import Register, Address


class Assign:
    INCLUDE = tuple()

    def __init__(self, address, value, namespace=None):
        self.namespace = namespace
        self.address = address
        self.value = value

    def store_immediate(self):
        return f"""
                    li $t1, {self.value}
                    sw $t1, {self.address}"""

    def store_from_address(self):
        return f"""
                    la $t1, {self.value}
                    sw $t1, {self.address}"""

    def store_from_register(self):
        return f"""
                   sw {self.value}, {self.address}"""

    def mips_code(self):
        value = self.value
        if isinstance(value, int):
            return self.store_immediate()

        elif isinstance(value, Address):
            return self.store_from_address()

        elif isinstance(value, Register):
            return self.store_from_register()


class Add:
    INCLUDE = tuple()

    def __init__(self, left_operand, right_operand, destination, namespace=None):
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.namespace = namespace
        self.destination = destination

    def add_immediate_and_address(self, immediate, address):
        return f"""
                   lw $t8, {address}
                   li $t9, {immediate}
                   add {self.destination}, $t8, $t9"""

    def add_immediate_and_register(self, immediate, register):
        return f"""
                   move $t8, {register}
                   li $t9, {immediate}
                   add {self.destination}, $t8, $t9"""

    def add_register_and_register(self, register_1, register_2):
        return f"""
                   move $t8, {register_1}
                   move $t9, {register_2}
                   add {self.destination}, $t8, $t9"""

    def add_address_and_address(self, address_1, address_2):
        return f"""
                   lw $t8, {address_1}
                   lw $t9, {address_2}
                   add {self.destination}, $t8, $t9"""

    def add_register_and_address(self, register, address):
        return f"""
                   move $t8, {register}
                   lw $t9, {address}
                   add {self.destination}, $t8, $t9"""

    def mips_code(self):
        # immediate and address
        if isinstance(self.left_operand, Address) and isinstance(self.right_operand, int):
            return self.add_immediate_and_address(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, Address):
            return self.add_immediate_and_address(self.left_operand, self.right_operand)

        # 2 addresses
        elif isinstance(self.left_operand, Address) and isinstance(self.right_operand, Address):
            return self.add_address_and_address(self.left_operand, self.right_operand)

        # 2 registers
        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, Register):
            return self.add_register_and_register(self.left_operand, self.right_operand)

        # register and address
        elif isinstance(self.left_operand, Address) and isinstance(self.right_operand, Register):
            return self.add_register_and_address(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, Address):
            return self.add_register_and_address(self.left_operand, self.right_operand)

        # immediate and register
        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, Register):
            return self.add_immediate_and_register(self.left_operand, self.right_operand)

        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, int):
            return self.add_immediate_and_register(self.right_operand, self.left_operand)


class Subtract:
    INCLUDE = tuple()

    def __init__(self, left_operand, right_operand, destination, namespace=None):
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.namespace = namespace
        self.destination = destination

    def sub_immediate_and_address(self, immediate, address):
        if immediate == self.left_operand:
            operand_registers = "$t8, $t9"
        else:
            operand_registers = "$t9, $t8"

        return f"""
                li $t8, {immediate}
                lw $t9, {address}
                sub {self.destination}, {operand_registers}"""

    def sub_immediate_and_register(self, immediate, register):
        if immediate == self.left_operand:
            operand_registers = "$t8, $t9"
        else:
            operand_registers = "$t9, $t8"

        return f"""
                   li $t8, {immediate}
                   move $t9, {register}
                   sub {self.destination}, {operand_registers}"""

    def sub_address_and_address(self, address_1, address_2):
        if address_1 == self.left_operand:
            operand_registers = "$t8, $t9"
        else:
            operand_registers = "$t9, $t8"

        return f"""
                   lw $t8, {address_1}
                   lw $t9, {address_2}
                   sub {self.destination}, {operand_registers}"""

    def add_register_and_register(self, register_1, register_2):
        if register_1 == self.left_operand:
            operand_registers = "$t8, $t9"
        else:
            operand_registers = "$t9, $t8"

        return f"""
                   move $t8, {register_1}
                   move $t9, {register_2}
                   add {self.destination}, {operand_registers}"""

    def sub_register_and_address(self, register, address):
        if register == self.left_operand:
            operand_registers = "$t8, $t9"
        else:
            operand_registers = "$t9, $t8"

        return f"""
                   move $t8, {register}
                   lw $t9, {address}
                   sub {self.destination}, {operand_registers}"""

    def mips_code(self):
        # immediate and address
        if isinstance(self.left_operand, Address) and isinstance(self.right_operand, int):
            return self.sub_immediate_and_address(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, Address):
            return self.sub_immediate_and_address(self.left_operand, self.right_operand)

        # 2 addresses
        elif isinstance(self.left_operand, Address) and isinstance(self.right_operand, Address):
            return self.sub_address_and_address(self.left_operand, self.right_operand)

        # register and address
        elif isinstance(self.left_operand, Address) and isinstance(self.right_operand, Register):
            return self.sub_register_and_address(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, Address):
            return self.sub_register_and_address(self.left_operand, self.right_operand)

        # immediate and register
        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, Register):
            return self.sub_immediate_and_register(self.left_operand, self.right_operand)

        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, int):
            return self.sub_immediate_and_register(self.right_operand, self.left_operand)

class Multiply:
    INCLUDE = tuple()

    def __init__(self, left_operand, right_operand, destination, namespace=None):
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.namespace = namespace
        self.destination = destination

    def mul_immediate_and_address(self, immediate, address):
        return f"""
                   lw $t8, {address}
                   li $t9, {immediate}
                   mul {self.destination}, $t8, $t9"""

    def mul_immediate_and_register(self, immediate, register):
        return f"""
                   move $t8, {register}
                   li $t9, {immediate}
                   mul {self.destination}, $t8, $t9"""

    def mul_register_and_register(self, register_1, register_2):
        return f"""
                   move $t8, {register_1}
                   move $t9, {register_2}
                   mul {self.destination}, $t8, $t9"""

    def mul_address_and_address(self, address_1, address_2):
        return f"""
                   lw $t8, {address_1}
                   lw $t9, {address_2}
                   mul {self.destination}, $t8, $t9"""

    def mul_register_and_address(self, register, address):
        return f"""
                   move $t8, {register}
                   lw $t9, {address}
                   mul {self.destination}, $t8, $t9"""

    def mips_code(self):
        # immediate and address
        if isinstance(self.left_operand, Address) and isinstance(self.right_operand, int):
            return self.mul_immediate_and_address(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, Address):
            return self.mul_immediate_and_address(self.left_operand, self.right_operand)

        # 2 addresses
        elif isinstance(self.left_operand, Address) and isinstance(self.right_operand, Address):
            return self.mul_address_and_address(self.left_operand, self.right_operand)

        # 2 registers
        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, Register):
            return self.mul_register_and_register(self.left_operand, self.right_operand)

        # register and address
        elif isinstance(self.left_operand, Address) and isinstance(self.right_operand, Register):
            return self.mul_register_and_address(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, Address):
            return self.mul_register_and_address(self.left_operand, self.right_operand)

        # immediate and register
        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, Register):
            return self.mul_immediate_and_register(self.left_operand, self.right_operand)

        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, int):
            return self.mul_immediate_and_register(self.right_operand, self.left_operand)

