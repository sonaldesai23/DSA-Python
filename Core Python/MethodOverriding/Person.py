class Person:
    def __init__(self, nm) :
        self.nm = nm
    def getname(self):
        return self.nm
    def isEmp(self):
        return False
class Emp(Person):
    def isEmp(self):
        return True

emp = Person("Ravi")
print("Name:", emp.getname())
print("IsEmployee? -", emp.isEmp())

emp = Emp("Darshit")
print("Name:", emp.getname())
print("IsEmployee? -", emp.isEmp())

# Name: Ravi
# IsEmployee? - False
# Name: Darshit
# IsEmployee? - True