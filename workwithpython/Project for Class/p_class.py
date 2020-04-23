from random import randint


class Human:
    count = 1
    name = [
        'حسین', 'مازیار', 'اکبر', 'نیما', 'مهدی', 'فرهاد'
        , 'محمد', 'خشایار', 'میلاد', 'مصطفی', 'امین', 'سعید'
        , 'پویا', 'پوریا', 'رضا', 'علی', 'بهزاد'
        , 'سهیل', 'بهروز', 'شهروز', 'سامان', 'محسن'
    ]
    n = 22
    dictionary_output = {}

    def __init__(self):
        number = int(randint(1, Human.n))
        self.number = number

    def setplayer(self):
        for value in FootballPlayer.dict_A.values():
            for item in value:
                Human.dictionary_output['A'] = Human.name[item - 1]

        for value in FootballPlayer.dict_A.values():
            for item in value:
                Human.dictionary_output['B'] = Human.name[item - 1]
        print(Human.dictionary_output)


class FootballPlayer(Human):
    A = []
    B = []

    for


while Human.count <= 11:
    FootballPlayer.teama()

while Human.count <= 22:
    FootballPlayer.teamb()

Human.setplayer()
