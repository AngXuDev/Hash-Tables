# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # find integer index.
        index = self._hash_mod(key)

        # check if a key/value pair already exists, if not create a linkedpair
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
        # if it does already exist:
        else:
            # pointer for current key/value
            existing = self.storage[index]
            # if key is the same then change the value to prevent duplicates
            if existing.key == key:
                existing.value = value
                return
            # if not the same then as long as there is a next, do same duplication check
            while existing.next:
                if existing.next.key == key:
                    existing.next.value = value
                    return
                # repoint the pointer
                else:
                    existing = existing.next
            # if after going through the entire list there's no identical key, create a next to the last node
            existing.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # pointer
        current = self.storage[index]

        # check for existence
        if current.key == key:
            self.storage[index] = current.next
            return

        # if not on initial level, check if on linked list
        while current.next:
            if current.next.key == key:
                # change pointer to next node in linked list
                current.next = current.next.next
                return
            # change pointer
            else:
                current = current.next

        print(f"Key not found in storage")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # store initial node
        current = self.storage[index]

        while current:
            if current.key == key:
                return current.value
            # if no match change pointer
            else:
                current = current.next
        # if not in linked list return none
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # create new array
        storage = [None] * self.capacity * 2
        # copy old storage
        old = self.storage
        # point storage to new array
        self.storage = storage
        # double capacity
        self.capacity *= 2
        # fill new array with old storage
        for i in old:
            current = i
            while current:
                self.insert(current.key, current.value)
                current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
