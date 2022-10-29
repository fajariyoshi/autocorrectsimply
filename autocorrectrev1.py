words_list = ["hari", "ini", "saya", "sangat", "bersemangat", "sekali", "dengan", "mata", "kuliah", "Pemrosesan", "bahasa", "alami"] #wordlist / citra bahasa

prompt = input("Tuliskan Text > ")                                                                                                    #penginputan text

output = ""                                                                                                                            # print hasil
list_1 = []                                                                                                                             #list kolom 1
list_2 = []                                                                                                                             #list kolom 2
char_num = 2                                                                                                                            # karatker minimal
num_string = "Dua"                                                                                                                      # string karakter
corrected = False                                                                                                                       # koreksi = salah
uncorrected = True

if len(prompt) <= 2:                                                                                                                    # jika karakter kurang dari 2
    char_num = 2                                                                                            
    num_string = "Dua"
elif len(prompt) >= 4:                                                                                                                  # jika panjang karakter 4
    char_num = 4
    num_string = "Empat"

for word in words_list:                                                                                                                 #pengambilan wordlist

    if len(prompt) < char_num:
        print(f"Harus memiliki lebih dari {num_string} karakter.")
        break
    

    if prompt == word:                                                                                                                  # hasil jika sesuai dari wordlist
        print(f"{word} <- adalah Benar-benar bahasa Alami!.")
        break
    

    elif prompt != word:                                                                                                                # hasil jika tidak sesuai / salah dari wordlist
        
        for char in word:
            if len(list_1) < char_num:
                list_1.append(char)

        for char in prompt:
            if len(list_2) < char_num:
                list_2.append(char)
        
        if list_1 == list_2:
            output += word
            corrected = True
            uncorrected = False
            list_1.clear()
            list_2.clear()
            break
            
        elif list_1 != list_2:
            list_1.clear()
            list_2.clear()
            
        

if corrected:                                                                                                                           #terkoreksi benar dari wordlist
    print(f"{output} -> Mungkin yang anda maksud.")             #jika data ditemukan
    
if uncorrected:
    print("Data tidak ditemukan")                               #jika data tidak ditemukan print