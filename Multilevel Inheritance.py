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


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, teamSize):
        super().__init__(name, age, employee_id, salary)  
        self.department = department
        self.teamSize = teamSize

    def display_manager_details(self):
        employee_details = self.display_employee_details()
        return f"{employee_details}, deparment:- {self.department}, team size:-- {self.teamSize}"


if __name__ == '__main__':
    manager = Manager("megha jaiswal", 67,"E234", 65000, "research and development", 13 )

    print(f"manager details{manager.display_manager_details()}")         