import importlib

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
            checked_words.append(num)
    print(checked_words)
    print("Words were checked")
    print("------------------------------")
    module = importlib.import_module("main")
    module.main()
