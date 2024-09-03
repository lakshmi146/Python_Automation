#using loop
my_list = [1, 2, 3, 4, 5]

# Modify elements based on a condition
for i in range(len(my_list)):
    if my_list[i] % 2 == 0:  # if the element is even
        my_list[i] *= 2  # multiply by 2

print(my_list)  # Output: [1, 4, 3, 8, 5]
