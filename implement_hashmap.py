class HashMap:
    
    def __init__(self):
        self.size = 1000
        self.table= [[] for _ in range(self.size)]
        
    def _hash(self,key):
        return key % self.size
    
    def put(self, key, value):
        index = self.hash(key)
        bucket = self.table[index]
        
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        
    def get(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
            return -1
        
    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return