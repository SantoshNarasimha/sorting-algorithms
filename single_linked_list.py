class node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linked_list:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.ref


    def __str__(self):
        curv = self.head

        result = ''

        while curv != None :
            result = result + str(curv.data) + '->'
            curv = curv.ref

        return result[:-2]

    def add_begin(self, data):
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def add_after(self, data, x):
        new_node = node(data)
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                else:
                    n = n.ref
            if n is None:
                print("Given node is not present in linked list")
            else:
                new_node.ref = n.ref
                n.ref = new_node
                
    def add_before(self, data, x):
        new_node = node(data)
        if self.head == None:
            print("Linked list is empty")
        if self.head.data == x:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
            return
            
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            else:
                n = n.ref
        if n is None:
            print("Given node is not present in linked list")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def delete_frst(self):
        if self.head is None:
            print("Linked list is empty so we can't perform delete operation")
        else:
            self.head = self.head.ref
            
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty so we can't perform delete end operation")
        elif self.head.ref == None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    
    def delete_specific(self, x):
        if self.head is None:
            print("Linked list is empty so we can't perform delete specific operation")
        elif self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref.data != x:
                n = n.ref
            n.ref = n.ref.ref
            
            
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.ref:
            slow = slow.ref
            fast = fast.ref.ref
        print(slow.data)
            


ll1 = linked_list()
ll1.add_begin(20)
ll1.add_begin(39)
ll1.add_end(22)
ll1.add_after(200, 22)
ll1.add_before(900, 200)
ll1.delete_frst()
ll1.delete_end()
ll1.delete_specific(20)
ll1.find_middle()
ll1.traverse()
#ll1.traverse()