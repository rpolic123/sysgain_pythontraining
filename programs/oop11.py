

# Parent class
class Vehicle:
    def start_engine(self):
        print("Engine started.")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is being driven.")

# Create object of child class
my_car = Car()

# Call methods from both parent and child
my_car.start_engine()  # Inherited from Vehicle
my_car.drive()         # Defined in Car