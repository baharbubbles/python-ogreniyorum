# Gömülü fonksiyonlar İngilizcede builtin functions olarak adlandırılır. Bu fonksiyonlar gerçekten de dile gömülü vaziyettedirler. 
# Bildiğiniz gibi, bir fonksiyonu kullanabilmemiz için o fonksiyonu tanımlamamız gerekir. İşte gömülü fonksiyonlar, bizim tanımlamamıza gerek
# kalmadan, Python geliştiricileri tarafından önceden tanımlanıp dile gömülmüş ve hizmetimize sunulmuş faydalı birtakım araçlardır.

# 1-abs() = fonksiyonu bir sayının mutlak değerini elde etmek için kullanıyoruz. Mutlak değer’ bir sayının 0’a olan uzaklığıdır.
print(abs(-20))
print(abs(20+3j)) # Gördüğünüz gibi bu fonksiyon yalnızca tek bir parametre alıyor ve bu parametrenin mutlak değerini döndürüyor.


# 2-round() = fonksiyonu bir sayıyı belli ölçütlere göre yukarı veya aşağı doğru yuvarlamamızı sağlar.
print(round(12.7))

print(round(1.5))   # fonksiyonumuz 1.5 sayısını yukarı doğru, 12.5 sayısını ise aşağı doğru yuvarladı. Bunun sebebi, kayan noktalı bir sayının 
print(round(10.5)) # üst ve alt tam sayılara olan uzaklığının birbirine eşit olduğu durumlarda Python’ın çift sayıya doğru yuvarlama yapmayı tercih etmesidir

# round() fonksiyonu toplam iki parametre alır. İlk parametre, yuvarlanacak sayının kendisidir. Yuvarlama hassasiyetini belirlemek için ise 
# ikinci bir parametreden yararlanabiliriz.
print(22/7)
print(round(22/7, 2))   # ,2 ile virgülden sonra 2 basamak almasını sağladık


# 3-all() = fonksiyonun görevi, bir dizi içinde bulunan bütün değerler True ise True değeri, eğer bu değerlerden herhangi biri False ise de False değeri döndürmektir.
liste = [1, 2, 3, 4]
print(all(liste))  # 0 hariç bütün sayıların bool değeri True’dur. Yukarıdaki listede False değeri verebilecek herhangi bir değer bulunmadığından, all() fonksiyonu 
# bu liste için True değerini veriyor
liste1 =[0, 1, 2, 3]
print(all(liste1)) # Burada 0'ın bool değeri false olduğundan çıktı False olur

a = 3
t1 = a == 3  # sayı 3 mü?
t2 = a < 4   # sayı 4'ten küçük mü?
t3 = a % 2 == 1   # sayı tek sayı mı?
print(all([t1, t2, t3]))  # sayı bu özelliklerin hepsine sahip mi?     Çıktı True olur. Eğer bir tanesi bile doğru olmasaydı çıktı False olucaktı


# 4-any() = fonksiyonu bir dizi içindeki bütün değerlerden en az biri True ise True çıktısı vermektir.
liste = ["ahmet", "", "mehmet"]
print(any(liste))  # çıktı True
# any() fonksiyonunun True çıktısı verebilmesi için listede yalnızca bir adet True değerli öğe olması yeterlidir. Bu fonksiyonun False çıktısı verebilmesi 
# için dizi içindeki bütün öğelerin bool değerinin False olması gerekir. Bir nevi all'un tersidir.
l = ['', 0, [], (), set(), dict()]
print(any(l))  # çıktı False


# 5-ascii() = 
print("\n")
print(ascii("\n!"))  # ascii() fonksiyonu, satır başı kaçış dizisinin görevini yapmasını sağlamak yerine bu kaçış dizisinin ekrana basılabilir halini veriyor bize.

