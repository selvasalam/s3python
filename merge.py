def get_user_dict(n):
    user_dict = {}
    for i in range(n):
        key = input(f"Enter key {i+1}: ")
        value = input(f"Enter value {i+1}: ")
        user_dict[key] = value
    return user_dict
n1 = int(input("How many items in the first dictionary? "))
print("Enter items for the first dictionary:")
dict1 = get_user_dict(n1)


n2 = int(input("\nHow many items in the second dictionary? "))
print("Enter items for the second dictionary:")
dict2 = get_user_dict(n2)
merged_dict = {**dict1, **dict2}

print("\nFirst dictionary:", dict1)
print("Second dictionary:", dict2)
print("Merged dictionary:", merged_dict)
