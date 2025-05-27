import random
class Car():
    def __init__(self,fuel,logger):
        self.fuel_amount = fuel
        self.current_mileage = 0
        self.logger = logger
        self.car_name = 'Жигули'


    def drive(self,distance,fuel_consumption = 7.5):

        score = (distance / 100) * fuel_consumption
        if self.fuel_amount >= score:
            self.fuel_amount -= score
            self.current_mileage += distance
            self.logger.log(distance, self.fuel_amount)
            return f'Вы проехали {cars.car_name} {distance} км, осталось топливо {self.fuel_amount} литра'
        else:
            return ('Не достаточно топливо')

    def get_mileage(self):
        return self.current_mileage

    def get_colors(self,color):

        colors = ['Оранжевый', 'Синий', 'Зеленный', 'Белый', 'Красный']
        if color in colors:
            return color
        else:
            return 'Цвет такой не найден'
    def get_car_name(self):
       return self.car_name

class Logger():
    def log(self,distance,fuel_amount):
        with open('logs.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{distance} - {fuel_amount} \n')


class SportCar(Car):

    def __init__(self,fuel,logger):
        self.current_mileage = 0
        self.logger = logger
        self.fuel_amount = fuel
        self.car_name = 'Мерседес'


    def fast_drive(self,distance,fuel_consumption = 12):
        score = (distance / 100) * fuel_consumption
        if self.fuel_amount >= score:
            self.fuel_amount -= score
            self.current_mileage += distance
            self.logger.log(distance, self.fuel_amount)
            return f'Вы проехали {sport_car.sport_car_name()}-{distance} км, осталось топливо {self.fuel_amount} литра'
        else:
            return ('Не достаточно топливо')

    def sport_car_name(self):
        sport_car = 'Мерседес'
        return sport_car

    def competition(self):
        win = [cars.get_car_name(), self.get_car_name()]
        random_car = random.choice(win)
        return random_car

logger = Logger()
cars = Car(fuel=40, logger=logger)
sport_car = SportCar(fuel=40, logger=logger)
print(cars.drive(distance= 60))
print(f'Пробег "{cars.get_colors("Желтый")}",{cars.get_mileage()} км')
print(sport_car.fast_drive(distance=65))
print(sport_car.fast_drive(distance=65))
print(sport_car.fast_drive(distance=65))
print(sport_car.fast_drive(distance=65))
print(sport_car.fast_drive(distance=65))
print(sport_car.fast_drive(distance=65))

print(f"Текущий пробег обычной машины,цвет {cars.get_colors('Белый')}: {cars.get_mileage()} км")
print(f"Текущий пробег спортивной машины, цвет {cars.get_colors('Красный')}: {sport_car.get_mileage()} км")
print(f'Выиграла машина {sport_car.competition()}')