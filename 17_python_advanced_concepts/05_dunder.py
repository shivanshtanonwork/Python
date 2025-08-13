class Employee:
    company = "Morgan Stanley"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}"
    
    def __repr__(self): # used by devs to debug
        return f"name: {self.name} \nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)

e = Employee("Shivansh", 200000)
print(len(e))
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))