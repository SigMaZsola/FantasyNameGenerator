def Number_Check():


    file = open("ki.txt", "r", encoding=("utf-8"))
    lines = file.readlines()
    file.close()

    numbers = []

    for line in lines:
        parts = line.strip().split(";")
        for part in parts:
            number = part
            numbers.append(number)
    numbers = numbers[slice(-1)]

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
    
    checked_numbers = []

    for num in numbers:
        if int(num) >= min_num and int(num) <= max_num:
            checked_numbers.append(num)
    print(checked_numbers)
Number_Check()