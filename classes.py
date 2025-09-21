# Add your class definition here (steps 1-3)
class Dog:
    def __init__ (self, name, breed, doacao):
        self.name = name
        self.breed = breed
        self.doacao = doacao
    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.breed} está pronto para doação, {self.doacao}.")
    
# Creating the instance of the Dog class (step 4)
my_dog = Dog(f"Buddy", "Golden Retriever", "sim")
# Directing the dog to bark (step 5)
my_dog.bark()