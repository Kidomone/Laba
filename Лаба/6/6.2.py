class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return "Марка: {}, Модель: {}".format(self.make, self.model)
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"
vehicle = Vehicle("Toyota", "Camry")
print(vehicle.get_info())
car = Car("Honda", "Civic", "Бензин")
print(car.get_info())


