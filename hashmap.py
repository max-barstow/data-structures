from linked import DictLinkedList

class DictPoint:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class hashmap:
    def __init__(self, hash_func, size):
        self.hash_func = hash_func
        self.table = [None for i in range(size)]

class hashmap_chaining(hashmap):
    def insert(self, key, value):
        hash_pos = self.hash_func(key)
        if self.table[hash_pos]:
            self.table[hash_pos].insert(key, value)
        else:
            self.table[hash_pos] = DictLinkedList(key, value)

    def search(self, key):
        hash_pos = self.hash_func(key)
        if self.table[hash_pos]:
            return self.table[self.hash_func(key)].search(key).value
        return None
    
    def delete(self, key):
        hash_pos = self.hash_func(key)
        if self.table[hash_pos]:
            self.table[hash_pos].delete(key)

class hashmap_linear_probing(hashmap):
    def insert(self, key, value):
        hash_pos = self.hash_func(key)
        while self.table[hash_pos]:
            hash_pos += 1
        self.table[hash_pos] = DictPoint(key, value)

    def search(self, key):
        hash_pos = self.hash_func(key)
        while self.table[hash_pos] and self.table[hash_pos].key != key:
            hash_pos += 1
        if self.table[hash_pos]:
            return self.table[hash_pos].value
        return None

    def delete(self, key):
        hash_pos = self.hash_func(key)
        while self.table[hash_pos] and self.table[hash_pos].key != key:
            hash_pos += 1
        del self.table[hash_pos]
        self.table[hash_pos] = None
