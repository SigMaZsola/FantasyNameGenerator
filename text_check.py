import importlib

approved = False

def text_check():

    file = open("ki.txt", "r", encoding=("utf-8"))
    lines = file.readlines()
    file.close()

    words = []

    for line in lines:
        parts = line.strip().split(";")
        for part in parts:
            words.append(part)

    not_usable = True

    while not_usable:
        try:
            pieces = int(input("Please enter how many words were generated: "))
            not_usable = False
        except: not_usable = True
    
    checked_words = []

    for num in words:
        if pieces == len(words):
            aproved = True
        else:
            approved = False
    if aproved:
        print("The texts did match with the given parameter.")
    else:
        print("The texts did not match with the given parameter.")
    print("Words were checked")
    print("------------------------------")
    module = importlib.import_module("main")
    module.main()
