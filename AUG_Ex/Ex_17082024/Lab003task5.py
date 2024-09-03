# Python program to compare two numbers

# Step 1: Get the first number from the user
num1 = float(input("Enter the first number: "))

# Step 2: Get the second number from the user
num2 = float(input("Enter the second number: "))

# Step 3: Compare the two numbers and print the appropriate message
if num1 > num2:
    print("The first number", num1, "is greater than the second number", num2)
elif num1 < num2:
    print("The first number", num1, "is less than the second number", num2)
else:
    print("The first number", num1, "is equal to the second number", num2)
