from typing import List

class Driver():
    num_drivers = 0

    def __init__(self, name, age, ranking) -> None:
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.num_drivers += 1

    def get_ranking(self):
        return self.ranking

class Race:
    def __init__(self, name: str, driver_limit: int, drivers: List[Driver]) -> None:
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = drivers
        print(f'Race Info:\n\tRace Name: {self.name}\n\tDriver Limit: {self.driver_limit}\n\tDrivers: {len(self.drivers)}')

    def add_driver(self, driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)

    def get_average_ranking(self):
        total_rank = 0
        for d in self.drivers:
            total_rank += d.ranking

        return total_rank / len(self.drivers)
    
class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def start(self):
        print('Vroom!')

    def talk(self, driver):
        print(f'Hello, {driver.name}, I am {self.name}.')


lewis = Driver("Lewis Hamilton", 36, 83)
eliud = Driver("Eliud Kipchoge", 36, 95)
sebastian = Driver("Sebastian Vettel", 34, 76)
ayrton = Driver("Ayrton Senna", 34, 99)

race = Race("Daytona 500", 5, [
    lewis, eliud, sebastian, ayrton
])
print(race.get_average_ranking())
