class test1:
    def __init__(self):
        print("This is constructor.")
    def __del__(self):
        print("This is destructor.")
        
print("Declaring obj 1")
t1 = test1()
t1.__init__()
t1.__del__()
print("Last line")
