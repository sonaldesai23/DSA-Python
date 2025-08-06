print("Hello world")

#Using for loop
num = int(input("Enter the number of which u want factorial:"))
fact = 1
while num > 0:
    fact *= num
    # fact *= i
    num = num -1
print("Factorial is:", fact)
