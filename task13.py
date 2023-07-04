class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_employee(self):
        print("Name:", self.name, "salary:", self.salary)

    def display_count(self):
        print("All ", Employee.emp_count)


empl = Employee("Tom", 50000)
empl.display_employee()


class Freelance(Employee):

    def __init__(self, name, salary, email):
        super().__init__(name, salary)
        self.email = email

    def display_email(self):
        print("email:", self.email)


empl2 = Freelance("Jerry", 80000, "mail@mail.ru")
empl2.display_email()
empl2.display_employee()
