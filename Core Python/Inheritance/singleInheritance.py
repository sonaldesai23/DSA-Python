# Single Inheritance
class Parent:
    x = 10
    def showx(self):
        print(self.x)
class child(Parent):
    y = 20
    def showy(self):
        print(self.y)
c = child()
c.showx()
c.showy()