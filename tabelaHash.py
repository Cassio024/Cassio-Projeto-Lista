class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None
    
hash_table = HashTable(10)
hash_table.insert("chave1", "valor1")
hash_table.insert("chave2", "valor2")

print(hash_table.search("chave1"))  
print(hash_table.search("chave3"))  
                        
                       