class Vehicle:
    def __init__ (self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")


my_car = Vehicle("Tesla","Model 3")

print(my_car.make)
print(my_car.model)
my_car.moves()
