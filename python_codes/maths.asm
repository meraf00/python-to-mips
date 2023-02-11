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


                   lw $t8, x
                   lw $t9, y
                   add $t6, $t8, $t9


                   move $t8, $t6
                   li $t9, 4
                   add $t6, $t8, $t9


                   move $t8, $t6
                   li $t9, 1
                   add $t6, $t8, $t9


                   sw $t6, z


                   la $t1, x
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                   la $t1, y
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                   la $t1, z
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                   lw $t8, x
                   li $t9, 1
                   add $t6, $t8, $t9


                   move $t8, $t6
                   lw $t9, z
                   add $t6, $t8, $t9


                   move $a0, $t6
                   li $v0, 1
                   syscall

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

                   la $t1, str_literal_0
                   sw $t1, 0($sp)    
                   jal print_str

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
	x: .word 1
	y: .word 3
	z: .word 0
	str_literal_0: .asciiz "a"
	list_0: .word 1 str_literal_0