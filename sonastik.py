from mymodule import*

rus=[]
engl=[]

rus = loe_fail("C:\Users\stalg\Desktop\sõnastik\sonastik1\rus.txt")
engl=loe_fail("engl.txt")
while True:
    v=input("1 - tõlkimine,\n2 - lisamine,\n3 - sõnavara kontroll,\n4 - sõna rääkimine \n=> ")
    if v=="1":
        tõlkimine(rus,engl,"rus.txt","engl.txt")
    elif v=="2":
        text=input("введи новое слово:")
        if text[0] in u"\u039F":
            kirjuta_fail("rus.txt",text)
            a=input("а теперь его перевод => ")
            kirjuta_fail("engl.txt",a)
            print(text," - ",a)
            rus.append(text)
            engl.append(a)
        else:
            kirjuta_fail("engl.txt",text)
            a=input("а теперь его перевод => ")
            kirjuta_fail("rus.txt",a)
            print(text," - ",a)
            engl.append(text)
            rus.append(a)
    elif v=="3":
        proverka(rus,engl)
    elif v=="4":
        speak(rus,engl)


