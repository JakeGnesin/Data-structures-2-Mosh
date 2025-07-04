# def odd_even():
#     try:
#         user_input = int(input('Enter a number: '))
#         if user_input % 2 == 0:
#             print('Even')
#         else:
#             print('Odd')
#     except ValueError:
#         print('Please enter a valid integer')


# odd_even()

# def reverse_a_word():
#     user_input = input('Enter a word: ')
#     reversed_word = user_input[::-1]  # Reverses the string using slicing
#     print('Reversed word:', reversed_word)


# reverse_a_word()

# def count_words():
#     word_dict = {}
#     user_input = input('Enter words: ')
#     words = user_input.split()
#     for word in words:
#         word_dict[word] = word_dict.get(word, 0) + 1
#     print('Word counts', word_dict)


# count_words()


# def reverse_stack():
#     stack = []  # Initialize empty stack
#     while True:
#         user_input = input(
#             "Enter a number (or 'done' to finish): ")  # Get input
#         if user_input == 'done':  # Check for exit condition
#             break
#         try:
#             num = int(user_input)  # Convert to integer
#             stack.append(num)  # Push to stack
#         except ValueError:
#             # Handle invalid input
#             print("Please enter a valid number or 'done'")

#     # Pop and print numbers in reverse
#     print("Reversed sequence:", end=" ")
#     while stack:  # Pop until stack is empty
#         print(stack.pop(), end="")
#         if stack:  # Add comma and space unless it's the last number
#             print(", ", end="")
#     print()  # Newline at the end


# reverse_stack()

# def is_palindrome():
#     stack = []  # Initialize empty stack
#     user_input = input("Enter word: ")  # Get input word
#     for char in user_input:  # Push each character to stack
#         stack.append(char)

#     reversed_word = ""  # Build reversed word by popping
#     while stack:
#         reversed_word += stack.pop()  # Pop and append to string

#     # Compare original and reversed word
#     if user_input == reversed_word:
#         print(user_input, "is a palindrome")
#     else:
#         print(user_input, "is not a palindrome")


# is_palindrome()


# def list_of_nums():
#     numbers = []  # Initialize empty list (array)
#     while True:
#         user_input = input(
#             "Enter a number (or 'done' to finish): ")  # Get input
#         if user_input == 'done':  # Check for exit condition
#             break
#         try:
#             num = int(user_input)  # Convert to integer
#             numbers.append(num)  # Append to list
#         except ValueError:
#             # Handle invalid input
#             print("Please enter a valid number or 'done'")

#     # Calculate sum (0 if empty)
#     total = sum(numbers) if numbers else 0
#     # Print array and sum
#     print(f"Array: {numbers}, Sum: {total}")


# list_of_nums()


# def print_even_nums():
#     numbers = []
#     while True:
#         user_input = input('Enter a set of numbers (or done to finish): ')
#         if user_input == 'done':
#             break
#         try:
#             nums = int(user_input)

#             if nums % 2 == 0:
#                 numbers.append(nums)
#         except ValueError:
#             print('Enter a valid num or "done"')

#     print(numbers)


# print_even_nums()


def product_of(numbers):
    # Initialize result list with same length as input
    result = [1] * len(numbers)  # Use 1 as default for multiplication
    # Iterate through each index
    for i in range(len(numbers)):
        # Compute product of all elements except the one at index i
        product = 1
        for j in range(len(numbers)):
            if j != i:
                product *= numbers[j]
        result[i] = product
    return result


# Input collection
first_list = []
while True:
    user_input = input('Enter a number (or done): ')
    if user_input == 'done':
        break
    try:
        nums = int(user_input)
        first_list.append(nums)
    except ValueError:
        print('Enter a valid number or done')

# Call function and print result
result = product_of(first_list)
print(result)
