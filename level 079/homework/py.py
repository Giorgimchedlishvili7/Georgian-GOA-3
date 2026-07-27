numbers = [1, 2, 3, 4, 5]

containing_numbers = [num for num in numbers if num % 2 == 0]


print(containing_numbers)


words = ["apple", "banana", "kiwi", "strawberry", "pear", "orange"]

filtered_words = [word for word in words if len(word) > 5]

print(filtered_words)