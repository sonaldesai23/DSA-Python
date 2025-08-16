class test:
    def __init__(self):
        print("This is constructor.")
    def __del__(self):
        print("This is destructor.")
def fun1():
    s1 = test()
def fun2():
    s2 = test()
print("Calling fun1")
fun1()
print("Calling fun2")
fun2()