# sözlük tanımlama
kelime = {"kitap":"book"}  # tek öğeli. kitap ve book iki ayrı öğe değil
# sözlük veri tipi de içinde farklı veri tiplerini barındıran, ‘kapsayıcı’ bir veri tipidir. Burada sözlüğümüz iki adet 
# karakter dizisinden oluşuyor.
# type(kelime) yaptığımızda <'class' dict> cevabını alırız. yani kelime adlı değişkenin gerçekten bir sözlük(dictionary) olduğunu görüyoruz
kelime = {"kitap":"book",
          "bilgisayar":"computer"} # iki öğeli-> virgül ile ayrılmış. okunaklı olması için bu şekilde yazılması daha iyi



# sözlük öğelerine erişmek
sözlük = {"kitap":"book",
          "bilgisayar":"computer",
          "defter":"notebook",
          "programlama":"programing"}
print(sözlük["kitap"])  # sözlük[sözlük_öğesinin_adı]

# telefon defteri uygulaması:
telefon_defteri = {"ali bak":"0555 355 55 55",
                   "veli gel":"0566 655 66 66",
                   "ayşe git":"0544 544 44 44"}
kisi = input("Aramak istediğiniz kişinin ismini girin: ")
if kisi in telefon_defteri:
    cevap = "{} adlı kişini numarası: {}"
    print(cevap.format(kisi, telefon_defteri[kisi]))
else:
    print("Aradığınız kişi telefon defterinde yok!")



# sözlüklerin yapısı
# *Teknik olarak, iki nokta üst üste işaretinin solundaki karakter dizisine ‘anahtar’ (key), sağındaki karakter dizisine ise ‘değer’ (value) adı verilir
# Sözlükler; anahtar ve değer çiftlerinin birbirleriyle eşleştirildiği bir veri tipidir.Dolayısıyla sözlükler bu anahtar ve değer çiftleri arasında birebir ilişki kurar.
sayi = {"sıfır":0}
liste = {"bahar ırmak":["uşak","mühendis", 21]}
print(liste["bahar ırmak"])

kisiler = {"ahmet yasa":{"memleket":"istanbul",
                         "meslek":"öğretmen",
                         "yaş":45},
           "fatih kuru":{"memleket":"bursa",
                         "meslek":"tesisatçı",
                         "yaş":55},
           "gül köse":{"memleket":"izmir",
                       "meslek":"doktor",
                       "yaş": 32}              }
print(kisiler["ahmet yasa"]["meslek"])

# irtibat listesi uygulaması
kisiler = {"ahmet yasa":{"memleket":"istanbul",
                         "meslek":"öğretmen",
                         "yaş":45},
           "fatih kuru":{"memleket":"bursa",
                         "meslek":"tesisatçı",
                         "yaş":55},
           "gül köse":{"memleket":"izmir",
                       "meslek":"doktor",
                       "yaş": 32}              }

isim = "Hakkında ayrıntılı bilgi edinmek istediğiniz kişinin adı: "
arama = input(isim)
ayrinti = input("memleket/meslek/yaş?: ")

print(kisiler[arama][ayrinti])

# **sözlükteki öğeler için 'sıra' diye bir kavram yoktur.          



# sözlüklere öğe eklemek
# Tıpkı listeler gibi, sözlükler de büyüyüp küçülebilen bir veri tipidir. Yani bir sözlüğü ilk kez tanımladıktan sonra istediğimiz 
# zaman bu sözlüğe yeni öğeler ekleyebilir veya varolan öğeleri çıkarabiliriz

kimlik = {}
kimlik["ali"] = "uşak"   # ekleme mantığı = sözlük[anahtar] = değer
print(kimlik["ali"])  # çıktı olarak 'uşak' yazacak
kimlik["meral"] = "ankara"
kimlik["ceren"] = "antalya"
kimlik["aslı"] = "ısparta"
print(kimlik)

# **Bir değerin ‘anahtar’ olabilmesi için, o öğenin değiştirilemeyen (immutable) bir veri tipi olması gerekir : demetler,sayılar,karakter dizileri



# sözlüklerin öğeleri üzerinde değişiklik yapmak
# Sözlükler değiştirilebilir veri tipleridir. Dolayısıyla sözlükler üzerinde rahatlıkla istediğimiz değişikliği yapabiliriz. Sözlükler üzerinde 
# değişiklik yapma işlemi, biraz önce öğrendiğimiz, sözlüklere yeni öğe ekleme işlemiyle aynıdır
notlar = {'Seda': 98, 'Ege': 95, 'Mehmet': 77,
          'Zeynep': 100, 'Deniz': 95, 'Ahmet': 45}
# Ahmetin notunu 65 olarak değiştirelim
notlar['Ahmet'] = 65
print(notlar)



# Sözlük Üreteçleri (Dictionary Comprehensions)
# Tıpkı liste üreteçlerinde olduğu gibi, sözlük üreteçleri sayesinde tek satırda ve hızlı bir şekilde sözlükler üretebiliriz.
isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
# elimizde yukarıda bulunn isimler listesi var. her ismin kaç harften oluştuğunu gösteren bir sözlük yazalım:
sözlük = {i : len(i) for i in isimler} # bunun anlamı -> for i in isimler: -sözlük[i]=len(i)   2 satır olan işlemi tek satırda yazmak
print(sözlük)

harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
# amacımız türkçe harflerin her birine bir numara vermek olsun. yapmamız gereken sözlük:
sözlük = {i : harfler.index(i) for i in harfler}
print(sözlük)