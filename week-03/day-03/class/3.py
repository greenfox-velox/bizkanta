# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate(object):
    def __init__(self):
        self.rum_num = 0

    def drink_rum(self):
        self.rum_num += 1

    def hows_goin_mate(self):
        if self.rum_num > 4:
            return "Arrrr!"
        else:
            return "Nothin'"

pirate1 = Pirate()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()

print(pirate1.rum_num) #5
print(pirate1.hows_goin_mate()) #"Arrrr!"
