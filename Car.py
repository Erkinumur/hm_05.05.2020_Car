class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, distance):
            self.odometer += distance

    def __subtract_fuel(self, consumption):
        self.fuel -= consumption

    def drive(self, distance):
        consumption = distance / 10
        if self.fuel < consumption:
            print(f'“Need more fuel, please, fill more! (min {consumption - self.fuel:.2f})”')
        else:
            self.__add_distance(distance)
            self.__subtract_fuel(consumption)
            print("Let’sLet’sdrive!")

car1 = Car('Mercedes', 'E350', 2010)

car1.drive(200)

car1.drive(300)

car1.drive(133)

car1.drive(263)
print(f'odometer = {car1.odometer}')
print(f'fuel = {car1.fuel:.2f}')