#string format concept

# Get the number from the user
number = int(input("Enter a number to print its multiplication table: "))

# Loop to print the table
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#float

# Get the number from the user (float or int)
number = float(input("Enter a number (integer or float) to print its multiplication table: "))

# Loop to print the table
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

