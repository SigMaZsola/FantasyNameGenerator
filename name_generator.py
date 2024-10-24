import random
import importlib
def text_gen():
    print("Welcome to random letter generator!!!\n-----------------------------------")
    print("1-Random 20 letters\n2-Fantasy name generator")
    choice = int(input("What do you want to generate?"))

    if choice == 1:
        name_gen()
    elif choice == 2:
        sex = int(input("1-Male\n2-Female"))
        fate = int(input("1-Good\n2-Evil"))
        fantasy(sex, fate)

def name_gen():
    rnd = ""
    letters = "abcdefghijklmnopuqrstwvxyz"
    word_numbers = int(input("How many words do you want to generate?"))
    generated_word = ""
    for word in range(word_numbers):
        word_length = random.randrange(1,20)
        for letter in range(word_length):
            generated_word += random.choice(letters)
        rnd += generated_word.capitalize() +";"
        generated_word = ""
    f = open("ki.txt", "w", encoding="utf-8")
    
    f.write(rnd[:-1])
    f.close()
    print("Letters were generated!\n-----------------------")
    backToMenu()

def fantasy(sex, fate):
    good_msh = "vdfhlnpt"
    bad_msh = "bgmvwprfk"
    man = "gbmwpkeéiíauo"
    woman = "lsnvauoéiíú"
    good_mgh = "eéiíú"
    bad_mgh = "auo"
    generated_name = ""
    
    for i in range(10):
        name_length = random.randint(6,20)
        while(len(generated_name) < name_length//2):
            rgs = random.choice(good_msh)
            rgh = random.choice(good_mgh)
            rbs = random.choice(bad_msh)
            rbh = random.choice(bad_mgh)
            if sex == 1:
                if rgh in woman or rgs in woman or rbh in woman or rbs in woman:
                    if fate == 1:
                        generated_name += random.choice(good_mgh) + random.choice(good_msh)
                    elif fate == 2:
                        generated_name += random.choice(bad_mgh) + random.choice(bad_msh)
            elif sex == 2:
                if rgh in man or rgs in man or rbh in man or rbs in man:
                    if fate == 1:
                        generated_name += random.choice(good_mgh) + random.choice(good_msh)
                    elif fate == 2:
                        generated_name += random.choice(bad_mgh) + random.choice(bad_msh)
        backwards = random.randint(0,2)
        if backwards == 0:
            print(generated_name.capitalize())
        else:
            print(generated_name[::-1].capitalize())
        generated_name = ""
    print("Names were generated!\n-----------------------")
    backToMenu()

def backToMenu():
    module = importlib.import_module("main")
    module.main()


