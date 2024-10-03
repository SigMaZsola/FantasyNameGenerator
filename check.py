import importlib

def Num(numbers):
    isAllNums = False
    for number in numbers:
        try:
            number = int(number)
            if number == int(number):
                isAllNums = True
        except:
            print("There are strings between the intigers!")
            module = importlib.import_module("main")
            module.main()
            isAllNums = False
            break
    if isAllNums:
        print("The datas are numbers")
        module = importlib.import_module("main")
        module.main()

def Txt(texts):
    isAllTexts = False
    for text in texts:
        try:
            text = int(text)
            if text == int(text):
                print("There are intigers between the strings!")
                module = importlib.import_module("main")
                module.main()
                isAllTexts = False
                break
        except:
            isAllTexts = True
    if isAllTexts:
        print("The datas are texts")
        module = importlib.import_module("main")
        module.main()
def Check():

    file = open("ki.txt", "r", encoding=("utf-8"))
    lines = file.readlines()
    file.close()

    data = []

    for line in lines:
        parts = line.strip().split(";")
        for part in parts:
            data.append(part)
        try:
            data[0] = int(data[0])
            if data[0] == int(data[0]):
                Num(data)
        except:
            if data[0] == str(data[0]):
                Txt(data)
