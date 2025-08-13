class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property    
    def first_name(self):
        l = self.name.split(" ")
        # print(l)
        return l[0]
    
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

    @property
    def set_salary(self):
        return self._salary 
    
    @set_salary.setter
    def get_salary(self, new_salary):
        self._salary = new_salary

e = Employee("Shiva Tandon", 110000)
print(e.first_name)

print(e.first_name)
e.first_name = "Shivansh"
print(e.name)

e.get_salary = 150000
print(e.get_salary)
# e.projects = 10
# print(e.projects)
