# fonksiyon tanımlama
# bir fonksiyonun yaşam döngüsü iki aşamadan oluşur: Fonksiyon tanımı ve fonksiyon çağrısı. Bir fonksiyonun çalışabilmesi için o
# fonksiyonun tanımlandıktan sonra çağrılması gerekir
def bir_fonksiyon():
    (...)
# fonksiyon tanımının yapısına çok dikkat edin. İki nokta üst üste işaretinden sonraki satırda girintili olarak yazılan bütün kodlar 
# (yani fonksiyonun gövde kısmı) fonksiyonun bir parçasıdır. Girintinin dışına çıkıldığı anda fonksiyon tanımlama işlemi de sona erer.


# fonksiyonların yapısı
# bir fonksiyonun ilk parçasına ‘fonksiyon tanımı’ (function deﬁnition) adı verilir

def sistem_bilgisi_goster():
    import sys
    print("\n Sistemde kurulu Python'ın;")
    print("\t ana sürüm numarası: ",sys.version_info.major)
    print("\t alt sürüm numarası: ",sys.version_info.minor)
    print("\t minik sürüm numarası: ",sys.version_info.micro)

    print("\n Kullanılan işletim sisteminin;")
    print("\t adı: ",sys.platform)
sistem_bilgisi_goster() # parametre almadığı için parantez içi boş

# parametre alabilen bir fonksiyon yazalım:
def kare_bul(sayi):
    cikti = "{} sayısının karesi {}"
    print(cikti.format(sayi, sayi**2))
kare_bul(18)
kare_bul(2)  # artık parametre alan bir fonksiyon yazdık. parametre sayesinde istediğimiz sayının karesini bulabiliriz



# Parametreler ve Argümanlar
# parametre = fonksiyon tanımlarken parantez içinde belirttiğimiz, fonksiyon gövdesinde yapılan işin değişken öğelerini gösteren parçalardır.

# bir fonksiyonu tanımlarken belirlediğimiz adlara parametre, aynı fonksiyonu çağırırken belirlediğimiz adlara ise argüman deniyor. Parametre ve 
# argüman arasındaki fark budur.
# kare_bul fonksiyonunda 'sayi' bir parametre, bu sayıya karşılık yazdığımız '18','2' de birer argümadır.

# Sıralı (veya İsimsiz) Parametreler = fonksiyou çağırırken argüman ve parametre uym,sırasına dikkat etmemize denir
def hatalı_versiyon(isim, yas, memleket):
    print("adı: ", isim)
    print("yaşı: ", yas)
    print("şehir: ", memleket)
hatalı_versiyon("konya","mehmet",20) # gibi parametre sırasına dikkat etmeden çağırırsak çıktı hatalı olur


# İsimli parametre
hatalı_versiyon(isim="kadir", memleket="ankara", yas=15)  # parametreleri isimli kullandığımız için doğru çıktı aldık. artısı bu 
# isimli parametreyle sıralı parametresi aynı çağırma işleminde kullanamayız = hatalı_versiyon(isim="kadir", "ankara", 15) diyemeyiz hata alırız


# Varsayılan değerli parametreler
# print fonksiyonunu ele alırsak:
print("Bahar", 20) # aslında bu fonksiyon; print("Bahar", 20, sep=" ", end="\n", file=sys.stdout, flush=False) şeklindedir. sep,end,file ve flush 
# parametreleri öntanımlı değerler alır ve biz kendimiz değer atamazsak python kendi öntanımlı değerleriyle bu parametreleri doldurur. Bu parametrelere
# varsayılan değerli parametreler denir.
def kendi_varsayılanlı_fonksiyonum(kurulum_dizini="/usr/bin/"):
    print("Yükleme {} dizinine kuruldu!".format(kurulum_dizini))
kendi_varsayılanlı_fonksiyonum()  # parametresiz çağırırsak çıktı: Yükleme /usr/bin/ dizinine kuruldu! olucak
kendi_varsayılanlı_fonksiyonum("C:\\Users\\bahar") # parametre verip çağırdığımızda çıktı: Yükleme C:\Users\bahar dizinine kuruldu! olur



# Rastgele sayıda isimsiz parametre belirleme
def fonksiyon(*parametreler):
    print(parametreler)
