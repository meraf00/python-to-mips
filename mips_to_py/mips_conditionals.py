from .mips_constructs import Register, Address


class Compare:
    INCLUDE = (
        """lt:				        # v0 = 0 if not lessthan
                                    # v0 = 1 if lessthan
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                blt $a0, $a1, end_lt
                li $v0, 0	

                end_lt:
                jr $ra        
        """,
        """gt:				        # v0 = 0 if not greater than
                                    # v0 = 1 if greater than
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                bgt $a0, $a1, end_gt
                li $v0, 0	

                end_gt:
                jr $ra        
        """,
        """eq:				        # v0 = 0 if not equal
                                    # v0 = 1 if equal
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                beq $a0, $a1, end_eq
                li $v0, 0	

                end_eq:
                jr $ra        
        """,
        """not_eq:				    # v0 = 0 if equal
                                    # v0 = 1 if not equal
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1
                bne $a0, $a1, end_not_eq
                li $v0, 0

                end_not_eq:
                jr $ra        
        """,
        """gt_eq:			        # v0 = 0 if not greater than or equal
                                    # v0 = 1 if greater than or equal
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                bge $a0, $a1, end_gt_eq
                li $v0, 0	

                end_gt_eq:
                jr $ra        
        """,
        """lt_eq:			        # v0 = 0 if not less than or equal
                                    # v0 = 1 if less than or equal
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                ble $a0, $a1, end_lt_eq
                li $v0, 0	

                end_lt_eq:
                jr $ra        
        """
    )

    REQUIRE = tuple()

    LESSTHAN = -2
    LESSTHAN_OR_EQUAL = -1
    EQUAL = 0
    GREATERTHAN_OR_EQUAL = 1
    GREATERTHAN = 2

    def __init__(self, left_operand, right_operand, operation, namespace=None):
        self.operations = {
            "<": "lt",
            ">": "gt",
            ">=": "gt_eq",
            "<=": "lt_eq",
            "==": "eq",
            "!=": "not_eq"
        }
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.namespace = namespace
        self.operation = self.operations[operation]

    def immediate_and_address(self, immediate, address):
        if immediate == self.left_operand:
            left, right = "$t8", "$t9"
        else:
            left, right = "$t9", "$t8"

        return f"""
                li $t8, {immediate}
                lw $t9, {address}
                sw {left}, 0($sp)
                sw {right}, 4($sp)
                jal {self.operation}
                """

    def immediate_and_immediate(self, immediate_1, immediate_2):
        if immediate_1 == self.left_operand:
            left, right = "$t8", "$t9"
        else:
            left, right = "$t9", "$t8"

        return f"""
                li $t8, {immediate_1}
                li $t9, {immediate_2}
                sw {left}, 0($sp)
                sw {right}, 4($sp)
                jal {self.operation}
                """

    def immediate_and_register(self, immediate, register):
        if immediate == self.left_operand:
            left, right = "$t8", "$t9"
        else:
            left, right = "$t9", "$t8"

        return f"""
                li $t8, {immediate}
                move $t9, {register}
                sw {left}, 0($sp)
                sw {right}, 4($sp)
                jal {self.operation}
                """

    def address_and_address(self, address_1, address_2):
        if address_1 == self.left_operand:
            left, right = "$t8", "$t9"
        else:
            left, right = "$t9", "$t8"

        return f"""
                lw $t8, {address_1}
                lw $t9, {address_2}
                sw {left}, 0($sp)
                sw {right}, 4($sp)
                jal {self.operation}
                """

    def register_and_register(self, register_1, register_2):
        if register_1 == self.left_operand:
            left, right = "$t8", "$t9"
        else:
            left, right = "$t9", "$t8"

        return f"""
                move $t8, {register_1}
                move $t9, {register_2}
                sw {left}, 0($sp)
                sw {right}, 4($sp)
                jal {self.operation}
                """

    def register_and_address(self, register, address):
        if register == self.left_operand:
            left, right = "$t8", "$t9"
        else:
            left, right = "$t9", "$t8"

        return f"""
                move $t8, {register}
                lw $t9, {address}
                sw {left}, 0($sp)
                sw {right}, 4($sp)
                jal {self.operation}
                """

    def mips_code(self):
        # immediate and address
        if isinstance(self.left_operand, Address) and isinstance(self.right_operand, int):
            return self.immediate_and_address(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, Address):
            return self.immediate_and_address(self.left_operand, self.right_operand)

        # 2 addresses
        elif isinstance(self.left_operand, Address) and isinstance(self.right_operand, Address):
            return self.address_and_address(self.left_operand, self.right_operand)

        # 2 registers
        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, Register):
            return self.register_and_register(self.left_operand, self.right_operand)

        # register and address
        elif isinstance(self.left_operand, Address) and isinstance(self.right_operand, Register):
            return self.register_and_address(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, Address):
            return self.register_and_address(self.left_operand, self.right_operand)

        # immediate and register
        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, Register):
            return self.immediate_and_register(self.left_operand, self.right_operand)

        elif isinstance(self.left_operand, Register) and isinstance(self.right_operand, int):
            return self.immediate_and_register(self.right_operand, self.left_operand)

        elif isinstance(self.left_operand, int) and isinstance(self.right_operand, int):
            return self.immediate_and_immediate(self.left_operand, self.right_operand)


class Conditional:
    INCLUDE = ()
    REQUIRE = ()

    def __init__(self, condition, jump_to, namespace=None):
        self.namespace = namespace
        self.condition = condition
        self.jump_to = jump_to

    def mips_code(self):
        if self.condition == "POP_JUMP_IF_FALSE":
            return f"""
                beqz $v0, {self.jump_to}"""
        elif self.condition == "POP_JUMP_IF_TRUE":
            return f"""
                bnez $v0, {self.jump_to}"""
