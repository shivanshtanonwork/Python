class Employee:
    company = "OpenAI" # THis is a class attribute


    def __init__(self, salary, name, company ):
        self.salary = salary  
        self.name = name
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. Company name is {self.company}.")

e1 = Employee(350000,"Shivansh","MetaAI")
print(e1.company) # will always print instance attribute whenever present
print(Employee.company)

# Object Introspection
print(dir(e1))