class MyHashSet:

    def __init__(self):
        self.hset = []

    def add(self, key: int) -> None:
        for i in self.hset:
            if i==key:
                return
        self.hset.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hset)):
            if self.hset[i]==key:
                self.hset = self.hset[:i] + self.hset[i+1:]
                break
        return
    def contains(self, key: int) -> bool:
        for i in range(len(self.hset)):
            if self.hset[i]==key:
                return True
        return False