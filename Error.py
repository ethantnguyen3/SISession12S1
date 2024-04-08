class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = 0
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        return f"{year} {make} {model}"

    def read_odometer(self):
        return f"This car has {odometer_reading} miles on it."

    def update_odometer(self, mileage):
        if self.mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(miles):
        self.odometer_reading += miles


my_car = Car(self, "Toyota", "Camry", 2020)


print(get_description())
print(my_car.read_odometer())


self.odometer_reading = 100
print(my_car.read_odometer(self.odometer_reading))


my_car.update_odometer(200, 10)
print(my_car.read_odometer())


my_car.increment_odometer(50)
print(my_car.read_odometer(50))


