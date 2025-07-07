class Person:
    def __init__(self, name, age):
          """
          initializes person class with details
          """
          self.name = name
          self.age = age

    def display_personal_details(self):
          return f"name:-{self.name}, age-- {self.age}"


class Employee(Person):
    def __init__(self,name, age, employee_id, salary ):
        self.employee_id = employee_id
        self.salary = salary
        Person.__init__(self,name,age)

    def display_employee_details(self):
        personal_details = self.display_personal_details()
        return f"{personal_details}, employee ID-- {self.employee_id}, salary-- ${self.salary:.2f}" 


class Manager(Person):
    def __init__(self, name, age, department, teamSize):
        super().__init__(name, age)  
        self.department = department
        self.teamSize = teamSize

    def display_manager_details(self):
        Personal_details = self.display_personal_details()
        return f"{Personal_details}, deparment:- {self.department}, team size:-- {self.teamSize}"


if __name__ == '__main__':
    manager = Manager("megha jaiswal", 67, "research and development,",14 )
     
    print(f"manager details {manager.display_manager_details()}")    

    employee = Employee("alka",27, "E143", 10000)
    print(F"Employee details  {employee.display_employee_details()}")