fonksiyon(1,2,3,4,5)  # çıktı (1,2,3,4,5) olur; fonksiyon() adlı fonksiyona argüman olarak verdiğimiz her bir öğenin (1, 2, 3, 4, 5) tek bir demet içinde 
# toplandığını görüyoruz.
# !!=> * işareti herhangi bir öğeyi alıp, bunu parçalarına ayırıyor. İşte bu * işaretini fonksiyon tanımlarken kullandığımızda ise bu işlemin tam tersi gerçekleşiyor. 
# Yani fonksiyon tanımında parametrenin soluna * getirdiğimizde, bu fonksiyon çağrılırken verilen argümanlar tek bir değişken içinde bir demet olarak toplanıyor.
# fonksiyon tanımında parametrenin soluna * getirdiğimizde, bu fonksiyon çağrılırken verilen argümanlar tek bir değişken içinde bir demet olarak toplanıyor.
def carp(*sayilar):
    sonuc = 1
    for i in sayilar:
        sonuc *= i
    print(sonuc)
carp(10,5,8,6) # fonksiyon kendisine verilen bütün parametreleri birbiriyle çarpar çıktı: 2400 olur
# yaygın kullanım; def fonksiyon(*args)'dır. * işareti ile args kullanmak python'da geleneksel bir alışkanlıktır


# Rastgele sayıda isimli parametre belirleme
def fonksiyon(**args):
    print(args)
fonksiyon(isim="bahar", yas=21, şehir="ısparta")  # çıktı: {'isim':'bahar', 'yas':21, 'şehir':'ısparta'} şeklindedir. fonksiyonu tanımlarken parametremizin sol 
# tarafına yerleştirdiğimiz ** işareti, bu fonksiyonu çağırırken yazdığımız isimli parametrelerin bize bir sözlük olarak verilmesini sağlıyor.

def kayit_olustur(**bilgiler):
    for anahtar,deger in bilgiler.items():
        print("{:<10}: {}".format(anahtar,deger))
    print("-"*30)
kayit_olustur(isim="ece", soyisim="arıkan", yas=22, meslek="doktor")
kayit_olustur(yas=20, meslek="hemşire", isim="ayhan", soyisim="kara")
# ** işaretlerini kullanmamız sayesinde hem adlarını hem de değerlerini kendimiz belirlediğimiz bir kişi veritabanı oluşturma imkanı elde ediyoruz. Üstelik bu
# veritabanının, kişiye ait kaç farklı bilgi içereceğini de tamamen kendimiz belirleyebiliyoruz.
# ** işaretlerinin betimlediği parametre de geleneksel olarak ‘kwargs’ şeklinde adlandırılır. def fonksiyon(**kwargs)

# print() fonksiyonun alabildiği isimli parametrelerin sep, end, ﬁle ve ﬂush adlı parametreler olduğunu biliyorsunuz. Bizim amacımız bu fonksiyona bir de start 
# adında isimli bir parametre ekleyerek print() fonksiyonunun işlevini genişleten başka bir fonksiyon yazmak. Bu yeni parametre, karakter dizilerinin en başına 
# hangi karakterin geleceğini belirleyecek.
def bas(*args, start='', **kwargs):
    for oge in args:
        print(start+oge,**kwargs)
bas("öğe1", "öğe2", "öğe3", start="_._")  # Bu fonksiyon her bakımdan print() fonksiyonu ile aynı işlevi görecek. Ancak bas() fonksiyonu, print() fonksiyonuna ek olarak, 
# sahip olduğu start adlı bir isimli parametre sayesinde, kendisine verilen parametrelerin en başına istediğimiz herhangi bir karakteri ekleme olanağı da verecek
# -> **kwargs parametresi print() fonksiyonunun halihazırda sahip olduğu sep, end, ﬁle ve ﬂush parametrelerinin bas() fonksiyonunda da aynı şekilde kullanılmasını sağlıyor. 
# **kwargs şeklinde bir tanımlama sayesinde, print() fonksiyonunun isimli parametrelerini tek tek belirtip tanımlamak zorunda kalmıyoruz



# return Deyimi
def ismin_ne():
    isim = input("İsmin ne? ")
    return isim  # print(isim) yazsaydık tek görevi ismi ekrana basmak olucaktı
    print(10)  # renginden de anlaşılacağı gibi return'den sonra geldiği için ekrana basılmayacak
print("Merhaba {}. Nasılsın?".format(ismin_ne()))
# ismin_ne() adlı fonksiyondan isim değerini döndürmüş olmamız sayesinde bu değerle istediğimiz işlemi gerçekleştirebiliyoruz. Yani bu değeri sadece ekrana basmakla sınırlamıyoruz.
# Hatta fonksiyondan döndürdüğümüz değeri başka bir değişkene atama imkanına dahi sahibiz:
ad = ismin_ne()
print(ad)

# Bu deyim, içinde bulunduğu fonksiyonun çalışma sürecini kesintiye uğratır. Yani return deyimini kullandığınız satırdan sonra gelen hiçbir kod çalışmaz. 



