name = input("What is your name?")
print("Welcome", name)

age = int(input("Enter your age: "))

if age > 18:
    print("You are an adult")
else:
    print("You are young")


i = age
while i > 0:
    print(i)
    i = i - 1

print("Lift off!")
