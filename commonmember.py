
list1 = input("Enter first list elements : ").split()
list2 = input("Enter second list elements : ").split()
set1 = set(list1)
set2 = set(list2)

temp = set1.copy()
temp.update(set2)

has_common = len(set1) + len(set2) > len(temp)

print("True" if has_common else "False")