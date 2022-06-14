#Bankamatik Uygulaması
bakiye=10000
#Fonksiyonlar
########################################    Para çekme     #######################################
def paraçekme(miktar):
    if miktar<=bakiye:
        print("Kalan paranız",bakiye-miktar,"TL")
        baskaislem=input("Başka bir işlem yapmak istermisiniz e/h")

        if baskaislem=="e":
            secenek = int(input("*-----MENÜ-----*\n"
                                "💰Para Çekmek için=1💰\n"
                                "💰Para Yatırmak için=2💰\n"
                                "💰Bakiye Sorgulamak için=3💰\n"
                               "Seçiniz..."))
            if secenek == 1:
                miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                paraçekme(miktar)

            elif secenek == 2:
                yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                parayatırma(yatirilacakmiktar)

            elif secenek == 3:
                print("Bakiyeniz: ", bakiye)
        elif baskaislem=="h":
            print("Tekrar Bekleriz 😀😀😀")
    else:
        menüdönüs=int(input("Bakiyeniz yeterli değil\n"
        "Menüye dönmek için=0\n"
        "Çıkış yapmak için=1"))

        if menüdönüs==0:
            secenek = int(input(
                "*-----MENÜ-----*\n"
                "💰Para Çekmek için=1💰\n"
                "💰Para Yatırmak için=2💰\n"
                "💰Bakiye Sorgulamak için=3💰\n"
                "Seçiniz..."
            ))
            if secenek == 1:
                miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                paraçekme(miktar)



            elif secenek == 2:
                yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                parayatırma(yatirilacakmiktar)



            elif secenek == 3:
                print("Bakiyeniz: ", bakiye)
        elif menüdönüs==1:
            print("Tekrar Bekleriz 😀😀😀")


    return
######################################          Para yatırma            ###############################################

def parayatırma(yatirilacakmiktar):
    ybakiye = bakiye+yatirilacakmiktar
    print("Bakiyeniz ", ybakiye, " TL'dir")
    baskaislem = input("Başka bir işlem yapmak istermisiniz e/h")
    if baskaislem == "e":
        secenek = int(input("*-----MENÜ-----*\n"
                            "💰Para Çekmek için=1💰\n"
                            "💰Para Yatırmak için=2💰\n"
                            "💰Bakiye Sorgulamak için=3💰\n"
                            "Seçiniz..."))
        if secenek == 1:
            miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
            paraçekme(miktar)

        elif secenek == 2:
            yatirilacakmiktar=int(input("💰Yatırmak istediğiniz miktarı girin💰"))
            parayatırma(yatirilacakmiktar)

        elif secenek == 3:
            print("Bakiyeniz: ",bakiye)
    elif baskaislem == "h":
        print("Tekrar Bekleriz 😀😀😀")
        return

#########################################  Hesap tekrarı 1   #################################################
print("*--------------------------------------ARİF BANK--------------------------------------------*")
hesapno = int(input("🔒Lütfendokuz haneli hesap numarasını girin🔒"))
##################################################   Şifre tekrarı 1  ###########################################
if hesapno == 123456789:
    sifre = int(input("🔒Lütfen şifrenizi girin🔒"))


    if sifre == 8588:
        secenek = int(input(
            "*-----MENÜ-----*\n"
            "💰Para Çekmek için=1💰\n"
            "💰Para Yatırmak için=2💰\n"
            "💰Bakiye Sorgulamak için=3💰\n"
            "Seçiniz..."
        ))
        if secenek == 1:
            miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
            paraçekme(miktar)



        elif secenek == 2:
            yatirilacakmiktar=int(input("💰Yatırmak istediğiniz miktarı girin💰"))
            parayatırma(yatirilacakmiktar)



        elif secenek == 3:
            print("Bakiyeniz: ",bakiye)
 ################################################## Şifre tekrarı 2 ########################################
    else:
        sifretekrarı = int(input("Tekrar Deneyiniz"))
        if sifretekrarı == 8588:
            secenek = int(input(
                "*-----MENÜ-----*\n"
                "💰Para Çekmek için=1💰\n"
                "💰Para Yatırmak için=2💰\n"
                "💰Bakiye Sorgulamak için=3💰\n"
                "Seçiniz..."
            ))
            if secenek == 1:
                miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                paraçekme(miktar)

            elif secenek == 2:
                yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                parayatırma(yatirilacakmiktar)

            elif secenek == 3:
                print("Bakiyeniz: ", bakiye)
        ########################################################   Şifre tekrarı 3 #########################################
        else:
            sifretekrarı = int(input("Tekrar Deneyiniz"))
            if sifretekrarı == 8588:
                secenek = int(input(
                    "*-----MENÜ-----*\n"
                    "💰Para Çekmek için=1💰\n"
                    "💰Para Yatırmak için=2💰\n"
                    "💰Bakiye Sorgulamak için=3💰\n"
                    "Seçiniz..."
                ))
                if secenek == 1:
                    miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                    paraçekme(miktar)

                elif secenek == 2:
                    yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                    parayatırma(yatirilacakmiktar)

                elif secenek == 3:
                    print("Bakiyeniz: ", bakiye)
            else:
                print("Yetkisiz kullanımdan hesabınız bloklandı:")

    #######################################    Hesap tekrarı 2 ############################################3

