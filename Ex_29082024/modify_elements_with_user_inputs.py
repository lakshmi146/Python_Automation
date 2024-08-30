# Step 1: Get list elements from the user
user_input = input("Enter the elements of the list separated by spaces: ")
my_list = list(map(int, user_input.split()))

# Step 2: Ask the user which indices they want to modify
indices_input = input("Enter the indices of elements to modify, separated by spaces: ")
indices_to_modify = list(map(int, indices_input.split()))

# Step 3: Ask for the new values for the specified indices
for index in indices_to_modify:
    if 0 <= index < len(my_list):
        new_value = int(input(f"Enter the new value for element at index {index}: "))
        my_list[index] = new_value
    else:
        print(f"Index {index} is out of range.")

print("Modified list:", my_list)
