class Hashtable:
    def __init__(self):
        self.MAX_SIZE = 100
        self.container = [None for _ in range(self.MAX_SIZE)]

    def hash_function(self, key):
        num = 0
        for c in key:
            num = num + ord(c)
        return num % self.MAX_SIZE

    def __setitem__(self, key, value):
        position = self.hash_function(key)
        self.container[position] = value

    def __getitem__(self, key):
        position = self.hash_function(key)
        return self.container[position]

    def __delitem__(self, key):
        position = self.hash_function(key)
        # print(position)
        self.container[position] = None
        



if __name__ == '__main__':
    ht = Hashtable()
    ht['march 30'] = 'yunus'
    ht['30 march'] = 'baba'
    ht['11 jan'] = 'saima'

    print(ht.container)
    print(ht['march 30'])
    del(ht['march 30'])
    print(ht.container)

