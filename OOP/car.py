class Car:
    # class variable
    wheels = 4

    def __init__(self, make, model, year, color):
        # these are instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # def drive(self):
    #     print('This ' + self.model + ' is driving')

    # def stop(self):
    #     print('This ' + self.model + ' car is stopped')
