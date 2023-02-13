isim = "Bahar"
yas = 21
print(f"Adı {isim} ve o {yas} yaşında.")

# format() fonksiyonu ile arasındaki farkı görmek için:
isim = "Irmak"
yas = 22
print("Adı {} ve o {} yaşında.".format(isim,yas))

# Sadece toplama işlemi yapan bir hesap makinesi yapalım f-stringle
bir_sayi = int(input("Birinci sayıyı girin: "))
iki_sayi = int(input("İkinci sayıyı girin: "))
print(f"Sayıların toplamı {bir_sayi+iki_sayi} eder.")

# Listeler 
# Bir liste elde etmek için, öğeleri birbirinden virgülle ayırıp, bunların hepsini köşeli parantezler içine alıyoruz.
# Farklı öğeleri bir araya getirip bunları köşeli parantezler içine alırsak ‘liste’ adlı veri tipini oluşturmuş oluyoruz.
# Bu listenin öğeleri farklı veri tiplerine ait olabilir.
liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]
for oge in liste:
    print("{} adlı öğenin veri tipi: {}".format(oge, type(oge)))   # listedeki verilerin tip çeşitlerini görmek için

# list() fonksiyonu
# list() fonksiyonu da tıpkı str() , int() ve float() fonksiyonları gibi bir dönüştürme fonksiyonudur.
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
harf_listesi = list(alfabe)
print(harf_listesi)

# list() fonksiyonunun önemli bir görevi de range() fonksiyonunun, sayı aralığını ekrana basmasını sağlamaktır
for i in range(10):   # gibi bir döngü kullanmamak için > print(*range(10)) < gibi alternatif öğrendik
    print(i)
# bu alternatife ek olarak list() fonksiyonunu da kullanabiliriz
print(list(range(10)))  # range türünde bir veriyi list türünde veriye dönüştürüyoruz
# ** bir liste olduğu için yan yana yazdırır ancak for döngüsü alt alta çıktı verir

# Listenin öğelerine erişmek:
# Tıpkı karakter dizilerinde olduğu gibi, listelerde de her öğenin bir sırası vardır

liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]
# liste adlı veri tipi, içinde başka bir liste de barındırabilir
print(liste)

print(liste[2][1]) 
 # iç içe geçmiş listelerin öğelerini almak oldukça basit. Yapmamız gereken tek şey, gömülü listenin önce ana listedeki konumunu, 
 # ardından da almak istediğimiz öğenin gömülü listedeki konumunu belirtmektir

yeni_liste = liste[2] # gömülü listeyi ayrı bir liste olarak alabiliriz
print(yeni_liste)

# Listenin öğelerini değiştirmek:
# Listeler ise değiştirilebilen (mutable) bir veri tipidir. Dolayısıyla listeler üzerinde doğrudan
# değişiklik yapabiliriz. Bir liste üzerinde değişiklik yapabilmek için o listeyi yeniden tanımlamamıza gerek yok
renkler = ["kırmızı", "sarı", "mavi", "yeşil", "beyaz"]
print(renkler)
renkler[0]="siyah"  # 0 indisli kırmızı rengini yeni renkler adlı liste ataması yapmadan var olan listenin üzerinde siyah olarak değiştirdik
print(renkler)

liste = [1, 2, 3]
print(liste)
liste[0:3] = 5, 6, 7 # liste[:] = 5, 6, 7   yazmak da aynı anlama gelir çünkü sıra numarası bir karakter dizisinin ilk öğesine
# karşılık geliyorsa o sıra numarasını belirtmeyebiliriz. Aynı şekilde son öğeye denk geliyorsa son öğeyi belirtmeyebiliriz.
print(liste)

# Listeye öğe eklemek:
liste = [1, 3, 5, 7]
liste + [8]  # köşeli parantez liste demek dikattt!!!
# Python’da + işareti kullanarak bir listeye öğe ekleyecekseniz, eklediğiniz öğenin de liste olması gerekiyor. Mesela bir listeye
# doğrudan karakter dizilerini veya sayıları ekleyemezsiniz.

# Listeleri birleştirmek:
# listelerde de birleştirme işlemleri için + işlecinden yararlanabilirsiniz
# örn: kullanıcı tarafından girilen sayıların ortalaması ile birlikte, hangi sayıların girildiğini de göstermek isteyen bir kod yazalım.
sayilar = 0
notlar = []
for i in range(10):
    veri = int(input("{}. not: ".format(i+1)))
    sayilar += veri
    notlar += [veri]
print("Girilen notlar: ", *notlar)
print("Not ortalamanız: ", sayilar/10)

# Listeden öğe çıkarmak:
# Bir listeden öğe silmek için del adlı ifadeden yararlanabilirsiniz
liste = [1, 2, 3, 4]
del liste[-1]  # 4 sayısı silinir
print(liste)
# tüm listeyi silmek
del liste

# Listeleri kopyalamak:
# Eğer birbirinden kopyalanan listelerin birbirini etkilemesini istemiyorsanız, önünüzde birkaç seçenek var:
# 1.seçenek
liste1 = ["ali", "veli", "ahmet"]
liste2 = liste1[:]  # Burada liste1’i kopyalarken, listeyi baştan sona dilimlediğimize dikkat edin
liste1[0] = "ayşe"
print(liste1)       # liste1’de yaptığımız değişiklik liste2’ye yansımadı.
print(liste2)

# 2.seçenek
liste3 = list(liste1)  # Artık elimizde birbirinin kopyası durumunda iki farklı liste var
liste3[0] = "bahar"
print(liste3)

# 3.seçenek : Bu yöntemi de bir sonraki bölümde liste metotlarını incelerken ele alacağız.

# Liste Üreteçleri (List Comprehensions)
# liste üreteçlerinin görevi liste üretmektir.
liste = [i for i in range(1000)]
# Örneğin 0 ile 1000 arasındaki çift sayıları listelemek için liste üreteçlerini kullanmak,alternatiﬂerine göre daha makul bir tercih olabilir:
liste = [i for i in range(1000) if i % 2 == 0]

liste = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12]]
tümü = [z for i in liste for z in i]
print(tümü)