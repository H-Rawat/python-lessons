# prevents a user from creating an object of that class
# compels a user to override abstract methods in a child class

# abstract class --> class which contains one or more abstract methods
# abstract methods --> a method that has a declaration but doesnt have an implementation

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print('You drive the car')

    def stop(self):
        print("this is stopped")


class Motorcycle(Vehicle):
    def go(self):
        print('You ride the motorcycle')

    def stop(self):
        print("this is stopped")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()
