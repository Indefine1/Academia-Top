class Car():
    def __init__(self,fuel,logger):
        self.fuel_amount = fuel
        self.current_mileage = 0
        self.logger = logger

    def drive(self,distance,fuel_consumption = 7.5):

        score = (distance / 100) * fuel_consumption
        if self.fuel_amount >= score:
            self.fuel_amount -= score
            self.current_mileage += distance
            self.logger.log(distance, self.fuel_amount)
            return f'Вы проехали {distance} км, осталось топливо {self.fuel_amount} литра'
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

class Logger():
    def log(self,distance,fuel_amount):
        with open('logs.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{distance} - {fuel_amount}\n')


logger = Logger()
cars = Car(fuel=40, logger=logger)

print(cars.drive(distance= 60))
print(f'Пробег "{cars.get_colors("Желтый")}",{cars.get_mileage()} км')