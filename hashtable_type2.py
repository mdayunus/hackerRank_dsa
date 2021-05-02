class Hashtable:
    def __init__(self):
        self.MAX_SIZE = 100
        self.container = [[] for _ in range(self.MAX_SIZE)]

    def hash_function(self, key):
        num = 0
        for c in key:
            num = num + ord(c)
        return num % self.MAX_SIZE

    def __setitem__(self, key, value):
        exist = False
        position = self.hash_function(key)
        for idx, elems in enumerate(self.container[position]):
            if len(elems) == 2 and elems[0] == key:
                self.container[position][idx] = (key, value)
                exist = True
                break
        if not exist:
            self.container[position].append((key, value))

    def __getitem__(self, key):
        position = self.hash_function(key)
        for elems in self.container[position]:
            if len(elems) == 2 and elems[0] == key:
                return elems[1]
        return -1

    def __delitem__(self, key):
        position = self.hash_function(key)
        for idx, elems in enumerate(self.container[position]):
            if len(elems) == 2 and elems[0] == key:
                del self.container[position][idx]
                return
            


if __name__ == '__main__':
    ht = Hashtable()
    ht['march 30'] = 'yunus'
    ht['march 03'] = 'cr7'
    print(ht.container)
    print(ht['march 03'])
    del(ht['march 03'])
    print(ht.container)