else:
    hesaptekrarı = int(input("Üzgünüz böyle bir hesap yok tekrar deneyin"))
    if hesaptekrarı == 123456789:
        sifre = int(input("🔒Lütfen şifrenizi girin🔒"))
        if sifre == 8588:
            secenek = int(input(
                "*-----MENÜ-----*\n"
                "💰Para Çekmek için=1💰\n"
                "💰Para Yatırmak için=2💰\n"
                "💰Bakiye Sorgulamak için=3💰\n"
                "Seçiniz..."
            ))
            if secenek == 1:
                miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                paraçekme(miktar)

            elif secenek == 2:
                yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                parayatırma(yatirilacakmiktar)

            elif secenek == 3:
                print("Bakiyeniz: ", bakiye)
        else:
            sifretekrarı = int(input("Tekrar Deneyiniz"))
            if sifretekrarı == 8588:
                secenek = int(input(
                    "*-----MENÜ-----*\n"
                    "💰Para Çekmek için=1💰\n"
                    "💰Para Yatırmak için=2💰\n"
                    "💰Bakiye Sorgulamak için=3💰\n"
                    "Seçiniz..."
                ))
                if secenek == 1:
                    miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                    paraçekme(miktar)

                elif secenek == 2:
                    yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                    parayatırma(yatirilacakmiktar)

                elif secenek == 3:
                    print("Bakiyeniz: ", bakiye)
            else:
                sifretekrarı = int(input("Tekrar Deneyiniz"))
                if sifretekrarı == 8588:
                    secenek = int(input(
                        "*-----MENÜ-----*\n"
                        "💰Para Çekmek için=1💰\n"
                        "💰Para Yatırmak için=2💰\n"
                        "💰Bakiye Sorgulamak için=3💰\n"
                        "Seçiniz..."
                    ))
                    if secenek == 1:
                        miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                        paraçekme(miktar)

                    elif secenek == 2:
                        yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                        parayatırma(yatirilacakmiktar)

                    elif secenek == 3:
                        print("Bakiyeniz: ", bakiye)
                else:
                    print("Yetkisiz kullanımdan hesabınız bloklandı:")

    #########################################     Hesap tekrarı 3 ############################################

    else:
        hesaptekrarı = int(input("Üzgünüz böyle bir hesap yok tekrar deneyin"))
        if hesaptekrarı == 123456789:
            sifre = int(input("🔒Lütfen şifrenizi girin🔒"))
            if sifre == 8588:
                secenek = int(input(
                    "*-----MENÜ-----*\n"
                    "💰Para Çekmek için=1💰\n"
                    "💰Para Yatırmak için=2💰\n"
                    "💰Bakiye Sorgulamak için=3💰\n"
                    "Seçiniz..."
                ))
                if secenek == 1:
                    miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                    paraçekme(miktar)

                elif secenek == 2:
                    yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                    parayatırma(yatirilacakmiktar)

                elif secenek == 3:
                    print("Bakiyeniz: ", bakiye)
            else:
                sifretekrarı = int(input("Tekrar Deneyiniz"))
                if sifretekrarı == 8588:
                    secenek = int(input(
                        "*-----MENÜ-----*\n"
                        "💰Para Çekmek için=1💰\n"
                        "💰Para Yatırmak için=2💰\n"
                        "💰Bakiye Sorgulamak için=3💰\n"
                        "Seçiniz..."
                    ))
                    if secenek == 1:
                        miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                        paraçekme(miktar)

                    elif secenek == 2:
                        yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                        parayatırma(yatirilacakmiktar)

                    elif secenek == 3:
                        print("Bakiyeniz: ", bakiye)
                else:
                    sifretekrarı = int(input("Tekrar Deneyiniz"))
                    if sifretekrarı == 8588:
                        secenek = int(input(
                            "*-----MENÜ-----*\n"
                            "💰Para Çekmek için=1💰\n"
                            "💰Para Yatırmak için=2💰\n"
                            "💰Bakiye Sorgulamak için=3💰\n"
                            "Seçiniz..."
                        ))
                        if secenek == 1:
                            miktar = int(input("💰Çekmek istediğiniz miktarı girin💰"))
                            paraçekme(miktar)

                        elif secenek == 2:
                            yatirilacakmiktar = int(input("💰Yatırmak istediğiniz miktarı girin💰"))
                            parayatırma(yatirilacakmiktar)

                        elif secenek == 3:
                            print("Bakiyeniz: ", bakiye)
                    else:
                        print("Yetkisiz kullanımdan hesabınız bloklandı:")
        else:
            print("Başka zaman deneyin")








