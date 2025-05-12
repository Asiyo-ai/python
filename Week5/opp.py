# Defining a class
class Car:
    color = "red"  # Attribute
    model = "Toyota"  

    # Method
    def drive(self):
        print("The car is driving ")
    
    def stop(self):
        print("The car has stopped ")
    
class Truck:
    color = "blue"  # Attribute
    model = "Ford"  

    # Method
    def drive(self):
        print("The truck is driving ")
    
    def stop(self):
        print("The truck has stopped ")

# Loop to demonstrate polymorphism
for vehicle in [Truck(), Car()]:
    vehicle.drive()
    vehicle.stop()
        
    # # Method
    # def drive(self):
    #     print("The truck is driving ")
    # def stop(self):
    #     print("The truck has stopped ")
    # def park(self):
    #     print("The truck is parked")
# # Creating an object
# my_car = Car()
# my_car.drive()
# my_car.stop()
# my_car.park()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# personDetails= Person ("John", 30)
# print(personDetails.name)
# print(personDetails.age)

# class SecretStash:
#     def __init__(self):
#         self.__chocolates = 0  # Private attribute

#     def take_chocolate(self):
#         if self.__chocolates > 0:
#             self.__chocolates -= 1
#             print("One chocolate taken!")
#         else:
#             print("No chocolates left")

# stash = SecretStash()
# stash.take_chocolate()