a = "ışık"
print(ascii(a))
# Ayrıca bu fonksiyon, karakter dizileri içindeki Türkçe karakterlerin de UNICODE temsillerini döndürür. ascii() fonksiyonu ASCII olmayan karakterlerle karşılaştığında 
# bunların karakter temsilleri yerine UNICODE temsillerini (veya onaltılık sayma düzenindeki karşılıklarını) veriyor. 

liste = ['elma', 'armut', 'erik']
temsil = ascii(liste)
print(temsil)  # listemiz ascii() fonksiyonuna parametre olarak verildikten sonra artık liste olma özelliğini yitirip bir karakter dizisi haline gelir.
print(type(temsil))  # <class 'str'> çıktısında da görebiliriz bunu!
print(temsil[0])  # [ parametresi karakter dizisine dönüşüyor 0. indise tehabül ediyor


# 6-repr() = 
print(ascii("şeker"))
print(repr("şeker"))
# repr() fonksiyonu ise ASCII olmayan karakterlerle karşılaşsa bile, bize çıktı olarak bunların da karakter karşılıklarını gösterir
# Geri kalan özellikleri bakımından repr() ve ascii() fonksiyonları birbiriyle aynıdır.


# 7-bool() = Nesnenin bool değerini verir


# 8-bin() = Bu fonksiyon, bir sayının ikili düzendeki karşılığını verir. Bu fonksiyonun verdiği çıktının bir sayı değil, karakter dizisi olduğuna dikkat etmelisiniz.


# 9-bytes() = fonksiyon, bytes türünde veriler oluşturmaya yarar. görevi de farklı veri tiplerini ‘bayt’ adlı veri tipine dönüştürmektir.
print(bytes("ışık", "cp1254"))
# bytes() fonksiyonuna verdiğimiz ikinci parametrenin isminin encoding olduğunu ve bu parametreyi isimli bir parametre olarak da kullanabiliriz.
print(bytes('şeker', encoding='cp857', errors='xmlcharrefreplace'))


# 10-bytearray() = bytearray() ve bytes() fonksiyonları birbirlerine çok benzer. Bu ikisi arasındaki tek fark, bytearray() ile oluşturulan veri tipinin, bytes() ile 
# oluşturulan veri tipinin aksine, değiştirilebilir olmasıdır.


# 11-chr() = kendisine parametre olarak verilen bir tam sayının karakter karşılığını döndürür. sayıları karakterlere dönüştürürken ASCII sistemini değil, UNICODE sistemini
# temel alır. Dolayısıyla bu fonksiyon ile 128 (veya 255) üstü sayıları da dönüştürebiliriz.


# 12-list() 
#12.1 = liste tipinde veri kullanmak için;
k = list()
#12.2 = farklı veri tiplerini liste adlı veri tipine dönüştürmek için;
print(list("anahtar"))    # karakter dizisini listeye dönüştürdük
s = {"elma":10, "muz":20, "kivi":30}
print(list(s))   # sözlük listeye dönüştürülürken sözlüğün anahtarları dikkate alınır
print(list(s.values()))  # dersek de sözlüğün değerlerini listeye çevirebiliriz


# 13-set() = fonksiyonun görevi farklı veri tiplerini kümeye dönüştürmektir


# 14-tuple() = farklı veri tiplerini demete dönüştürür


# 15-frozenset() = farklı veri tiplerini dondurulmuş kümeye dönüştürür


# 16-complex() = karmaşık sayıları ifade etmede veya herhangi bir sayıyı karmaşık sayıya dönüştürmede kullanılır


# 17-float() = sayıları veya karakter dizilerini kayan noktalı sayıya dönüştürmek için


# 18-int() = int() fonksiyonunun en temel görevi, bir karakter dizisi veya kayan noktalı sayıyı (eğer mümkünse) tam sayıya dönüştürmektir
# Bunun dışında herhangi bir sayma sisteminde temsil edilen sayıyı onlu sayma sistemine dönüştürmek için 
print(int("12", 8))  # 8li sayma sistemindeki 12yi 10lu sisteme dönüştürür


