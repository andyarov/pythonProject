class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Name:", self.name, "salary:", self.salary)


empl = Employee("Tom", 50000)
empl.display_employee()
