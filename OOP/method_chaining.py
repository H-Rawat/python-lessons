# calling multiple methods sequentially

class Car:
    def turn_on(self):
        print('start the engine')
        return self

    def drive(self):
        print('drive')
        return self

    def brake(self):
        print('stop')
        return self

    def turn_off(self):
        print('stop the engine')
        return self


car = Car()

# car.turn_on().drive()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
