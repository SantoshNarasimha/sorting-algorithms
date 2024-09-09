class node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None
        
class dd_ll:
    def __init__(self):
        self.head = None
        
    def traverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end= " ")
                n = n.nref
                
    def add_begin(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            
            
    def traverse_reverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end= " ")
                n = n.pref
                
    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
            
    def add_after(self, data, x):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                else:
                    n = n.nref
            if n.data == x:
                new_node = node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
        
    def add_before(self, data, x):
        new_node = node(data)
        n = self.head
        if n is None:
            print("Linked list is empty")
        else:
            while n is not None:
                if n.data == x:
                    break
                else:
                    n = n.nref
                    
            if n.data == x:
                new_node.pref = n.pref
                new_node.nref = n
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
                
                
dd1 = dd_ll()
dd1.add_begin(2020)
dd1.add_begin(37)
dd1.add_begin(920)
dd1.add_end(3000)
dd1.add_after(202020, 3000)
dd1.add_before(900909, 202020)
dd1.traverse()


"""
class node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None

class linked_list:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.nref

    def traverse_reverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            # Find the last node first
            n = self.head
            while n.nref is not None:
                n = n.nref

            # Then traverse backwards from the last node
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
        else:
            print("Linked list is not empty so performing add begin operation")
            self.add_begin(data)

    def add_begin(self, data):
        new_node = node(data)
        if self.head is None:
            self.insert_empty(data)
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node


    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            print("Linked list is empty so we cant perform add_end operation")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            new_node.pref = n.nref
            n.nref = new_node


pp = linked_list()
pp.insert_empty(200)

pp.add_begin(23)

pp.add_end(2002)

pp.traverse()
"""