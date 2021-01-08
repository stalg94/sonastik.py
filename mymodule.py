import random
import os
import time
import playsound
from gtts import gTTS

def loe_fail(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    print(mas)
    return mas

def kirjuta_fail(f,rida):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(rida+'\n')
    fail.close()
    return


def tõlkimine(s1,s2,s3,s4):
    text=input("text:")
    if text in s1:
        print(f"{text}-{s2[s1.index(text)]}")
        a=int(input("перевод правильный? => да 1/ нет 2 "))
        if a==2:
            b=input("введи реальный перевод слова => ")
            f=open(s4,'r',encoding="utf-8-sig")
            data=f.read()
            data=data.replace(s2[s1.index(text)],b)
            f.close()
            f=open(s4, 'wt', encoding="utf-8-sig")
            f.write(data)
            f.close()
            s2.pop(s1.index(text))
            s2.insert(s1.index(text),b)
            print(f"{text}-{s2[s1.index(text)]}")
            return
        else:
            return

    elif text in s2:
        print(f"{text}-{s1[s2.index(text)]}")
        a=int(input("перевод правильный? => да 1/ нет 2 "))
        if a==2:
            b=input("введи реальный перевод слова => ")
            f=open(s3,'r',encoding="utf-8-sig")
            data=f.read()
            data=data.replace(s1[s2.index(text)],b)
            f.close()
            f=open(s3, 'wt', encoding="utf-8-sig")
            f.write(data)
            f.close()
            s1.pop(s2.index(text))
            s1.insert(s2.index(text),b)
            print(f"{text}-{s1[s2.index(text)]}")
            return
        else:
            return
    else:
        print(f"{text} puudub")
        return

def kontrol(s1,s2):
    w=len(s1)
    q=int(input("выбери язык => рус 1 / англ 2 => "))
    if q==1:
        a=0.0
        while type(a) != int:
            try:
                a=int(input("введи сколько попыток хочешь => "))
            except:
                TypeError
                print("введи правильно!")
            if a <= w:
                k=0
                for i in range (0,a):
                    s=random.randrange(1,a+1)
                    v=s1[s]
                    p=input(f"напиши перевод слова {v} => ")
                    o=s2[s1.index(v)]
                    if p==o:
                        print("правильно!")
                        k+=1
                    else:
                        print(f"к сожалению, ответ будет => {o}")
                    s+=1
                    i+=1
                tulemus=(k/a)*100
                print(f"ваше результат => {tulemus}%")
                return                  
            else:
                print("введи меньше!")
    if q==2:
        a=0.0
        while type(a) != int:
            try:
                a=int(input("введи сколько попыток хочешь => "))
            except:
                TypeError
                print("введи правильно!")
            if a <= w:
                k=0
                for i in range (0,a):
                    s=random.randrange(1,a+1)
                    v=s2[s]
                    p=input(f"напиши перевод слова {v} => ")
                    o=s1[s2.index(v)]
                    if p==o:
                        print("правильно!")
                        k+=1
                    else:
                        print(f"к сожалению, ответ будет => {o}")
                    s+=1
                    i+=1
                tulemus=(k/a)*100
                print(f"ваше результат => {tulemus}%")
                return                  
            else:
                print("введи меньше!") 
    return

def speak(s1,s2):
    text=input("tekst:")
    if text in s1:
        print(f"{text}-{s2[s1.index(text)]}")
        tts1 = gTTS(text=text, lang ="ru")
        tts2 = gTTS(text=s2[s1.index(text)],lang="en")
        tts1.save("voice1.mp3")
        tts2.save("voice2.mp3")
        os.system("start voice1.mp3")
        time.sleep(2)
        os.system("start voice2.mp3")

        
    elif text in s2:
        print(f"{text}-{s1[s2.index(text)]}")
        tts1 = gTTS(text=text,lang="en")
        tts2 = gTTS(text=s1[s2.index(text)],lang="ru")
        tts1.save("voice1.mp3")
        tts2.save("voice2.mp3")
        os.system("start voice1.mp3")
        time.sleep(2)
        os.system("start voice2.mp3")
        
    else:
        print(f"слово {text} отсутвует")
        return
