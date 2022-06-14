#k bölümüne integer değer girin

k = 
mesaj = "Şifrelenicek Mesaj"
alfabe = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZqwxQWX1234567890.@+-/"

boyut = len(alfabe)

sifrelimesaj = ""
for i in mesaj:
    for c in alfabe:
        if i == c:
            konum = alfabe.index(c)
            konum += k
            sifrelimesaj += alfabe[konum % boyut]


print(sifrelimesaj)