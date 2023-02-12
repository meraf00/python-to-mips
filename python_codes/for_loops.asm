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


            li $v0, 0
            li $a2, 10
            li $a3, 1
            move $k0, $v0
            

conditional_label_0:


                # sw $v0, None                
                add $k0, $k0, $a3

                blt $a3, 0, for_label_0

                bgt $k0, $a2, conditional_label_1
                j for_guard_0
                for_label_0:
                blt $k0, $a2, conditional_label_1
                for_guard_0:  

                move $v0, $k0              
                


                   sw $v0, i


                   lw $t8, x
                   lw $t9, y
                   add $t6, $t8, $t9


                   move $t8, $t6
                   lw $t9, i
                   add $t6, $t8, $t9


                   la $t1, str_literal_0
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   move $a0, $t6
                   li $v0, 1
                   syscall

                   li $a0, 32
                   li $v0, 11
                   syscall

                   li $a0, 91
                   li $v0, 11
                   syscall

                   la $t1, i
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 0
                   li $v0, 11
                   syscall

                   li $a0, 93
                   li $v0, 11
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

                   li $a0, 2
                   li $v0, 1
                   syscall

                   li $a0, 44
                   li $v0, 11
                   syscall

                   la $t1, i
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 0
                   li $v0, 11
                   syscall

                   li $a0, 93
                   li $v0, 11
                   syscall

                   li $a0, 10
                   li $v0, 11
                   syscall


                   la $t1, i
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                j conditional_label_0

conditional_label_1:


                   la $t1, str_literal_1
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, i
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                    li $v0, 10
                    syscall

.data
	i: .word 0
	x: .word 1
	y: .word 5
	list_0: .word 1 2 i
	z: .word 1 2 i
	str_literal_0: .asciiz ">>>"
	list_1: .word i
	str_literal_1: .asciiz ">>>"