# 19-str() = farklı veri tiplerini karakter dizisine dönüştürür. bir baytı karakter dizisine dönüştürmek için str() fonksiyonuna encoding adlı bir 
# parametre veriyoruz
bayt = b"karanfil"
kardiz = str(bayt, encoding="utf-8")
print(kardiz)
# belirttiğiniz kodlama biçiminin herhangi bir baytı karakter dizisine dönüştüremediği durumlara karşı bir errors parametresi de verebiliriz
kardiz = str(bayt, encoding="ascii", errors="ignore")
print(kardiz)


# 20-dict() = farklı veri tiplerinden sözlük üretmeyi sağlar


# 21-callable() = Bu fonksiyon, bir nesnenin ‘çağrılabilir’ olup olmadığını denetler. Mesela fonksiyonlar çağrılabilir nesnelerdir. Değişkenler ise
# çağrılabilir nesneler değildir
print(callable(open))  # Pythonda open() adlı bir fonksiyon olduğu için True cevabı döner


# 22-ord() = Bu fonksiyon, bir karakterin karşılık geldiği ondalık sayıyı verir.


# 23-oct() = Bu fonksiyon, bir sayıyı sekizli düzendeki karşılığına çevirmemizi sağlar

# **Yalnız hem oct() hem de hex() fonksiyonlarında dikkat etmemiz gereken şey, bu fonksiyonların parametre olarak bir sayı alıp, çıktı olarak bir karakter dizisi veriyor olmasıdır.

# 24-hex() = Bu fonksiyon, bir sayıyı onaltılı düzendeki karşılığına çevirmemizi sağlar


# 25-eval(), exec(), globals(), locals(), compile()
# expression denen ‘ifadeler’, bir değer üretmek için kullanılan kod parçalarıdır. Karakter dizileri, sayılar, işleçler, öteki veri tipleri, liste üreteçleri, sözlük üreteçleri, küme
# üreteçleri, fonksiyonlar hep birer ifadedir
23+4
len([1,2,3])
# statement olarak adlandırılan ‘deyimler’ ise ifadeleri de kapsayan daha geniş bir kavramdır. Buna göre bütün ifadeler aynı zamanda birer deyimdir. Daha doğrusu, ifadelerin
# bir araya gelmesi ile deyimler oluşturulabilir.
a = 5

if a:
    print(a)

# deyim mi yoksa ifade mi olduğundan emin olamadığınız bir şeyi eval() fonksiyonuna parametre olarak verdiğinizde hata almıyorsanız o parametre bir ifadedir. Eğer hata alıyorsanız 
# o parametre bir deyimdir. Çünkü eval() fonksiyonuna parametre olarak yalnızca ifadeler verilebilir.

# exec() fonksiyonu, mevcut isim alanı içinde a adlı bir değişken oluşturdu.
a=10
exec("a=6")  # a'nın 10 olan değerini silip 6 koydu
print(a)  # çıktı 6 olur

# Python programlama dilinde isim alanları sözlük tipinde bir veridir. Örneğin global isim alanı basit bir sözlükten ibarettir. Global isim alanını gösteren sözlükte hangi anahtar ve 
# değerlerin olduğunu görmek için globals() adlı bir fonksiyonu kullanabilirsiniz. Sözlükle ne yapabilirsek bu sözlük ile de aynı şeyi yapabiliriz
# ‘globals’ adlı bu sözlüğün içeriği, o anda global isim alanında bulunan nesnelere göre farklılık gösterecektir.
x = 10
globals()["j"] = 20   # global isim alanına z adlı bir değişken eklemiş olduk
print("j") 

# Lokal isim alanlarının, fonksiyonlara (ve ileride göreceğimiz gibi sınıﬂara) ait bir isim alanı olduğunu biliyorsunuz. İşte bu isim alanlarına ulaşmak için de locals() adlı bir fonksiyondan
# yararlanacağız
def fonksiyon(param1, param2):
   x = 10
   print(locals())
