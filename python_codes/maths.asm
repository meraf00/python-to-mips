.text

j main # jump to main (entry point)

# Library





# Functions

main: # (Entry Point)


                   lw $t8, x
                   lw $t9, y
                   mul $t5, $t8, $t9


                   sw $t5, z

.data
	x: .word 1
	y: .word 2
	z: .word 0