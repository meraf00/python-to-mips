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
                   mul $t0, $t8, $t9


                   sw $t0, z


                   lw $t8, x
                   lw $t9, y
                   div $t0, $t8, $t9


                   sw $t0, a


                   la $t1, str_literal_0
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, x
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                   la $t1, str_literal_1
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, y
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                   la $t1, str_literal_2
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, a
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                   lw $t8, y
                   lw $t9, x
                   div $t0, $t8, $t9


                   la $t1, str_literal_3
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   move $a0, $t0
                   li $v0, 1
                   syscall

                   li $a0, 10
                   li $v0, 11
                   syscall


                   la $t1, str_literal_4
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, z
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 10
                   li $v0, 11
                   syscall


                   lw $t8, x
                   lw $t9, y
                   add $t0, $t8, $t9


                   move $t8, $t0
                   lw $t9, z
                   sub $t0, $t8, $t9


                   move $t8, $t0
                   lw $t9, z
                   add $t0, $t8, $t9


                   move $t8, $t0
                   lw $t9, y
                   sub $t0, $t8, $t9


                   lw $t8, x
                   lw $t9, z
                   mul $t4, $t8, $t9


                   move $t8, $t0
                   move $t9, $t4
                   sub $t0, $t8, $t9


                   sw $t0, a


                   la $t1, a
                   sw $t1, 0($sp)    
                   jal print_int

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, str_literal_5
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall


                   lw $t8, x
                   lw $t9, x
                   add $t0, $t8, $t9


                   move $t8, $t0
                   lw $t9, x
                   add $t0, $t8, $t9


                   move $t8, $t0
                   lw $t9, y
                   sub $t0, $t8, $t9


                   move $a0, $t0
                   li $v0, 1
                   syscall

                   li $a0, 32
                   li $v0, 11
                   syscall

                   la $t1, str_literal_6
                   sw $t1, 0($sp)    
                   jal print_str

                   li $a0, 10
                   li $v0, 11
                   syscall

.data
	x: .word 1
	y: .word 2
	z: .word 0
	a: .word 0
	str_literal_0: .asciiz "x ="
	str_literal_1: .asciiz "y ="
	str_literal_2: .asciiz "x // y = "
	str_literal_3: .asciiz "y // x = "
	str_literal_4: .asciiz "z = x * y ="
	str_literal_5: .asciiz "should be -1"
	str_literal_6: .asciiz "should be 1"