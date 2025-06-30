


#class - create our own implementation

class Employee:
    #constructor - this method is invoked automatically when object is created
    def __init__(self,name):
        self.name = name
    def displayName(self):
        print("Emp name :",self.name)

# object creation
emp1 = Employee('Ram')
emp1.displayName()

emp2 = Employee('Rao')
emp2.displayName()

emp3 = Employee('Gita')
emp3.displayName()

