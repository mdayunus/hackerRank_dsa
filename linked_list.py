class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
        
    def printll(self):
        x = self.head
        llstr = ''
        while x:
            llstr = llstr + str(x.data) + '--->'
            x = x.next
        return llstr


    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_begining(data)
        else:
            x = self.head
            while x.next != None:
                x = x.next
            x.next = Node(data)

    
    def get_len(self):
        count = 0
        x = self.head
        while x:
            count+=1
            x = x.next
        return count

    def insert_at(self, data, loc):
        lllen = self.get_len()
        if loc == 0:
            self.insert_at_begining(data)
            return
        if loc >= lllen:
            self.insert_at_end(data)
            return
        x = self.head
        count = 0
        while x:
            if count == loc - 1:
                node = Node(data, x.next)
                x.next = node
                break
            x = x.next
            count+=1
        # x = self.head
        # for i in range(loc-1):
        #     x = x.next
        # node = Node(data, x.next)
        # x.next = node

    def remove_at(self, loc):
        if loc == 0:
            self.head = self.head.next
            return
        x = self.head
        count = 0
        while x:
            if count == loc - 1:
                x.next = x.next.next
                break
            x = x.next
            count += 1



if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_end(32)
    # ll.insert_at_end(34)
    # ll.insert_at_begining(12)
    # ll.insert_at_begining(23)
    # print(ll.printll())
    # print(ll.get_len())
    # ll.insert_at(45,2)
    # print(ll.printll())
    # print(ll.get_len())
    # ll.remove_at(2)
    # print(ll.printll())
    # print(ll.get_len())
    ll.remove_at(0)
    print(ll.printll())

