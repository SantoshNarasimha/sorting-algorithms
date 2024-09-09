class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.key == None:
            self.key = data
            return
        
        if data == self.key:
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                
    def search(self, data):
        if self.key == data:
            print("Given data is found")
            return
        
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not found")
                
                
    def pre_order(self):
        print(self.key, end = " ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
    
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end = " ")
            
            
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key, end = " ")
        if self.rchild:
            self.rchild.in_order()
                
          
b = BST(None)
b.insert(90)
b.insert(900)
b.search(900)
b.insert(899)
b.pre_order()
print()
b.post_order()
print()
b.in_order()