# Örnek Uygulama:
# Amacımız belli miktarda ve belli aralıkta rastgele sayılar üreten bir program yazmak. Ancak programımız bu sayıları üretirken her sayıdan yalnızca bir adet üretecek;
import random  # Bu satır yardımı ile random modülünü içe aktarıyoruz

def sayi_uret(baslangic=0, bitis=500, adet=6):   # 3 farklı parametre almış sayi_uret fonksiyonu. Her parametrenin varsayılan değeri var!
    sayilar = set()  # küme tanımlayarak her sayıdan bir tane olmasını sağlıyoruz. aynı sayı istemediğimizi başta söyledik

    while len(sayilar) < adet:   # kullanıcı fonksiyonu parametresiz çağırırsa varsayılan değerlere göre dönecek döngü
        sayilar.add(random.randrange(baslangic, bitis))  
    
    return sayilar # fonksiyonu bu şekilde istediğimiz gibi kullanabiliriz
for i in range(20):
    print(sayi_uret()) # çıktımız her biri 6 öğeden oluşan 20 adet sayı listesi verdi. Parametresiz olarak kullandık yani başlangıç,bitiş,adet varsayılan(0,500,6) çalıştı

print(sayi_uret(0,100,10)) # Parametre vererek çağırabiliriz fonksiyonu. Bu kodlar bize 0 ile 100 arasından 10 adet rastgele sayı seçer
print(*sayi_uret(10,50,8), sep="/")  # çıktı küme parantezleri arasında görünmüyor(* işareti) ve aralarına / işareti getiriliyor(sep= ile)




# Fonksiyonların kapsamı ve global deyimi
x = 0

def fonk():
    x = 1
    return x

print("fonsiyonun dışındaki x: ", x)
print("fonksiyonun içindeki x: ",fonk())
# kodların çıktısı: fonksiyon içindeki x: 1  fonksiyon dışındaki x: 0  olur. 
# yukarıdaki kodlarda fonksiyon dışındaki x değişkeni ana isim alanında yer alan ‘global’ bir değişkendir. Fonksiyon içindeki x değişkeni ise 
# fonk() değişkeninin isim alanı içinde yer alan ‘lokal’ bir değişkendir. Bu iki değişken, adları aynı da olsa, birbirlerinden farklı iki nesnedir.
# Python'da 'name space(isim alanı)' adlı bir kavram vardır. Dolayısıyla Python'da her nesnenin, geçerli ve etkin olduğu bir isim alanı vardır.

a = 2  # buraya a değeri tanımlamasaydık kod hata verecekti. 
def fonk():
    return a
fonk() # çıktı global alandaki a'nın değerini vericek

def fonk():
    a = 8
    return a
fonk() # çıktı 8 değerini verir. Çünkü Python öncelikle mevcut isim alanını kontrol ediyor. a değişkeni mevcut isim alanında bulunduğundan globale
# bakma gereği duymuyor.


# **global isim alanındaki nesnelerin değerini lokal isim alanlarından sorgulayabiliyoruz. Ancak istediğimiz şey global isim alanındaki nesnelerin değerini
# değiştirmekse bazı kavramlar arasındaki farkları iyi anlamamız gerekiyor.

# -Eğer bir nesne değiştirilebilir bir nesne ise, o nesnenin değerini, lokal isim alanlarından değiştirebilirsiniz:
x = set()
def fonk():
    x.add(10)
    return x
print(fonk())

# -Ama eğer bir nesne değiştirilemez bir nesne ise, o nesnenin değerini zaten normalde de değiştiremezsiniz. Değiştirmiş gibi yapmak için ise o nesneyi 
# yeniden tanımlamamız gerektiğini biliyoruz:
isim_liste = []

def fonk():
    isim_liste.extend(["bahar","tahsin"])  # isim_liste += ["bahar","tahsin"] yazsaydık kod hata verirdi. Değiştirilebilen bir veri tipi olan listeleri, 
    # fonksiyon içinde yeniden tanımlayamazsınız. Ancak değişikliğe uğratabiliriz
    return isim_liste
print(fonk())


isim = "bahar"

def fonk():
    global isim  # İşte bu satır, isim adlı değişkenin global alana taşınmasını sağlıyor. Böylece global alanda bulunan isim adlı değişkeni değişikliğe uğratabiliyoruz
    isim += " ırmak"
    return isim
print(fonk())
# programlarımızda genellikle bu deyimi kullanmaktan kaçınmamız iyi bir ﬁkir olacaktır. Çünkü bu deyim aslında global alanı kirletmemize neden oluyor




