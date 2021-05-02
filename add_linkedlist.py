class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self ,data):
        self.head = Node(data, self.head)

    
    def printll(self):
        x = self.head
        if x != None:
            num = ''
            while x:
                num = num + str(x.data)
                x = x.next 
            return num


def createll(data):
    ll3 = LinkedList()
    arr = [int(i) for i in str(data)]

    for i in arr:
        ll3.insert_at_head(i)
    
    return ll3



if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_at_head(3)
    ll1.insert_at_head(4)
    ll1.insert_at_head(2)
    num1 = int(ll1.printll())
    ll2 = LinkedList()
    ll2.insert_at_head(4)
    ll2.insert_at_head(6)
    ll2.insert_at_head(5)
    num2 = int(ll2.printll())
    num3 = num1 + num2
    ll3 = createll(num3)
    print(ll3.printll())

