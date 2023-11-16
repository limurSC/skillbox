from abc import ABC


class Transport(ABC):
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        return f"Coordinates: {self.__coordinates}, Speed: {self.__speed}, Brand: {self.__brand}, Year: {self.__year}, Number: {self.__number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x < self.__coordinates[0] < pos_x + length and pos_y < self.__coordinates[0] < pos_y + width

    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def speed(self):
        return self.__speed

    @property
    def brand(self):
        return self.__brand

    @property
    def year(self):
        return self.__year

    @property
    def number(self):
        return self.__number

    @coordinates.setter
    def coordinates(self, coordinates):
        if not isinstance(coordinates, tuple) or len(coordinates) != 2:
            print("Недопустимый формат coordinates")
        elif not 0 < coordinates[0] < 1000:
            print("Недопустимое значение pos_x")
        elif not 0 < coordinates[1] < 1000:
            print("Недопустимое значение pos_y")
        else:
            self.__coordinates = coordinates

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            print("Недопустимый формат speed")
        elif not 0 < speed < 1000:
            print("Недопустимое значение speed")
        else:
            self.__speed = speed

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            print("Недопустимое формат brand")
        else:
            self.__brand = brand

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            print("Недопустимый формат year")
        elif not 0 < year < 2024:
            print("Недопустимое значение year")
        else:
            self.__year = year

    @number.setter
    def number(self, number):
        if not isinstance(number, str):
            print("Недопустимый формат number")
        else:
            self.__number = number


class Passenger(ABC):
    def __init__(self, passengers_capacity, number_of_passengers):
        self.__passengers_capacity = passengers_capacity
        self.__number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int):
            print("Недопустимый формат passengers_capacity")
        elif 0 > passengers_capacity:
            print("Недопустимое значение passengers_capacity")
        else:
            self.__passengers_capacity = passengers_capacity

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int):
            print("Недопустимый формат number_of_passengers")
        elif not 0 < number_of_passengers < 1000:
            print("Недопустимое значение number_of_passengers")
        elif number_of_passengers < self.passengers_capacity:
            print("Недопустимое значение passengers_capacity")
        else:
            self.__number_of_passengers = number_of_passengers


class Cargo(ABC):
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, int):
            print("Недопустимый формат number_of_passengers")
        elif not 0 < carrying < 1000:
            print("Недопустимый значение number_of_passengers")
        else:
            self.__carrying = carrying


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.__port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if isinstance(port, str):
            print("Недопустимый формат number_of_passengers")
        else:
            self.__port = port


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int):
            print("Недопустимый формат passengers_capacity")
        elif not 0 < passengers_capacity < 350:
            print("Недопустимое значение passengers_capacity")
        else:
            self.__passengers_capacity = passengers_capacity

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int):
            print("Недопустимый формат number_of_passengers")
        elif number_of_passengers < self.passengers_capacity:
            print("Недопустимое значение passengers_capacity")
        else:
            self.__number_of_passengers = number_of_passengers


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, int):
            print("Недопустимый формат number_of_passengers")
        elif 0 < carrying < 1500:
            print("Недопустимый значение number_of_passengers")
        else:
            self.__carrying = carrying


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        self.height = height
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            print("Недопустимый формат height")
        elif not 0 < height < 10000:
            print("Недопустимый значение height")
        else:
            self.__height = height


class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)


x = Seaplane((1, 1), -100, "asd", 1999, "a123", -5, "asd")