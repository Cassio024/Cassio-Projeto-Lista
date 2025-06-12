def hash_prime_mapping_title(key, table_size):
    prime_mapping = {
        'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23,
        'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59,
        'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101
    }
    total = sum(prime_mapping[char] for char in key.lower() if char in prime_mapping)
    return total % table_size

# Exemplo de uso
titles = ["Maus", "Fun Home", "Watchmen"]
table_size = 10
for title in titles:
    print(f"Hash de \"{title}\": {hash_prime_mapping_title(title, table_size)}")