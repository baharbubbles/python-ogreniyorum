# 1.Lambda Fonksiyonları
fonk = lambda sayi1, sayi2: sayi1+sayi2
print(fonk(4,5))
# birleştir = lambda ifade, birleştirici: birleştirici.join(ifade.split())
# Burada lambda fonksiyonumuz toplam iki farklı parametre alıyor: Bunlardan ilki ifade, ikincisi ise birleştirici. Fonksiyonumuzun gövdesinde ifade 
# parametresine split() metodunu uyguladıktan sonra, elde ettiğimiz parçaları birleştirici parametresinin değerini kullanarak birbirleriyle birleştiriyoruz

# lambda fonksiyonu ne işe yarar?
# Lambda fonksiyonlarını, bir fonksiyonun işlevselliğine ihtiyaç duyduğumuz, ama konum olarak bir fonksiyon tanımlayamayacağımız veya fonksiyon tanımlamanın zor 
# ya da meşakkatli olduğu durumlarda kullanabiliriz.
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem", "can", "şule", "iskender"]
print(sorted(isimler, key=lambda x: çevrim.get(x[0])))  # sorted() fonksiyonunun key parametresi içinde kullandığımız ifade bir lambda fonksiyonudur
# sorted() fonksiyonunun key parametresi bizden bir fonksiyon tanımı bekler. Ancak biz elbette oraya def ifadesini kullanarak doğrudan bir fonksiyon tanımlayamayız. 
# Ama def yerine lambda ifadesi yardımıyla key parametresi için bir lambda fonksiyonu tanımlayabiliriz.

def sırala(eleman):
   return çevrim.get(eleman[0])
print(sorted(isimler, key=sırala))
# Burada lambda fonksiyonu kullanmak yerine, sırala() adlı bir fonksiyon kullandık



# 2.Özyinelemeli (Recursive) Fonksiyonlar
# Özyinelemeli fonksiyonlar; büyük bir problemin çözülebilmesi için, o problemin, problemin bütününü temsil eden daha küçük bir parçası üzerinde işlem yapabilmemizi sağlayan
# fonksiyonlardır
# Python fonksiyonları, nasıl başka fonksiyonları çağırabiliyorsa, aynı şekilde, istenirse, kendi kendilerini de çağırabilirler. İşte bu tür
# fonksiyonlara Python programlama dilinde ‘kendi kendilerini yineleyen’, veya daha teknik bir dille ifade etmek gerekirse ‘özyinelemeli’ (recursive) fonksiyonlar adı verilir

# kendisine parametre olarak verilen karakter dizisini teker teker azaltan bir fonksiyon:
def azalt(s):
   if len(s) < 1:
      return s
   else:
      print(s)
      return azalt(s[1:])  # [1:] ile karakter dizisini başından azaltarak son harf kalana kadar / return azalt(s[1:]) ile azalt fonk. içinde azalt fonk. tekrar çağırıyoruz
print(azalt("badana"))  
# fonksiyonumuz ilk çalışmada parametre olarak karakter dizisinin tamamını alıyor. Ancak fonksiyonun her yinelenişinde listedeki harﬂer birer birer düşüyor. Böylece özyinelemeli
# fonksiyonumuz parametre olarak karakter dizisinin her defasında bir eksiltilmiş biçimini alıyor

def azalt(s):
   if len(s) < 1:  # İşte biz özyinelemeli fonksiyonlarımızda dip noktayı mutlaka belirterek, Python’ın fonksiyonu yinelerken ne kadar derine inip nerede duracağını belirlemiş oluyoruz.
      return s
   else:
      print("özyineleme sürecine girerken: ", s)
      azalt(s[1:])
      print("özyinelme sürecinden çıkarken: ", s)
azalt("badana")
# fonksiyon özyineleme sürecine girerken düşürdüğü her bir karakteri, özyineleme sürecinden çıkarken yeniden döndürüyor. Bu, özyinelemeli fonksiyonların önemli bir özelliğidir.

