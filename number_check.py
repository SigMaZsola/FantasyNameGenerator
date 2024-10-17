import importlib

def Number_Check():

    file = open("ki.txt", "r", encoding=("utf-8"))
    lines = file.readlines()
    file.close()

    numbers = []

    for line in lines:
        parts = line.strip().split(";")
        for part in parts:
            numbers.append(part)

    not_usable = True

    while not_usable:
        try:
            min_num = int(input("Please enter the minimum number: "))
            not_usable = False
        except: not_usable = True
        try:
            max_num = int(input("Please enter the maximum number: "))
            not_usable = False
        except: not_usable = True
    
    approved_numbers = []
    declined_numbers = []

    for num in numbers:
        if int(num) >= min_num and int(num) <= max_num:
            approved_numbers.append(num)
        else:
            declined_numbers.append(num)

    print(f"These numbers matched the given range: {approved_numbers}")
    print(f"These numbers didn't matched the given range: {declined_numbers}")

    print("Numbers were checked")
    print("------------------------------")
    module = importlib.import_module("main")
    module.main()
