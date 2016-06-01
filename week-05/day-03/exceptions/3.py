# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person(object):

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

        if birth_date <= 0 or birth_date > 2016:
            raise ValueError('error')


joco = Person('Joco', 1990)
# joco = Person('Joco', 0)
print(joco.name)
print(joco.birth_date)
