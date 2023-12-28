class Person:
    def __init__(self, name, sur_name, age, weight):
        self.name = name
        self.sur_name = sur_name
        self.age = age
        self.weight = weight

    def display_info(self):
        print(f"Меня зовут {self.name} \nмоя фамилия {self.sur_name} \nмой возраст {self.age} \nмой вес {self.weight}")


person_first = Person("Argen", "Bagylov", 1234, 88)
person_second = Person("Aitbek", "Bakytbekov", 4321, 79)

person_first.display_info()
person_second.display_info()


class Transport:

    def __init__(self, name, model, volume, fuel):  # fuel топливо
        self.name = name,
        self.model = model,
        self.volume = volume,
        self.fuel = fuel

    def info(self):
        print(
            f'Название транспорта: {self.name} \nМарка транпорта: {self.model} \nОбьем транспорта: {self.volume} \nДВС: {self.fuel}')


class Car(Transport):

    def __init__(self, name, model, volume, fuel):
        super().__init__(name, model, volume, fuel)

    def info(self):
        print(
            f'Название транспорта: {self.name} \nМарка транпорта: {self.model} \nОбьем транспорта: {self.volume} \nДВС: {self.fuel}')


class CarReal(Car):

    def __init__(self, name, model, volume, fuel, brand, year):
        super().__init__(name, model, volume, fuel)
        self.brand = brand,
        self.year = year

    def info_car(self):
        super().info()
        print(f'Бренд: {self.brand} \nГод выпуска: {self.year}')


real_car = CarReal(name='Car1', model='Civic', volume=1500, fuel='Газ', brand='Honda', year=2022)
real_car.info()


class Truck(Transport):

    def __init__(self, name, model, volume, fuel, cargo):
        super().__init__(name, model, volume, fuel)
        self.cargo = cargo

    def info(self):
        super().info()
        print(f'Грузоподъемность грузовика: {self.cargo}')


class TruckReal(Truck):

    def __init__(self, name, model, volume, fuel, cargo, manufacturer, year):
        super().__init__(name, model, volume, fuel, cargo)
        self.manufacturer = manufacturer
        self.year = year

    def info_truck(self):
        super().info()
        print(f'Производитель: {self.manufacturer} \nГод выпуска: {self.year}')


real_truck = TruckReal(name='Truck1', model='BigHauler', volume=15000, fuel='Дизель', cargo=8000,
                       manufacturer='Volvo', year=2021)
real_truck.info()
