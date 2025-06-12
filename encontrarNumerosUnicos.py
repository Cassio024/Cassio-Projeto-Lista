def unique_numbers(numbers):
    hash_table = {}
    for num in numbers:
        hash_table[num] = hash_table.get(num, 0) + 1
    return [num for num, count in hash_table.items() if count == 1]


numbers = [1, 2, 2, 3, 4, 5, 6, 66, 7, 8, 9, 99]
print(unique_numbers(numbers))  