fonksiyon(10, 20)

# exec() ile oluşturduğumuz değişkenleri global isim alanı yerine nasıl farklı bir isim alanına göndereceğimizi öğrenelim:
c = 7
print(c)
isim_alani = {}
exec("c = 5", isim_alani)  # global isim alanındaki a değişkeninin değerine dokunmamış olduk
print(isim_alani["c"])  # Yeni oluşturduğumuz değer ise ia adlı yeni isim alanına gitti


# 26-dir() = dir() fonksiyonunu parametresiz olarak kullanırsak, mevcut isim alanındaki öğeleri bir liste halinde elde ederiz. dir() fonksiyonu globals() ve locals() fonksiyonlarına benzer. Ancak
# onlardan farkı, dir() fonksiyonunun çıktı olarak bir liste, globals() ve locals() fonksiyonlarının ise birer sözlük vermesidir
# bu fonksiyonu kullanarak farklı veri tiplerinin metot ve niteliklerini listeleyebiliriz


# 27-divmod() = divmod(10, 2) komutu bize iki öğeli bir demet veriyor. Bu demetin ilk öğesi, divmod() fonksiyonuna verilen ilk parametrenin ikinci parametreye bölünmesi işleminin sonucudur. 
# Demetimizin ikinci öğesi ise, ilk parametrenin ikinci parametreye bölünmesi işleminden kalan sayıdır. Yani demetin ilk parametresi bölme işleminin ‘bölüm’ kısmını, ikinci öğesi ise ‘kalan’ kısmını verir.
print(divmod(10, 2))  # (5, 0) çıktısı verir


# 28-enumerate() = bu fonksiyonu kullanarak nesneleri numaralandırabiliriz
print(*enumerate("karnabahar"))   # ‘enumerate’ nesnesi bize her koşulda iki öğeli demetler verir
print(*enumerate("karnabahar", 1))  # saymaya 0'dan değil de 1'den başlaması için başlangıç sayısı verebiliriz


# 29-exit() = Bu fonksiyon, o anda çalışan programdan çıkmanızı sağlar. Eğer bu komutu etkileşimli kabukta verirseniz o anda açık olan oturum kapanacaktır


# 30-help() = Gömülü fonksiyonlar içinde en faydalı fonksiyonların başında gelir. Bu fonksiyonu kullanarak Python programlama diline ait öğelere ilişkin yardım belgelerine ulaşabiliriz.


# 31-id() = Python'da her nesnenin kimliği eşsiz, benzersizdir.


# 32-input() = bu gömülü fonksiyonu kullanarak kullanıcı ile veri alışverişinde bulunabiliyoruz


# 33-format() = **format() fonksiyonu, daha önce öğrendiğimiz format() metoduna göre daha dar kapsamlıdır. format() metodunu kullanarak oldukça karmaşık karakter dizisi
# biçimlendirme işlemlerini gerçekleştirebiliriz, ama birazdan inceleyeceğimiz format() gömülü fonksiyonu yalnızca tek bir değeri biçimlendirmek için kullanılır


# 34-filter() = dizi niteliği taşıyan nesneler içindeki öğeler üzerinde belirli bir ölçüte göre bir süzme işlemi uygulayabiliriz.
l = [400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31, 120, 120, 236, 241, 123, 249, 364, 292, 153]
# amacımız bu liste içindeki tek sayıları süzmek;
def tek(sayi):
    return sayi % 2 == 1
print(*filter(tek, l))
# filter() fonksiyonu toplam iki parametre alır. Bu parametrelerden ilki ölçütü belirleyen fonksiyon, ikincisi ise bu ölçütün uygulanacağı öğedir. Yukarıdaki örneğe baktığımızda, tek()
# adlı fonksiyonun, l adlı öğe üzerine uygulandığını görüyoruz


