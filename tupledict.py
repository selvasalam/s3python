n = int(input("How many key-value pairs do you want to enter? "))
pairs = []
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value {i+1}: ")
    pairs.append((key, value))
tuple_of_pairs = tuple(pairs)
result_dict = dict(tuple_of_pairs)
print("Tuple of key-value pairs:", tuple_of_pairs)
print("Converted dictionary:", result_dict)
