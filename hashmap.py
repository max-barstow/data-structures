from linked import DictLinkedList

class DictPoint:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class hashmap:
    def __init__(self, hash_func, size):
        # Initialise the object storing a hash function and allocating memory
        self.hash_func = hash_func
        self.table = [None for i in range(size)]

class hashmap_chaining(hashmap):
    def insert(self, key, value):
        # Compute the location of the storage bin for the value
        hash_pos = self.hash_func(key)

        if self.table[hash_pos]:
            # If there already exists a LinkedList in the bin, add the key and value pair to it
            self.table[hash_pos].insert(key, value)
        else:
            # If not, create it
            self.table[hash_pos] = DictLinkedList(key, value)

    def search(self, key):
        # Compute the location of the storage bin for the value
        hash_pos = self.hash_func(key)

        if self.table[hash_pos]:
            # If it exists, search the LinkedList for the key and return the value
            return self.table[self.hash_func(key)].search(key).value

        # If not, return None
        return None
    
    def delete(self, key):
        # Compute the location of the storage bin for the value
        hash_pos = self.hash_func(key)
        if self.table[hash_pos]:
            # If the storage bin is not empty, attempt to delete the key
            self.table[hash_pos].delete(key)

class hashmap_linear_probing(hashmap):
    def insert(self, key, value):
        # Compute the location of the storage bin for the value
        hash_pos = self.hash_func(key)

        # Iterate the hash position until we find an empty bin
        while self.table[hash_pos]:
            hash_pos += 1

        # Store the value alongside its key
        self.table[hash_pos] = DictPoint(key, value)

    def search(self, key):
        # Compute the location of the storage bin for the value
        hash_pos = self.hash_func(key)
        
        # Iterate through the storage bins until we either 
        # find an empty one, or the bin we are looking for
        while self.table[hash_pos] and self.table[hash_pos].key != key:
            hash_pos += 1
        
        # If we found the key in a storage bin
        if self.table[hash_pos]:
            # Return the associated value
            return self.table[hash_pos].value

        # Otherwise return None
        return None

    def delete(self, key):
        # Compute the location of the storage bin for the value
        hash_pos = self.hash_func(key)

        # Search through the storage bins until we either 
        # find an empty one, or the bin we are looking for
        while self.table[hash_pos] and self.table[hash_pos].key != key:
            hash_pos += 1

        # Empty the relevant storage bin
        # If the bin is empty, these lines change nothing
        del self.table[hash_pos]
        self.table[hash_pos] = None
