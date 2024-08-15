# Get two numbers from the user (float or int)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
maximum = max(num1, num2)
power = num1 ** num2
subtraction = num1 - num2
multiplication = num1 * num2
addition = num1 + num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Print results with formatted output
#formated_number = f"{number:.9f}"
print(f"Maximum of {num1} and {num2}: {maximum}")
print(f"{num1} raised to the power of {num2}: {power}")
print(f"Subtraction ({num1} - {num2}): {subtraction}")
print(f"Multiplication ({num1} * {num2}): {multiplication}")
print(f"Addition ({num1} + {num2}): {addition}")
print(f"Division ({num1} / {num2}): {division}")

# round off the decimals

# Get two numbers from the user (float or int)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
maximum = max(num1, num2)
power = num1 ** num2
subtraction = num1 - num2
multiplication = num1 * num2
addition = num1 + num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Print results with formatted output and rounding
print(f"Maximum of {num1} and {num2}: {maximum:.1f}")
print(f"{num1} raised to the power of {num2}: {power:.2f}")
print(f"Subtraction ({num1} - {num2}): {subtraction:.2f}")
print(f"Multiplication ({num1} * {num2}): {multiplication:.2f}")
print(f"Addition ({num1} + {num2}): {addition:.2f}")
print(f"Division ({num1} / {num2}): {division:.2f}" if num2 != 0 else f"Division ({num1} / {num2}): {division}")
