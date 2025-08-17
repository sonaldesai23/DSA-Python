# When object of child class is created , the const & destructor of class A(Parent) isnot called.

class A:
    def __init__(self):
        print("Constructor of calss A.")
    def __del__(self):
        print("Destructor of class A")
class B(A):
    def __init__(self):
        A.__init__(self)
        print("Constructor of class B")
    def __del__(self):
        A.__del__(self)
        print("Destructor of class B")
    
obj = B()
