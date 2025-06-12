def hash_length(key, table_size):
    return len(key) % table_size


sizes = ["A", "AA", "AAA", "AAAA"]
table_size = 10
for size in sizes:
    print(f"Hash de {size}: {hash_length(size, table_size)}")