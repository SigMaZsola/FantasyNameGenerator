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

    file = open("ki.txt", "a", encoding="utf-8")

    for i in range(how_many_numbers):
        number = random.randint(min_number, max_number)
        file.write(f"{number};")
        
    file.close()

Number_Generator()