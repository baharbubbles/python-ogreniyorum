#if kullanımı
sayı = int(input("Bir sayı giriniz: "))
if sayı > 10:
    print("Girdiğiniz sayı 10'dan büyüktür!")

if sayı < 10:
    print("Girdiğiniz sayı 10'dan küçüktür!")

if sayı == 10:
    print("Girdiğiniz sayı 10'dur!")
#-----------------------------------------------------------------------

#'elif' kullanımı
a = int(input("Bir sayı giriniz: "))
if a < 100:
    print("verdiğiniz sayı 100'den küçüktür.")
elif a < 50:
    print("verdiğiniz sayı 50'den küçüktür.")
elif a == 100:
    print("verdiğiniz sayı 100'dür.")
elif a > 100:
    print("verdiğiniz sayı 100'den büyüktür.")
elif a > 150:
    print("verdiğiniz sayı 150'den büyüktür.")
#burada 'elif' yerine 'if' de kullanabilirdik
# ancak o zaman doğru olan tüm sonuçları çıktı alırdık

# 'elif'te de doğru olan birden çok durumda ilk doğruyu çıktı olarak alıyoruz   
#--------------------------------------------------------------------------

#'else' kullanımı
boy = int(input("boyunuz kaç cm?"))
if boy < 170:
    print("boyunuz kısa")
elif boy < 180:
    print("boyunuz normal")
else:
    print("boyunuz uzun")
#else bloğundan önce art arda gelen if blokları varsa, else deyimi yalnızca kendisinden önceki
#son if bloğunu dikkate alır 

#eğer programınızda bir else bloğuna yer verecekseniz, ondan önce gelen koşullu
#durumların ilkini if ile sonrakileri ise elif ile bağlayın