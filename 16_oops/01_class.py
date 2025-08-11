# Class: is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, etc

# Object: Specific instance created from the template(class). Eg. Form which contains the data from Shivansh

class Employee:
    company = "Google"

    def get_salary(self): #self is important here because self is a way to reference the objects of the class which is being created.
        print(self)
        return 90000
    
e1 = Employee() # An object of class Employee is created here
print(e1.get_salary()) # Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)