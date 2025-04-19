class Animal:
    def move(self):
        pass  

class Dog(Animal):
    def move(self):
        return "🐕 Running on four legs!"

class Fish(Animal):
    def move(self):
        return "🐟 Swimming in water!"

class Bird(Animal):
    def move(self):
        return "🦅 Flying through the air!"

class Snake(Animal):
    def move(self):
        return "🐍 Slithering on the ground!"


animals = [Dog(), Fish(), Bird(), Snake()]


for animal in animals:
    print(animal.move())