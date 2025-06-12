
def hash_constant(key):
    return 1


def hash_length(key):
    return len(key) % 10


def hash_first_char(key):
    return ord(key[0].lower()) % 10


def hash_prime_mapping(key):
    prime_mapping = {
        'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23,
        'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59,
        'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101
    }
    total = sum(prime_mapping[char] for char in key.lower() if char in prime_mapping)
    return total % 10


keys = ["bag", "apple", "banana", "grape", "orange"]
print("Hash Constant:")
for key in keys:
    print(f"{key}: {hash_constant(key)}")

print("\nHash Length:")
for key in keys:
    print(f"{key}: {hash_length(key)}")

print("\nHash First Character:")
for key in keys:
    print(f"{key}: {hash_first_char(key)}")

print("\nHash Prime Mapping:")
for key in keys:
    print(f"{key}: {hash_prime_mapping(key)}")