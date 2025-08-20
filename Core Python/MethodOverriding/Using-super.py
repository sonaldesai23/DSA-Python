class A:
    def sayhello(self):
        print("Hello From A")
class B(A):
    def sayhello(self):
        print("Hello From B")
    def greet(self):
        super().sayhello()
        self.sayhello
b1 = B()
b1.greet()