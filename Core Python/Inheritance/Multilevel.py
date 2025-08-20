class A:
    a = 10
    def methd1(self):
        print("Method1 of A")
class B(A):
    b = 20
    def methd2(self):
        print("Method2 of B")
class C(B):
    c = 30
    def methd3(self):
        print("Method3 of C")

obj = C()
obj.methd1()
obj.methd2()
obj.methd3()
print("a=",obj.a)
print("b=",obj.b)
print("c=",obj.c)