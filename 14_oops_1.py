# # Inheritance => Inheriting from other class
# # Polymorphism ==> same function using for diff class with small changes
# class Animal:
#
#     def __init__(self):
#         print("Animal is created")
#
#     def who_am_i(self):
#         print("i am an animal")
#
#     def eat(self):
#         print("I am eating")
#
#
# class Dog(Animal):
#     def __int__(self):
#         self.eat()
#
#     def who_am_i(self):
#         print("i am an Bird")
#
#
# dog = Dog()
# animal = Animal()
# for pet in [dog, animal]:
#     print(pet.eat())
#
# dog.who_am_i()
#


#  HOMEWORK

class Line:

    def __int__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x1 = self.coor1[0]
        self.x2 = self.coor1[1]
        self.y1 = self.coor2[0]
        self.y2 = self.coor2[1]

    def distance(self):
        return ((self.x2 - self.x1)**2 - (self.y2 - self.y1)**2) * 0.5

    def slope(self):
        return (self.y2 - self.y1)/(self.x2 - self.x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line()
distance = li.distance()
print(distance)
# print((li.slope()))



# class Cyllinder:
#
#     def __int__(self, h1, h2):
#         self.h1 = h1
#         self.h2 = h2
#
#     def volume(self):
#
#
#     def surface_area(self):
#
#
#
# c= Cyllinder(2, 3)

