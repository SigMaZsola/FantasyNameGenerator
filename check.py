def Check():

    value = False

    file = open("ki.txt", "r", encoding=("utf-8"))
    lines = file.readlines()
    file.close()

    data = []

    for line in lines:
        parts = line.strip().split(";")
        for part in parts:
            data.append(part)
    for d in data:
        try:
            if d == int(d):
                value = True
        except:
            if d == str(d):
                value = False
    if value:
        print("The datas are numbers")
    else:
        print("The datas are texts")
Check()