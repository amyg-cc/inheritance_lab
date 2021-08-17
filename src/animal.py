class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        return "Yummy!"

class Cat(Animal): 
    def __init__(self, name, species, breed, fur):
        super().__init__(name, species)
        self.breed = breed
        self.fur = fur

    def eat(self):
        return "Yummy birds!"

class Chicken(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.eggs = 0

cat = Cat("Fluffy", "Cat", "Ragdoll", "Grey")
print(cat.fur)
print(cat.eat())

chicken = Chicken("Betty", "chicken")
print(chicken.eggs)
print(chicken.eat())