class Person:
    def __init__(self, nm, id):
        self.nm = nm
        self.id = id
class Employee(Person):
    def __init__(self, nm, id, sal, post):
        Person.__init__(self, nm, id)
        self.sal = sal
        self.post = post
    def display_emp(self):
        print("Name:", self.nm)
        print("ID Numbers:", self.id)
        print("Salary:", self.sal)
        print("Post:", self.post)
        
e1 = Employee("Sonal", 21, 34555, "HR")
e1.display_emp()
