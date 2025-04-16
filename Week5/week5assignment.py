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