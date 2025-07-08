
user_input = input("Enter numbers separated by spaces: ")

numbers = user_input.split()
numbers = [int(num) for num in numbers]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)