# iç içe geçmiş listeleri tek katmanlı bir liste haline getireceğiz:
def düz_liste_yap(liste):
   if not isinstance(liste, list):  # dip noktayı yazıyoruz önce; temel çalışma prensibine göre liste içindeki bütün öğeleri tek tek alıp başka bir liste içinde toplayacağız. 
      return [liste]           # # Eğer liste elemanları üzerinde ilerlerken karşımıza liste olmayan bir eleman çıkarsa bu elemanı [liste] koduyla bir listeye dönüştüreceğiz.  
   elif not liste:       # ikinci dip nokta; Eğer özyineleme esnasında boş bir liste ile karşılaşırsak, tekrar boş bir liste döndürüyoruz.
      return []
   else:
      return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])  # Dip noktaya ulaşılana kadar yapılacak işlemler; Yani listenin ilk öğesine, geri kalan öğeleri teker teker ekliyoruz.
   
l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]
print(düz_liste_yap(l))



# 3.İç İçe (Nested) Fonksiyonlar
def yazici():
   def yaz(mesaj):
      print(mesaj)
   return yaz
# Şeklinde kapsayıcı fonksiyonumuzu tanımlamış oluyoruz. Dikkat ederseniz sadece kapsa- yıcı fonksiyonun tanımlandığını söyledim. Artık yazıcı fonksiyonunun, Python yorum- layıcısı
# tarafından ne yapacağı, nasıl çalışacağı biliniyor
# bir fonksiyon çağırılmadan içerisindeki komutlar çalışmaz. Eğer def yaz... komutu çalışmaz ise de yaz fonksiyonumuz tanımlanmış olmaz.
y = yazici()
y("merhaba")
# yazıcı fonksiyonumuz çağrıldığında değer olarak yaz fonksiyonunu çeviriyor. Bu yaz fonksiyonu da yazıcı fonksiyonumuzun içerisinde tanımladığı için bizim iç fonksiyonumuz oluyor. 
# yazıcı ise kapsayıcı fonksiyonumuz.
print(type(y))
print(y)
# yazıcı fonksiyonumuzu her çağırdımızda yaz sınıfı en baştan tanımlanır. Bu da yazıcı fonksiyonumuzu her çağırışımızda yeni tanımlanan yaz fonksiyonunun farklı ve tek olduğu
# anlamına gelir. Yani kapsayıcı olan yazıcı fonksiyonu sadece bir tane iken döndürdüğü yaz fonksiyonu birden fazla ve farklı oluyor. Yani yazıcı fonksiyonumuzu her çağırdığımızda
# sadece o çağırışımıza özel bir yaz fonksiyonu elde ediyoruz. İşte bu <locals> kelimesi buradan geliyor.

# -‘nonlocal’ Deyimi
# nonlocal deyimi yerel olmayan anlamına gelir. Kullanım amacı global deyimi ile benzerdir. *Ancak bunu kullanmamız küresel yani global değişkenlere ulaşmamızı değil, yerel olmayan
# değişkenlere ulaşmamızı sağlar. **Ayrıca bu deyimi sadece iç içe fonksiyonlarda kullanabiliriz.
def kapsayici_fonk():
   non_local_degisken = 1
   def ic_fonk():
      non_local_degisken = 2
      print(non_local_degisken)
   return ic_fonk

dönüs_fonk = kapsayici_fonk()
dönüs_fonk()  # 2 çıktısı verir. Yani kapsayıcı fonksiyona ait olan non_local_değişken ile iç fonksiyonumuza ait olan non_local_değişken farklılar

# iç_fonk ’un içinde kapsayıcı_fonk ’a ait olan non_local_değişken değişkenini değiştirmek istersek bunu da nonlocal deyimi ile şöyle yapabiliriz:
def kapsayici_fonk():
   non_local_degisken = 1

   def ic_fonk():
      nonlocal non_local_degisken
      non_local_degisken += 1
      print(non_local_degisken)
   return(ic_fonk)
dönüs_fonk = kapsayici_fonk()
dönüs_fonk()
# nonlocal ifadesi iç içe fonksiyonlar ile çalışırken iç fonksiyonda, kapsayıcı fonksiyonunun değişkenlerini değiştirmemizi sağlıyor

# değişkeni değiştirmek gibi bir amacımız yoksa, sadece kullanmak isteseydik şöyle de yapabilirdik ve nonlocal deyimine gerek kalmazdı:
def kapsayici_fonk():
   non_local_degisken = 1

   def ic_fonk():
      print(non_local_degisken)
   return(ic_fonk)

dönüs_fonk = kapsayici_fonk()
dönüs_fonk()



# 4.Üreteçler (Generators)
# Üreteçler, fonksiyonlara benzer şekilde tanımlanır. Hatta tek farkının yield adındaki bir ifade olduğunu söyleyebiliriz
def fonk_sayici():
   sayi = 0
   def say():
      nonlocal sayi
      sayi += 10
      return sayi
   return say
