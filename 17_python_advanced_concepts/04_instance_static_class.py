class Employee:
    company = "Morgan Stanley"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and salary is {self.salary}"
        print(info)

    # static method - it doesnt need self
    @staticmethod
    def sum(a,b):
        return a+b

    # Class method
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod
    def change_company(cls, new_company):
        cls.company =  new_company


e1 = Employee("Shivansh", 150000)
e2 = Employee("Vidushi", 150000)
# print(Employee.company)
# print(Employee.name) # this will throw an error cause we dont have name as a class variable

e1.print_info()
e2.print_info()

# print(e2.sum(20,49))
e1.print_company()
e2.change_company("Cognizant")
e2.print_company()