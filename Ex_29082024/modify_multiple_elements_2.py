#using list comprehensions

my_list = [1, 2, 3, 4, 5]

# Modify elements based on a condition using a list comprehension
my_list = [x * 2 if x % 2 == 0 else x for x in my_list]

print(my_list)  # Output: [1, 4, 3, 8, 5]
