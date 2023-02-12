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
        











lt:				        # v0 = 0 if not lessthan
                                    # v0 = 1 if lessthan
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                blt $a0, $a1, end_lt
                li $v0, 0	

                end_lt:
                jr $ra        
        
gt:				        # v0 = 0 if not greater than
                                    # v0 = 1 if greater than
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                bgt $a0, $a1, end_gt
                li $v0, 0	

                end_gt:
                jr $ra        
        
eq:				        # v0 = 0 if not equal
                                    # v0 = 1 if equal
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                beq $a0, $a1, end_eq
                li $v0, 0	

                end_eq:
                jr $ra        
        
not_eq:				    # v0 = 0 if equal
                                    # v0 = 1 if not equal
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1
                bne $a0, $a1, end_not_eq
                li $v0, 0

                end_not_eq:
                jr $ra        
        
gt_eq:			        # v0 = 0 if not greater than or equal
                                    # v0 = 1 if greater than or equal
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                bge $a0, $a1, end_gt_eq
                li $v0, 0	

                end_gt_eq:
                jr $ra        
        
lt_eq:			        # v0 = 0 if not less than or equal
                                    # v0 = 1 if less than or equal
                lw $a0, 0($sp)		# left operand
                lw $a1, 4($sp)		# right operand
                
                li $v0, 1	
                ble $a0, $a1, end_lt_eq
                li $v0, 0	

                end_lt_eq:
                jr $ra        
        

# Functions

main: # (Entry Point)


                li $t8, 0
                lw $t9, x
                sw $t9, 0($sp)
                sw $t8, 4($sp)
                jal gt
                


                beqz $v0, conditional_label_0

conditional_label_1:


                   la $t1, x
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                li $t8, 1
                lw $t9, x
                sub $t7, $t9, $t8


                   sw $t7, x


                li $t8, 0
                lw $t9, x
                sw $t9, 0($sp)
                sw $t8, 4($sp)
                jal gt
                


                bnez $v0, conditional_label_1


                    li $v0, 10
                    syscall

conditional_label_0:


                    li $v0, 10
                    syscall

.data
	x: .word 10