def üretec_sayici():
   sayi = 0
   while True:
      sayi += 10
      yield sayi
# type() yapıp baktığımızda fonk_sayici ve üretec_sayici birer fonksiyon olduğunu görürüz. üreteç_sayıcı aslında bir fonksiyon. Ama alelade bir fonksiyon değil,
# çağrıldığında generator nesnesi döndüren bir fonksiyon
fonk = fonk_sayici()
üretec = üretec_sayici()  # type(üretec) yaptığımızda class generator çıktısı alırız
print(fonk())
print(fonk())
print(next(üretec))
# fonk ve üreteclerde elde ettiğimiz sonuçların aynı olduğunu görüyoruz



# ‘yield’ Deyimi ve ‘next’ Fonksiyonu
# next fonksiyonu gömülü bir fonksiyondur. yield deyimi üreteçten değer döndürmemizi sağlar.
def üretec():
   yield "merhaba"
   yield "dünya"
# return deyiminin fonksiyonu sonlandırırken yield deyimi üretecin çalışmasına ara verir ve sağındaki değişkeni geriye döndürür. Herhangi bir değer verilmemiş ise None döndürecektir.
g = üretec()
print(next(g)) # merhaba 
print(next(g)) # dünya
# next fonksiyonunun, kendisine verilen üretecin kodunu bir yield deyimine rastlayana kadar çalıştırdığını, yield deyimine rastladığında ise deyimin sağındaki değişkeni döndürdüğünü 
# görebiliriz. Unutmayalım ki bu döndürme işlemini yapan next fonksiyonudur.
# print(next(g)) # Üretecimizin içinde herhangi bir yönerge kalmadığında ise next fonksiyonumuz StopIteration hatası yükseltmektedir.

# ** ‘next’ fonksiyonunun burada yaptığı iş için ‘yineleme (iteration)’ terimi kullanılır. ‘next’ fonksiyonuna parametre olarak verilebilen nesneler ise birer ‘yinelenebilir nesne (iterable
# object)’dir. ‘generator’ sınıfı yinelenebilir nesnelere bir örnektir.

def üreteç():
    print("üreteç ilk defa next fonksiyonu ile kullanıldı.")
    yield "1. yield"
    print("üreteç ikinci defa next fonksiyonu ile kullanıldı.")
    yield "2. yield"
    print("üreteç üçüncü defa next fonksiyonu ile kullanıldı ve bitti.")

b = üreteç()
ilk_dönüs = next(b)
ikinci_dönüs = next(b)
#ücüncü_dönüs = next(b)  StopIretion hatası verir
print(ilk_dönüs)
print(ikinci_dönüs)
#print(ücüncü_dönüs)     NameError hatası verir

# while döngüsü kullanarak, 1’den başlayarak her yinelediğimizde ﬁbonacci sayı dizisinin bir sonraki elemanını döndürecek bir üreteç yazalım:
def fibonacci():
   x = 1
   y = 0
   z = 0
   while True:  # if döngüsü yazmak yerine 'while not x >100' yazabilirdik
      z = y
      y = x
      x = y+z
      yield x
      if x > 100:
         return

f = fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

for i in fibonacci():
   print(i)
# Ancak bu örnekte üretecimiz hiç durmuyor. Bazen üreteçlerimizin durmasını isteyebiliriz. Bunu yapmamız için tek gereken şey üretecimizin durmasını istediğimiz yerde üretecimizi
# return etmemizdir. Sonuçta üreteçler de bir tür fonksiyondur ve return deyimi fonksiyonları sonlandırır (bu return deyiminden dönen değer üreteçlerde bize ulaşmaz). Bu durum next
# fonksiyonunun StopIteration yükseltmesine neden olur. for döngüsü bu hatayı yakalar ve üretecimizin bittiğini anlar


# ‘yield from’ Deyimi
# yield from deyimi bir üretecin içinde, başka bir üretecin yield ile döndüreceği değerleri tekrar yield etmek istediğimizde kullanılabilir.
def üreteç1():
    yield "üreteç1 başladı"
    yield "üreteç1 bitti"
def üreteç2():
    yield "üreteç2 başladı"
    yield from üreteç1()  # ifadesi 'for i in üreteç1: >>> print(i)' ile eşittir
    yield "üreteç2 bitti"

for i in üreteç2():  
   print(i)








