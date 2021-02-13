class NoDriverException(Exception):
    """ Raised when no driver is in vehicle """
    pass


class TooManyPassengersException(Exception):
    """ Raised when there are more passengers than seats in a car """


class Car:
    def __init__(self, n_seats):
        self.passengers = []
        self.speed = 0
        self.n_seats = n_seats

    def add_passenger(self, name):
        if len(self.passengers) == self.n_seats:
            raise TooManyPassengersException("Too many passengers for too few seats")
        self.passengers.append(name)

    def accelerate(self):
        if len(self.passengers) < 1:
            raise NoDriverException("No driver!")
        self.speed += 1

    def brake(self):
        if self.speed > 0:
            self.speed -= 1

    def remove_passenger(self, name):
        self.passengers.remove(name)

    def get_speed(self):
        return self.speed

    def get_passengers(self):
        return self.passengers
