# constructor with parameter
class stud2:
    def __init__(self, a = 18, g = "Male", d = "CS"):
        self.age = a
        self.gender = g
        self.dept = d
    def show_val(self):
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Department:", self.dept)
        
s1 = stud2()
s2 = stud2(19, "Female", "IT")
print("Initialized 1st student.")
s1.show_val()
print("Reintitialized 2nd student.")
s2.show_val()
        
