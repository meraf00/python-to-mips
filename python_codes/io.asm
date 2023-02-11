.text

j main # jump to main (entry point)

# Library

input:                
                li $a0, 200     # allocate heap
                li $v0, 9
                syscall
                
                move $t1, $v0   # address of input string
                
                move $a0, $t1   # get user input
                li $a1, 200
                li $v0, 8
                syscall
                    
                move $v0, $t1 	# return address of input string
                
                jr $ra



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


                   la $t1, str_literal_3
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, str_literal_4
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                   la $t1, str_literal_5
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall


                   jal input


                   sw $v0, x


                   la $t1, str_literal_6
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall


                   jal input


                   sw $v0, y


                   lw $t1, x
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                   lw $t1, y
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                   lw $t1, x
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   lw $t1, y
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, str_literal_7
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall

.data
	str_literal_0: .asciiz "ab"
	str_literal_1: .asciiz "ab"
	str_literal_2: .asciiz "a"
	tuple_0: .word 1 2 3
	list_0: .word 1 2 str_literal_2 tuple_0
	str_literal_3: .asciiz "Mr"
	str_literal_4: .asciiz "I"
	str_literal_5: .asciiz "Enter a number: "
	x: .word 0
	str_literal_6: .asciiz "Enter another number: "
	y: .word 0
	str_literal_7: .asciiz "Why!"