#BlackJAck#
import random
import time
biltoplam = 0
usertoplam = 0
sayac=0
sayec=0
kartlar = [1,2,3,4,5,6,7,8,9,10,11]
bilikincikart = [0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11]
########################################################################################
while sayac<2:
    sayac+=1
    bilsecim = random.choice(kartlar)
    biltoplam += bilsecim
while True:
    if biltoplam<21:
        bilikin = random.choice(bilikincikart)
        biltoplam += bilikin
        if biltoplam<21:
            bilikin = random.choice(kartlar)
            biltoplam += bilikin
        if biltoplam == 21:

            break
    if biltoplam>21:

        break
    if biltoplam==21:

        break
###########################################################
while sayec<2:
    sayec +=1
    usersecim = random.choice(kartlar)
    usertoplam += usersecim
    time.sleep(1)
    print("Kart seçiliyor...")
    time.sleep(1)
    print(f"Elinizdeki kart ------------>{usertoplam}")
    while True:
        giris=input("Kart çekmek ister misin ------------> e/h :")
        if giris == "h":
            if biltoplam>21:
                print("Bilgisayar Battı")
                break
            if biltoplam<21:
                if usertoplam<biltoplam:
                    print(f"Bilgisayar sizi {biltoplam} ile yendi :) ")
                    break
                if usertoplam>biltoplam:
                    print(f"Bilgisayarı {usertoplam} ile yendiniz !!!")
                    break
                if usertoplam>21:
                    print("Batttınız!!!")
        if giris == "e":
            usersecim = random.choice(kartlar)
            usertoplam += usersecim
            time.sleep(1)
            print("Kart seçiliyor...")
            time.sleep(1)
            print(f"Çekilen kart ------------> {usersecim}")
            time.sleep(0.5)
            print(f"Kart toplamınız ------------> {usertoplam}")
            if usertoplam>21:
                print("Battınız!!")
                break
    break







