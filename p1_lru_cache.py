class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.lru_key_cache = dict()
        self.use_rate = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.capacity == 0:
            return "You can't get any item, because Cache capasitiy is 0"
        if key in self.cache:
            self.lru_key_cache[key] = self.use_rate
            self.use_rate += 1
            return self.cache[key]

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is
        # at capacity remove the oldest item.
        if self.capacity == 0:
            print("You can't set any item, because Cache capasitiy is 0")
            return
        if len(self.cache) >= self.capacity:  # it is full
            old_key = min(self.lru_key_cache,
                          key=lambda k: self.lru_key_cache[k])
            self.cache.pop(old_key)
            self.lru_key_cache.pop(old_key)

        self.cache[key] = value
        self.lru_key_cache[key] = self.use_rate
        self.use_rate += 1

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return -1


our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(1, 8)
our_cache.set(2, 2)
print(our_cache.get(1))  # returns 8
print(our_cache.get(2))  # returns 2
our_cache.set(3, 3)
print(our_cache.get(3))  # returns 3
print(our_cache.get(1))  # returns -1


our_cache = LRU_Cache(0)
our_cache.set(1, 1)
print(our_cache.get(1))