# 35-isinstance() = tip denetimi için kullanabileceğimiz bir fonksiyon daha var. Bu fonksiyonun adı isinstance()
print(isinstance("bardak", str))  # True çıktısı verir çünkü bardak karakter dizisidir


# 36-len() = nesnelerin uzunluklarını hsaplamada kullanıyoruz


# 37-map() = 
l = [1, 4, 5, 4, 2, 9, 10]
# amacımız bu liste içindeki her bir öğenin karesini hesaplamak;
def karesi(n):
    return n**2
print(list(map(karesi, l)))


# 38-max() = görevi, bir dizi içindeki en büyük öğeyi vermektir. Bu fonksiyon birkaç farklı parametre alır ve verdiği çıktı, aldığı parametrelerin türüne ve sayısına bağlı olarak
# değişiklik gösterebilir
print(max(4,8,7))   # 8 çıktısını verir

# key isimli bir parametre de alır. Bu parametre yardımıyla max() fonksiyonunun ‘en büyük’ kavramını hangi ölçüte göre seçeceğini belirleyebiliriz.
isimler = ['ahmet', 'can', 'mehmet', 'selin', 'abdullah', 'kezban']
print(max(isimler, key=len))  # key fonksiyonuna len() fonksiyonunu parantezsiz olarak verdiğimize dikkat edin!

def en_yüksek_rütbe(rütbe):
    rütbeler = {
        "er"      :0,
        "onbaşı"  :1,
        "çavuş"   :2,
        "asteğmen":3,
        "teğmen"  :4,
        "üsteğmen":5,
        "yüzbaşı" :6,
        "binbaşı" :7,
        "yarbay"  :8,
        "albay"   :9
    }
    return rütbeler[rütbe]
askerler = {'ahmet': 'onbaşı',
            'mehmet': 'teğmen',
            'ali': 'yüzbaşı',
            'cevat': 'albay',
            'berkay': 'üsteğmen',
            'mahmut': 'binbaşı'}
print(max(askerler.values(), key=en_yüksek_rütbe))  # Böylece askerler adlı sözlüğün değerleri en_yüksek_rütbe() fonksiyonunun sunduğu ölçüt
# üzerinden ele alınacak ve en büyük sayı değerine sahip olan rütbe çıktı olarak verilecektir.

# rütbe ile birlikte bu rütbeyi taşıyan askerin adını da öğrenmek istersek:
for k, v in askerler.items():
   if askerler[k] == max(askerler.values(), key=en_yüksek_rütbe):
      print(v, k)


# 39-min() = min() fonksiyonu da bir dizi içindeki en küçük öğeyi bulur. Bu fonksiyonun kullanımı max() ile aynıdır.


# 40-open() = Bu fonksiyon herhangi bir dosyayı açmak veya oluşturmak için kullanılır. Eğer dosyanın açılması veya oluşturulması esnasında bir hata 
# ortaya çıkarsa IOError türünde bir hata mesajı verilir.

# fonksiyonun formülü:
# open(dosya_adi, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# - open() fonksiyonunun ilk parametresi dosya_adi’dır. Yani açmak veya oluşturmak istediğimiz dosya adı
# - open() fonksiyonunun ikinci parametresi olan mode yardımıyla, herhangi bir dosyayı hangi kipte açmak istediğimizi belirtebiliyoruz. Default değeri okuma kipidir.

# r = okuma kipi, öntanımlı bulunur / w = Yazma kipidir. Eğer belirtilen adda dosya zaten varsa o dosya silinir. / x = Yeni bir dosya oluşturulup yazma kipinde açılır.
# a = Dosya ekleme kipinde açılır. Bu kip ile, varolan bir dosyanın sonuna eklemeler yapılabilir. / b = Dosyaları ikili kipte açmak için kullanılır.
# t = Dosyaları metin kipinde açmak için kullanılır. Öntanımlı değerdir. /  + = Aynı dosya üzerinde hem okuma hem de yazma işlemleri yapılmasını sağlar


