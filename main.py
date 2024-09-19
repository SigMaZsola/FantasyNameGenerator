from name_generator import name_gen
from number_gen import Number_Generator

def main():
    #Változók felvétele
    is_number_generated = False
    is_name_generated = False
    type = False
    selected = int(0)
    #Köszöntő szöveg
    print("Welcome to Generator 2000!!!\n--------------------------------\n")
    while type == False:
    #Kivételek lekezelése
        try:
            selected = int(input("1.-Number generator\n2.-Name generator\n3.-Check numbers\n4.-Check names\n"))
            type = True
        except:
            type = False
        
        if selected == 1:
            Number_Generator()
        if selected == 2:
            name_gen()

        if selected == 3 or selected == 4:
            if is_number_generated == False or is_name_generated == False:
                print("Data not yet generated")
                type = False
main()

