class stud:
    def __init__(self, roll, nm):
        self.roll = roll
        self.nm = nm

    def show(self):
        print("Roll no is:", self.roll)
        print("Name is:", self.nm)

roll = int(input("Enter roll no:"))
nm = str(input("Enter name:"))
s = stud(roll, nm)
s.show()