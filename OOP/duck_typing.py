# concept where the class of an object is less important than the methods/attributes
# class type is not checked if minimum methods/attributes are present

class Duck:
    def walk(self):
        print('this duck is walking')

    def talk(self):
        print('this duck is talking')


class Chicken:
    def walk(self):
        print('this chicken is walking')

    def talk(self):
        print('this chicken is talking')


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('you caught the duck')


duck = Duck()
chicken = Chicken()
person = Person()

# person.catch(duck)

# this is not a problem since the Chicken object also has the same methods as the Duck Object
person.catch(chicken)
