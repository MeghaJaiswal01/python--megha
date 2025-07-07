class Animal:
    def speak(self):
        return "animal can speak"
    
class Dog(Animal):
    def speak(self):
         return "woof!"
    

class Cat(Animal):
    def speak(self):
        return "meow!"


def make_animal_speak(animal):
        print(animal.speak())


if __name__ == "__main__":
     dog = Dog()
     cat = Cat()



     make_animal_speak(cat)
     make_animal_speak(dog)