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


lt:				# v0 = 0 if not lessthan v0 = 1 if lessthan
	lw $a0, 0($sp)		# left operand
	lw $a1, 4($sp)		# right operand
	
	li $v0, 1	
	blt $a0, $a1, end_lt
	li $v0, 0	

	end_lt:
	jr $ra	
        

# Functions

main: # (Entry Point)
li $t1, 11
li $t2, 38
sw $t1, 0($sp)
sw $t2, 4($sp)
jal lt

.data

