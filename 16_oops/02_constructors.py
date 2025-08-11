class Employee:
    def __init__(self, salary, name, company ):
        self.salary = salary  #Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. Company name is {self.company}.")


e1 = Employee(100000,"Shivansh", "Morgan Stanley")
print(e1.get_salary())
e1.get_info()