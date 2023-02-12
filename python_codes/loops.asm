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

conditional_label_0:


                li $t8, 0
                lw $t9, x
                sw $t9, 0($sp)
                sw $t8, 4($sp)
                jal gt
                


                beqz $v0, conditional_label_1

conditional_label_2:


                li $t8, 5
                lw $t9, x
                sw $t9, 0($sp)
                sw $t8, 4($sp)
                jal eq
                


                beqz $v0, conditional_label_3


                li $t8, 1
                lw $t9, x
                sub $t1, $t9, $t8


                   sw $t1, x


                j conditional_label_0

conditional_label_3:


                li $t8, 2
                lw $t9, x
                sw $t9, 0($sp)
                sw $t8, 4($sp)
                jal eq
                


                beqz $v0, conditional_label_4


                j conditional_label_1

conditional_label_4:


                   la $t1, x
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                li $t8, 1
                lw $t9, x
                sub $t1, $t9, $t8


                   sw $t1, x


                li $t8, 0
                lw $t9, x
                sw $t9, 0($sp)
                sw $t8, 4($sp)
                jal gt
                


                bnez $v0, conditional_label_2

conditional_label_1:


                   la $t1, str_literal_0
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                li $t8, 3
                lw $t9, x
                sw $t9, 0($sp)
                sw $t8, 4($sp)
                jal eq
                


                beqz $v0, conditional_label_5


                   la $t1, str_literal_1
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                j conditional_label_6

conditional_label_5:


                li $t8, 0
                lw $t9, x
                sw $t9, 0($sp)
                sw $t8, 4($sp)
                jal eq
                


                beqz $v0, conditional_label_7


                   la $t1, str_literal_2
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                j conditional_label_6

conditional_label_7:


                   la $t1, str_literal_3
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall

conditional_label_6:


                   la $t1, str_literal_4
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                   la $t1, str_literal_5
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


            li $v0, 2
            li $a2, 20
            li $a3, 2
            move $k0, $v0
            

conditional_label_8:


                # sw $v0, None                
                add $k0, $k0, $a3

                blt $a3, 0, for_label_0

                bgt $k0, $a2, conditional_label_9
                j for_guard_0
                for_label_0:
                blt $k0, $a2, conditional_label_9
                for_guard_0:  

                move $v0, $k0              
                


                   sw $v0, j


                   la $t1, j
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 32
                   li $v0, 11
                   syscall


                j conditional_label_8

conditional_label_9:


                    li $v0, 10
                    syscall

.data
	x: .word 10
	str_literal_0: .asciiz "WHy"
	str_literal_1: .asciiz "apple"
	str_literal_2: .asciiz "bababa"
	str_literal_3: .asciiz "hooo"
	str_literal_4: .asciiz "herer"
	str_literal_5: .asciiz "========== Evens! ============="
	j: .word 0
	str_literal_6: .asciiz " "
	str_literal_7: .asciiz " "
	str_literal_8: .asciiz "end"
	str_literal_9: .asciiz "sep"
	tuple_0: .word str_literal_8 str_literal_9