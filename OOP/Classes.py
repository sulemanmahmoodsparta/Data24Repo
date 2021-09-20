class Dog:  # Classes should start with capital letters.

    animal_kind = "canine"  # Class variable

    def bark(self):  # Self means referring to the current class.
        return "Woof!"


# print(Dog.animal_kind)
# print(Dog().bark())
Dog.animal_kind = "Dolphin"

fido = Dog()
lassie = Dog()
# instantiation ^ Creating an instance of an object. So lassie and fido are both instances of an object.
fido.animal_kind = "Big Dog"

# Essentially allows you to make a lot of 'Dogs' really easily.
# You change attributes independently for each of the dogs.

print(fido.animal_kind)
print(lassie.animal_kind)

# learn about them in non-technical terms.

# 4 pillars:
#           abstraction - abstracts away the complicated stuff.
#           Encapsulation - hiding things from the user.

#           inheritance - a class can inherit attributes from another class. normally when making a sub-class
#           polymorphism - flexibility as things can be changed quite easily. Can overwrite.


# presentation - intro what is OOP?
# - 4 pillars : talk about them using real life objects.
# demonstrate the pillars are memorable and clear.
# show some code of us editing our dog class.
