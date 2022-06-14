import random
a=(random.randint(1,10))
hakbilgisi=int(input("Kaç hakkınız olsun:"))
i=0
sayac=0

while i < hakbilgisi:
    hakbilgisi -= 1
    i += 1
    deneme = int(input("Tahmin:"))
    sayac += 1


    if deneme==a:
        print(f"Doğru!{sayac}.denemede bildiniz")
        break
    elif deneme > a:
        print(f"Azalt! {hakbilgisi} hakkın kaldı")
    elif deneme < a:
        print(f"Arttır! {hakbilgisi} hakkın kaldı")

    if hakbilgisi == 0:
        print("Hakkınız bitti")
