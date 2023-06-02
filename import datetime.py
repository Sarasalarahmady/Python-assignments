import datetime
import random


month_names = (
    ({"jan": "january"}, 31),
    ({"feb": "february"}, 28),
    ({"mar": "march"}, 31),
    ({"apr": "april"}, 30),
    ({"may": "may"}, 31),
    ({"jun": "june"}, 30),
    ({"jul": "july"}, 31),
    ({"aug": "august"}, 31),
    ({"sep": "september"}, 30),
    ({"oct": "october"}, 31),
    ({"nov": "november"}, 30),
    ({"dec": "december"}, 31),
)


class DateCalc:
    def init(self, y=1972, m=1, d=1):
        """It produces a date of [year, month, day]"""
        self.year = y
        self.month = m
        self.day = d
        DateCalc.normalize(self)

    def add_date(self, oth):
        """This adds two dates correspondingly"""
        d3 = DateCalc()
        d3.day = self.day + oth.day
        d3.month = self.month + oth.month
        d3.year = self.year + oth.year
        DateCalc.normalize(d3)
        return d3

    def sub_date(self, oth):
        """This subtracts two dates correspondingly"""
        d3 = DateCalc()
        d3.day = self.day - oth.day
        d3.month = self.month - oth.month
        d3.year = self.year - oth.year
        DateCalc.normalize(d3)
        return d3

    @staticmethod
    def normalize(d):
        """It normalizes date with type of DateCalc"""
        if isinstance(d.day, int):
            max_days = month_names[d.month - 1][1]
            rem = d.day // max_days
            d.day %= max_days
        else:
            raise TypeError("Invalid date for day")

        d.month += rem
        if isinstance(d.month, int):
            rem = d.month // 12
            d.month %= 12
        else:
            raise TypeError("Invalid date for month")

        d.year += rem
        if d.year < 0:  
            print("Year should be positive")
            d.year = 1

    def display(self, short=True, format_="-"):
        """It shows the given date neatly"""
        d = self.day
        for month in month_names:
            if month_names[self.month - 1] == month:
                if short:
                    m = list(month[0].keys())[0]
                else:
                    m = list(month[0].values())[0]

        y = self.year
        print(f"{y}{format_}{m}{format_}{d}")


d1 = DateCalc(3, d=23)
d2 = DateCalc(m=4, d=10)


d3 = d1.add_date(d2)
d3.display()