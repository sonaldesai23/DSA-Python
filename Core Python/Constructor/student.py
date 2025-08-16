class student:
    def __init__(self):
        self.roll = 1
        self.nm = "abc"
    def show(self):
        print("Roll no is:", self.roll)
        print("Name is:", self.nm)

s = student()
s.show()