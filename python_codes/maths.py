x = 1
y = 2
z = x * y
a = x // y

print("x =", x)
print("y =", y)
print("x // y = ", a)
print("y // x = ", y // x)
print("z = x * y =", z)

a = x + y - z + z - y - x * z

print(a, "should be -1")
print(x+x+x-y, "should be 1")
