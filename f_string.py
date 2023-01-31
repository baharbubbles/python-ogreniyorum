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
