import datetime


class Date():
    def __init__(self, m):
        self.birthday = datetime.datetime.strptime(m, '%Y/%m/%d')

    def calcu_age(self):
        today = datetime.datetime.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def calculate_age(self):
        today = datetime.datetime.today()

        try:
            birthday = self.birthday.replace(year=today.year)

            # raised when birth date is February 29
            # and the current year is not a leap year
        except ValueError:
            birthday = self.birthday.replace(year=today.year,
                                             month=self.birthday.month + 1, day=1)
        if birthday > today:
            return today.year - self.birthday.year - 1
        else:
            return today.year - self.birthday.year


my_date = input()
check_date = my_date.strip().split('/')
if int(check_date[1]) < 12 and int(check_date[2]) < 32:
    my = Date(my_date)
    print(my.calculate_age())

else:
    print('WRONG')
