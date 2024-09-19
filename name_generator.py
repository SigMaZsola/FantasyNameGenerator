import random
def name_gen():
    print("Welcome to random letter generator!!!\n-----------------------------------")
    name_numbers = int(input("How many words do you want to generate?"))
    letters = "abcdefghijklmnopuqrstwvxyz"
    generated_word = ""
    
    for word in range(name_numbers):
        word_length = random.randrange(1,20)
        for letter in range(word_length):
            generated_word += random.choice(letters)
        
        f = open("ki.txt", "a", encoding="utf-8")
        f.write(f"{generated_word.capitalize()};")
        generated_word = ""
        print("Names were generated!\n-----------------------")
        
