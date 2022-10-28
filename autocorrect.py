words_list = ["hari", "ini", "saya", "sangat", "bersemangat", "sekali", "dengan", "mata", "kuliah", "Pemrosesan", "bahasa", "alami"]

prompt = input("Tuliskan Text> ")

output = ""
list_1 = []
list_2 = []
char_num = 3
num_string = "Tiga"
corrected = False

if len(prompt) <= 3:
    char_num = 3
    num_string = "Tiga"
elif len(prompt) >= 4:
    char_num = 4
    num_string = "Empat"

for word in words_list:

    if len(prompt) < char_num:
        print(f"Harus memiliki lebih dari {num_string} karakter.")
        break

    if prompt == word:
        print("Yes.")
        break

    elif prompt != word:

        for char in word:
            if len(list_1) < char_num:
                list_1.append(char)

        for char in prompt:
            if len(list_2) < char_num:
                list_2.append(char)
        
        if list_1 == list_2:
            output += word
            corrected = True
            list_1.clear()
            list_2.clear()
            break

        elif list_1 != list_2:
            list_1.clear()
            list_2.clear()

if corrected:
    print(f"{output} -> Sebagian Benar.")