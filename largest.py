def get_largest_number():
    user_input = input("Enter numbers separated by spaces: ")
    number_strings = user_input.split()

    numbers = [float(num) for num in number_strings]

    largest = max(numbers)

    print(f"The largest number is: {largest}")
get_largest_number()
