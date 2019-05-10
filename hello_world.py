from collections import OrderedDict

# python 类

OrderedDict()


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage
        print(self.odometer_reading)


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(1)


class ElectricCar(Car):

    def __init__(self, make, model, year, self_burn):
        """"""
        super().__init__(make, model, year)
        self.self_burn = self_burn
        self.battery = Battery()


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def get_battery_size(self):
        print(self.battery_size)


tesla = ElectricCar('tesla', 'model S', 2018, True)
tesla.battery.get_battery_size()
print(tesla.get_descriptive_name())
