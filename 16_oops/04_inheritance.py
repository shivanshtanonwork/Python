class Animal: # Parent class(superclass)
    location = "India"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Generic animal sound")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using the speak function of the parent class   
        print("Woof")

# a = Animal("Dog")
# a.speak()

d = Dog("Smokey")
d.speak()
print(d.location)