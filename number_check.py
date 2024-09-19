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
print(numbers)
