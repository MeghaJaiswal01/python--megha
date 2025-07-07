class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"hello, I am {self.name}"
    

class Employee:
    def __init__(self, employee_ID):
        self.Employee_ID = employee_ID

    def get_employee_id(self):
        return self.Employee_ID
    

class Manager(Person, Employee):
    def __init__(self, name, employee_ID, password):
        self.password = password
        Person.__init__(self, name)
        Employee.__init__(self, employee_ID)


if __name__ == '__main__':
     manager = Manager('meera', 'E234', 'm@123')

     print(manager.greet())
     print (f"Employee ID-- {manager.get_employee_id()}")
     print(F"Employee ID password:--{manager.password}")

        