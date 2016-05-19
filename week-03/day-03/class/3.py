# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate(object):
    def __init__(self, rum_num = 0):
        self.rum_num = rum_num


    def drink_rum(self):
        self.rum_num += 1

    def hows_goin_mate(self):
        if self.rum_num > 4:
            return "Arrrr!"
        else:
            return "Nothin'"

pirate1 = Pirate(5)
pirate1.drink_rum()
pirate1.drink_rum()
print(pirate1.rum_num)
print(pirate1.hows_goin_mate())
