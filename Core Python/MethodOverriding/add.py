class demo:
    def add(self, a, b):
        print("Addition is:", (a+b))
    def add(self, a, b, c = 0):
        #using default value argument
        print("Addition is:", (a+b+c))
d = demo()
d.add(10,20)
d.add(10,20,30)
