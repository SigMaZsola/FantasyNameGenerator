from sorting import Sort
def New_data():
    def Data_type(dType):
        try:
            if int(dType) == int(dType):
                return "Int"
        except:
            return "Str"
        
    def New_text():
        word = input("Type the word you want to add: ")
        if Data_type(word) == "Str":
            word_file = open("ki.txt", "a", encoding="utf-8")
            word_file.write(f";{word}")
            word_file.close()
            Sort()
        else:
            print("It wasn't a word!")
            New_text()

    def New_number():
        number = input("Type the number you want to add: ")
        if Data_type(number) == "Int":
            number_file = open("ki.txt", "a", encoding="utf-8")
            number_file.write(f";{number}")
            number_file.close()
            Sort()
        else:
            print("It wasn't a number!")
            New_number()

    file = open("ki.txt", "r", encoding="utf-8")
    line = file.readline()
    file.close()

    data = line.strip().split(";")

    type = False
    while type == False:
        try:
            new_data_type = int(input("what type of data would you like to add?\n1.-Number\n2.-Text\n"))
            if new_data_type < 3:
                type = True
        except:
            type = False

        if new_data_type == 2:
            if Data_type(data[0]) == "Str":
                New_text()
            else:
                print("You can't add a text in a file full of numbers!")
                type = False
        if new_data_type == 1:
            if Data_type(data[0]) == "Int":
                New_number()
            else:
                print("You can't add a number in a file full of words!")
                type = False
New_data()