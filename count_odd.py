'''🚀 Python Quick Codes: Count total odd numbers in a list.'''

numbers = [3, 2, 5, 4, 6, 8, 9, 5, 6, 7, 8, 5]

# 📋 Method-1: Using List comprehension
odd_nums = [num for num in numbers if num % 2 != 0]
print(f"Odd numbers: {odd_nums}")
print(f"Total odds: {len(odd_nums)}")

# 📋 Method-2: Using normal for loop
odd_count = 0
for num in numbers:
    if num % 2 != 0:
        odd_count += 1
print(f"Total odds: {odd_count}")

# 📋 Method-3: Using Lambda Expression
odd_count = len(list(filter(lambda x: x % 2 != 0, numbers)))
print(f"Total odds: {odd_count}")

# 👩‍💻 See you soon, Till then Keep Improving!!!🎯
