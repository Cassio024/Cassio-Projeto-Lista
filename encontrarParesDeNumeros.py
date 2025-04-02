def find_pairs(numbers, target):
    hash_table = {}
    pairs = []
    for num in numbers:
        complement = target - num
        if hash_table.get(complement, 0) > 0:
            pairs.append((num, complement))
            hash_table[complement] -= 1
        else:
            hash_table[num] = hash_table.get(num, 0) + 1
    return pairs


numbers = [2, 3, 4, 7, 11, 15]
print(find_pairs(numbers, 6))  
print(find_pairs(numbers, 9))  
print(find_pairs(numbers, 20))  