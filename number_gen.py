import random

def Number_Generator():

    good = True

    while good:
        try:
            how_many_numbers = int(input("Please enter how many numbers you want to generate: "))
            good = False
        except: good = True
        try:
            from_where = int(input("Please enter the minimum number: "))
            good = False
        except: good = True
        try:
            to_where = int(input("Please enter the maximum number: "))
            good = False
        except: good = True

    numbers =[]

    for i in range(how_many_numbers):
        number = random.randint(from_where, to_where)
        numbers.append(number)
Number_Generator()