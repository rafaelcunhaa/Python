class WeekDayError(Exception):
    pass
	

class Weeker:
    diasemana = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.diasemana:
            raise WeekDayError
        self.__selsem = day

    def __str__(self):
        return self.__selsem

    def add_days(self, n):
        dia = self.diasemana.index(self.__selsem)
        dia = (dia + n) % 7
        self.__selsem = self.diasemana[dia]

    def subtract_days(self, n):
        dia = self.diasemana.index(self.__selsem)
        dia = (dia - n) % 7
        self.__selsem = self.diasemana[dia]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    