# 41-pow() = bu fonksiyonu bir sayının kuvvetlerini hesaplamak için kullanıyoruz. pow() fonksiyonu toplamda üç farklı parametre alır. Üçüncü parametre ise kuvvet hesaplaması sonucu 
# elde edilen sayının modülüsünü hesaplayabilmemizi sağlar
# ! pow() fonksiyonu çoğunlukla yalnızca ilk iki parametresi ile birlikte kullanılır


# 42-print()

# 43-quit() = Bu fonksiyonu programdan çıkmak için kullanıyoruz. Eğer bu fonksiyonu etkileşimli kabukta verecek olursanız etkileşimli kabuk kapanacaktır.

# 44-range() = Bu fonksiyonu belli bir aralıktaki sayıları listelemek için kullanıyoruz
# range() fonksiyonundan elde ettiğiniz ‘range’ nesnesinin içeriğini elde etmek için bunu başka bir veri tipine dönüştürmenin yanısıra, bu nesne üzerinde bir for döngüsü de kurabilirsiniz

# 45-reversed() = bir liste öğelerini ters sıraya çevirmek istersek, reversed() fonksiyonu da bize ürettiği öğelerin kendisi yerine, bir ‘nesne’ veriyor.

# 46-sorted() = bir dizi içindeki öğeleri belirli bir ölçüte göre sıraya dizmemizi sağlıyor. sorted() adlı fonksiyon, dizi özelliği taşıyan her türlü nesne üzerine uygulanabilir
# !! sorted() fonksiyonuna hangi türde bir veri tipi verirseniz verin, aldığınız çıktı her zaman bir liste olacaktır.


# 47-slice() = birtakım öğelerden oluşan bir nesnenin yalnızca belli kısımlarını ayırıp alma işlemine ‘dilimleme’ diyoruz. dilimleme işlemleri için slice() adlı bir gömülü fonksiyondan yararlanabiliriz.
l = ['ahmet', 'mehmet', 'ayşe', 'senem', 'salih']
dilimle = slice(0,3)       # slice(başlangıç, bitiş, atlama)
print(l[dilimle])


# 48-sum() = Bu fonksiyonun temel görevi, bir dizi içindeki değerlerin toplamını bulmaktır
l=[1,2,3]
print(sum(l))
# ikinci bir parametre daha alır:
print(sum(l, 10))  # verilen ikinci parametreyi, birinci parametredeki toplam değerin üzerine ekliyor


# 49-type() = type() fonksiyonunun görevi bir nesnenin hangi veri tipine ait olduğunu söylemektir

# 50-zip() = 
a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']
# listelerin öğelerini birbirleriyle eşleştirmek istersek zip() fonksiyonundan yararlanabiliriz:
zip(a1, a2)
# yukarıdaki kod bize bir ‘zip’ nesnesi veriyor
print(*zip(a1, a2)) 
for a,b in zip(a1, a2):
    print(a,b)         # ilk listenin ilk öğesinin, ikinci listenin ilk öğesiyle; ilk listenin ikinci öğesinin, ikinci listenin ikinci öğesiyle; 
# ilk listenin üçüncü öğesinin ise, ikinci listenin üçüncü öğesiyle eşleştiğini görüyoruz

isimler = ['ahmet', 'mehmet', 'zeynep', 'ilker']
yaşlar = [25, 40, 35, 20]
for i,y in zip(isimler, yaşlar):
    print("isim: {} / yaş: {}".format(i,y))


# 51- vars() = mevcut isim alanı içindeki metot, fonksiyon ve nitelikleri listeler. Eğer bu fonksiyonu parametresiz olarak kullanırsak, daha önce gördüğümüz 
# locals() fonksiyonuyla aynı çıktıyı elde ederiz
# Bu fonksiyonu, nesnelerin metotlarını ve niteliklerini öğrenmek için de kullanabilirsiniz. Bu yönüyle vars() fonksiyonu dir() fonksiyonuna benzer
print(vars(str))


