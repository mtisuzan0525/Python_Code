# Lists are used to store multiple items in a single variable
# We can change the values of the elements
# It allows duplicate values
# It maintains order
# Lists are indexed at 0

example_list = ["A", "A", "B", "C", "D", "E", "F", "G"]

print(example_list)

# Accessing the list items
print(example_list[2])

# Negative indexing
print(example_list[-3])

# Range of Indices
print(example_list[2:6])
print(example_list[:3])
print(example_list[3:])
print(example_list[-3:-1])
print(example_list[6:2]) # It will generate empty list

# Checking an item
if "D" in example_list:
    print("The item is present on the list")

# Changing the item values
example_list[1] = "New Item"
example_list.insert(2, "Inserting new value")
example_list.append("This is Append Value")
example_list.remove("A")
example_list.pop(1)
print(example_list)

# Loop Through a List
for any_variable in example_list:
    print(any_variable)