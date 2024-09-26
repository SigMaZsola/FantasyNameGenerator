import random

def Number_Generator():

    not_usable = True

    while not_usable:
        try:
            how_many_numbers = int(input("Please enter how many numbers you want to generate: "))
            not_usable = False
        except: not_usable = True
        try:
            min_number = int(input("Please enter the minimum number: "))
            not_usable = False
        except: not_usable = True
        try:
            max_number = int(input("Please enter the maximum number: "))
            not_usable = False
        except: not_usable = True

    numbers = ""

    file = open("ki.txt", "w", encoding="utf-8")

    for i in range(how_many_numbers):
        number = random.randint(min_number, max_number)
        numbers += str(number)
        numbers += ";"

    file.write(numbers[slice(-1)])
        
    file.close()

Number_Generator()