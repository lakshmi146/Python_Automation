# Python program to generate Fibonacci series up to n terms

# Function to print Fibonacci series
def fibonacci_series(n):
    # Starting with the first two numbers in the Fibonacci series
    a, b = 0, 1
    # Print the first n numbers in the series
    for i in range(n):
        print(a, end=" ")
        # Calculate the next number
        a, b = b, a + b

# Input from the user: number of terms
n = int(input("Enter the number of terms: "))
