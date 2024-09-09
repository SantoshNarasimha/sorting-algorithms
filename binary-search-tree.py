class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return # return function will be return from the function and doesnt execute the lines after the return statement

        #to avoid placing multiple values in trees
        if self.key == data:
            return

        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
                # if the above line executes then self.lchild will store the address of left node

        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)


    def search(self, data):
        if self.key == data:
            print("Key is found")
            return
        if data <= self.key:
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
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
        print(self.key)

    def in_order(self):
        if self.lchild:
            self.lchild.in_order()

        print(self.key, end= " ")

        if self.rchild:
            self.rchild.in_order()

root = BST(None)
list1 = [2, 22, 32, 31, 100]
for i in list1:
    root.insert(i)

root.search(100)

print("pre-order")
root.pre_order()
print()
print()

print("post-order")
root.post_order()
print()

print("in-order:")
root.in_order()
print()