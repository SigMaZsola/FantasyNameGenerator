import importlib

def Sort():
    print("welcome sorting sorting 2000")
    sort_type = int(input("1.-Acending\n2.-Decendig"))

    file = open("ki.txt", "r", encoding=("utf-8"))
    lines = file.readlines()
    file.close()
    data = []
    for line in lines:
        parts = line.strip().split(";")
        for part in parts:
            data.append(part)
    sort = int(input("1.-Bubble\n2.-Stalin"))
    if sort == 1:
        bubbleSort(data)
    else:
        StalinSort(data)
    if sort_type == 1:
        print(data)
    else:
        print(data[::-1])
    module = importlib.import_module("main")
    module.main()

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

def StalinSort(list):
    i = 0
    length = len(list)
    if length > 0:
        aux = list[0]
    while i < length and length > 0:
        if aux <= list[i] :
            aux = list[i]
            i = i+1
        else:
            del list[i]
            length = length -1
             
             