class Employee:
    def __init__(self, name,employee_ID, salary):
        """initializes the employee class with employee details"""
        self.name = name
        self.employee_ID = employee_ID
        self.salary = salary

    def display_details(self):
        """
        displays the employee's details. 
        """
        return f"Employee Name:- {self.name}\n employee ID:- {self.employee_ID}\n. salary:- {self.salary:.2f}."
    

class Manager(Employee):
    def __init__(self, name, employee_ID, salary,team_size):
        """
        Initializes the manager class, which inherits from Employee(parent) class
        """
        super().__init__(name, employee_ID, salary)
        self.team_size = team_size

    def display_details(self):
        """
        displays manager details inlude team size
        """
        employee_details = super().display_details()
        return f"{employee_details}\n team size:- {self.team_size}"
    
if __name__ ==  "__main__":

#create intance of manager, emoloyee
     employee = Employee("Employee1", "E001", 50000)
     manager = Manager("manager", "M345", 80000, 8)


     print("employee details:-",employee.display_details())
     #print(employee.display_details())
      
     print("\nmanager details-")
     print(manager.display_details())
