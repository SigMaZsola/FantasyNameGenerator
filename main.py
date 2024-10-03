from name_generator import name_gen
from number_gen import Number_Generator
from number_check import Number_Check
from text_check import text_check

def main():
    #Változók felvétele
    is_number_generated = False
    is_name_generated = False
    type = False
    selected = 0
    #Köszöntő szöveg
    print("Welcome to Generator 2000!!!\n--------------------------------\n")
    while type == False:
    #Kivételek lekezelése
        try: 
            selected = int(input("1.-Number generator\n2.-Name generator\n3.-Check numbers\n4.-Check names\n5.-EXIT\n"))
            if selected <5:
                type = True
        except:
            type = False
        
        if selected == 1:
            Number_Generator()
        if selected == 2:
            name_gen()
        if selected == 3:
            Number_Check()
        if selected == 4:
            text_check()
        if selected == 5:
            break
if __name__ == main():
    main()

