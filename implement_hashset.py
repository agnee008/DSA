class HashSet:
    
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
        
    def _hash(self, key):
        return key % self.size
    
    def add(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        if key not in self.bucket:
            bucket.append(key)
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        if key in self.bucket:
            bucket.remove(key)
            
    def contains(self, key):
        index = self._hash(key)
        return key in self.table[index]