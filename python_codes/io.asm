.text

j main # jump to main (entry point)

# Library

print_str:
                lw $a0, 0($sp)
                li $v0, 4
                syscall
                jr $ra
print_int:
                lw $a0, 0($sp)
                lw $a0, ($a0)
                li $v0, 1
                syscall
                jr $ra
        

# Functions

main: # (Entry Point)


                   li $a0, 1
                   li $v0, 1
                   syscall

                   li $a0, 10
                   li $v0, 11
                   syscall


                   li $a0, 1
                   li $v0, 1
                   syscall

                   li $a0, 32
                   li $v0, 11
                   syscall

                   li $a0, 2
                   li $v0, 1
                   syscall

                   li $a0, 10
                   li $v0, 11
                   syscall


                   li $a0, 1
                   li $v0, 1
                   syscall

                   li $a0, 32
                   li $v0, 11
                   syscall

                   li $a0, 2
                   li $v0, 1
                   syscall

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, str_literal_0
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                   li $a0, 1
                   li $v0, 1
                   syscall

                   li $a0, 32
                   li $v0, 11
                   syscall

                   li $a0, 2
                   li $v0, 1
                   syscall

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, str_literal_1
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   li $a0, 91
                   li $v0, 11
                   syscall

                   li $a0, 1
                   li $v0, 1
                   syscall

                   li $a0, 44
                   li $v0, 11
                   syscall

                   li $a0, 2
                   li $v0, 1
                   syscall

                   li $a0, 44
                   li $v0, 11
                   syscall

                   la $t1, str_literal_2
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 44
                   li $v0, 11
                   syscall

                   li $a0, 91
                   li $v0, 11
                   syscall

                   li $a0, 1
                   li $v0, 1
                   syscall

                   li $a0, 44
                   li $v0, 11
                   syscall

                   li $a0, 2
                   li $v0, 1
                   syscall

                   li $a0, 44
                   li $v0, 11
                   syscall

                   li $a0, 3
                   li $v0, 1
                   syscall

                   li $a0, 0
                   li $v0, 11
                   syscall

                   li $a0, 93
                   li $v0, 11
                   syscall

                   li $a0, 0
                   li $v0, 11
                   syscall

                   li $a0, 93
                   li $v0, 11
                   syscall

                   li $a0, 10
                   li $v0, 11
                   syscall

.data
	str_literal_0: .asciiz "ab"
	str_literal_1: .asciiz "ab"
	str_literal_2: .asciiz "a"
	tuple_0: .word 1 2 3
	list_0: .word 1 2 str_literal_2 tuple_0