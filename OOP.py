# from turtle import Turtle, Screen
# my_screen=Screen()
# donatello = Turtle()
# print(my_screen.canvwidth)
# donatello.shape('turtle')
# donatello.color('purple')
# donatello.forward(100)
# donatello.right(90)
# donatello.forward(100)
# donatello.right(90)
# donatello.forward(100)
# donatello.right(90)
# donatello.forward(200)
# donatello.home()
# raphael=Turtle()
# raphael.color('red')
# raphael.shape('turtle')
# raphael.penup()
# raphael.goto(-150,200)
# raphael.pendown()
# raphael.pencolor('blue')
#
# x=10
# while x<=50:
#     raphael.circle(x)
#     donatello.circle(x+5)
#     x += 10
# my_screen.exitonclick()
# class Robot:
#     """This class implements a Robot."""
#     population = 0 #class attrubute
#     def __init__(self, name, year):
#         self.name=name
#         self.year=year
#         Robot.population +=1
#     def __del__(self):
#         print('robot Destroyed')
#     def setEnergy(self, energy):
#         self.energy= energy
#
#
# r1=Robot('R1', 2024)
# r2= Robot('Ben', 2040)
# print(r1.__doc__)
# print(f'Robot name: {r1.name}')
# r1.setEnergy(500)
# print(r1.energy)
# print(getattr(r1, 'energy'))
# print(r1.__dict__)
#
# print(f'Robots alive: {Robot.population}')
###MAGIC METHODSSSSS
class Robot:
    """This class implements a Robot."""
    population = 0 #class attrubute
    def __init__(self, name, price):
        self.name=name
        self.price=price
        Robot.population +=1
    def __del__(self):
        print('robot Destroyed')
    def __str__(self):
        my_str = f'My name is {self.name} and my price is {self.price}'
        return my_str
    def __add__(self, other):
        price = self.price + other.price
        return price

r1=Robot('Marvin', 150)
r2 = Robot('Gal', 45)
print(r1)
print(r1+r2)
