# küme oluşturma
bos_küme = set()
küme = set(["elma","süt","kebap"])
# Gördüğünüz gibi set() fonksiyonu içindeki öğeler bir liste içinde yer alıyor. Dolayısıyla yukarıdaki tanımlamayı şöyle de yapabiliriz:
liste = ["elma","süt","kebap"]
küme = set(liste)
# demet, sözlük ve karakter dizilerini de küme haline getirebiliriz. *** ama sayılardan küme oluşturamayız!!!

# listeler, demetler, sözlükler ve karakter dizilerinin aksine kümelerin [ ], ( ), { }, ‘ ‘ gibi ayırt edici bir işareti yoktur. Ama eğer istersek 
# sözlükleri oluşturmak için kullandığımız özel işaretleri küme oluşturmak için de kullanabiliriz.
sinif = {"ali","ayşe","veli","ela"}
print(type(sinif))  # <class 'set'> çıktısı alırız yani küme olduğunu görüyoruz
print(sinif)

# ** bir sözlüğü kümeye çevirdiğinizde, elbette sözlüğün yalnızca anahtarları kümeye eklenecektir. Sözlüğün değerleri ise böyle bir işlemin sonucunda ortadan kaybolur.
# Eğer bir sözlüğü kümeye çevirirken hem anahtarları hem de değerleri korumak gibi bir niyetiniz varsa:
bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux",
         "dağıtım": "Ubuntu GNU/Linux"}
liste = [(anahtar, deger) for anahtar, deger in bilgi.items()]
küme = set(liste)
print(küme)

# Kümelerin önemli bir özelliği de, tıpkı sözlükler gibi, herhangi bir şekilde ‘öğe sırası’ kavramına sahip olmamasıdır.



# kümelerin yapısı:
kardiz = "Python Programlama Dili"
küme = set(kardiz)
print(küme)    # çıktı={'g', 'D', 'a', ' ', 'o', 'n', 'm', 'l', 'i', 'h', 't', 'r', 'P', 'y'} bu şekilde olur ve örn: 2P var iken tek P var çıktıda
# *** kümeler aynı öğeyi birden fazla tekrar etmez. Aynı durum karakter dizisi dışında kalan öteki veri tipleri için de geçerlidir.
liste = ["elma", "armut", "elma", "kiraz",
         "çilek", "kiraz", "elma", "kebap"]
for i in set(liste):
    print("{} listede {} kez geçiyor!".format(i, liste.count(i)))



# Küme Üreteçleri (Set Comprehensions)
# küme üreteçlerini kullanarak tek satırda ve hızlı bir şekilde kümeler de üretebiliriz.

# liste içinde yer alan sayılardan, değeri 100’den küçük olanları listelemek isyoruz ama her sayıdan bir tane olsun dersen küme kullan.
import random
liste = [random.randint(0,1000) for i in range(1000)]
küme = {i for i in liste if i < 100}
print(küme)



# Kümelerin Metotları
# clear() = kümenin içini boşaltır
yemek = set(["erişte","türlü"])
yemek.clear()
print(yemek)  # set() çıktısı alırız, artık elimizde boş bir küme var



# copy() 
yer = set(["uşak"])
yeni_yer = yer.copy()
print(yeni_yer)


# add() = kümeye yeni öğe ekletir
# Kümelerden bahsederken, bunların değiştirilebilir bir veri tipi olduğunu söylemiştik.
yer.add("mersin")
print(yer)

# **Bir kümeye herhangi bir öğe ekleyebilmemiz için, o öğenin değiştirilemeyen (immutable) bir veri tipi olması gerekir. -Demetler -Sayılar  -Karakter Dizileri
kume = set()
d = (1,2,3)
s = 4
k = "bahar"
kume.add(d)
kume.add(s)
kume.add(k)
print(kume)



# difference() = iki kümenin farkınıı almamızı sağlar
k1 = set([2,4,6,8])
k2 = set([4,5,6,7])
print(k1.difference(k2))  # k1'in k2'den farkı : 2 8
print(k2.difference(k1))   # k2'nin k1'den farkı : 5 7 
print(k1 - k2)  # farkı bulmak için - işaretini de kullanabiliriz


# difference_update() = Bu metot, difference() metodundan elde edilen sonuca göre bir kümenin güncellenmesini sağlar
k1 = set([1, 2, 3])
k2 = set([1, 3, 5])
k1.difference_update(k2)
print(k1)
# k1 ile k2 arasındaki tek fark 2 adlı öğe idi. Dolayısıyla difference_update() metodunu uyguladığımızda k1’in öğelerini silinip yerlerine 2 adlı öğe geldi


# discard() = kümeden öğe silmemizi sağlar
# Eğer küme içinde bulunmayan bir öğe silmeye çalışırsak hiç bir şey olmaz. Yani hata mesajı almayız. etkileşimli kabuk sessizce bir alt satıra geçecektir.
# **Bu metodun en önemli özelliği budur. Yani olmayan bir öğeyi silmeye çalıştığımızda hata vermemesi.
hayvanlar = set(["kedi","köpek","kuş","ördek"])
hayvanlar.discard("köpek")
print(hayvanlar)
hayvanlar.discard("civciv") # hata vermiyor derleme kısmında



# remove()
# discard() metoduyla, kümede olmayan bir öğeyi silmeye çalışırsak herhangi bir hata mesajı almayacağımızı söylemiştik. Eğer remove() metodunu kullanarak,
# kümede olmayan bir öğeyi silmeye çalışırsak, discard() metodunun aksine, hata mesajı alırız. 



# intersection() = iki kümenin kesişim kümesini verecektir
k1 = set([1, 2, 3])
k2 = set([1, 3, 5])
print(k1.intersection(k2))  # k1 & k2 yazarak da kesişim sorgulayabiliriz!!

tr = "şçöğüıŞÇÖĞÜİ"
parola = input("Sisteme girmek için parolanızı belirleyin: ")

if set(tr) & set(parola):
    print("Parolanız Türkçe karakter içermemeli!")
else:
    print("Parolanız onaylandı!")



# intersection_update() = Bu metot, intersection() metodundan elde edilen sonuca göre bir kümenin güncellenmesini sağlar.
k1 = set([1, 2, 3])
k2 = set([1, 3, 5])
k1.intersection_update(k2)
print(k1)  # {1, 3} çıktısı verir. yani k1'in öğeleri silinir ve yerine k2 ile kesişim  öğeleri yazılır



# isdisjoint() = beklentiniz iki kümenin kesişim kümesinin boş olup olmadığını öğrenmekse: a ve b ayrık kümeler mi?
print(k1.isdisjoint(k2))  # k1=1,3 ve k2=1,3,5 olduğu için kesişimleri var ve False cevabı döner


# issubset() = bir kümenin bütün elemanlarının başka bir küme içinde yer alıp yer almadığını sorgulayabiliriz. Yani bir kümenin, başka bir kümenin 
# alt kümesi olup olmadığını öğrenebiliriz. Eğer bir küme başka bir kümenin alt kümesi ise bu metot bize True değerini verecek; eğer değilse False çıktısını verecektir
a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])
print(a.issubset(b))   # True cevabı döner çünkü a, b'nin alt kümesidir


# issuperset() = Matematik derslerinde gördüğümüz “kümeler” konusunda hatırladığınız “b kümesi a kümesini kapsar” ifadesini bu metotla gösteriyoruz.
print(b.issuperset(a))  # True döner yine çünkü b, a'yı kapsıyor


# union() = union() metodu iki kümenin birleşimini almamızı sağlar
s1 = set([2,4,6])
s2 = set([1,3,5]) 
print(s1.union(s2))   # s1 | s2 yazabiliriz. 


# update() 
küme = set(["elma", "armut", "kebap"])
yeni = [1, 2, 3]
for i in yeni:
   küme.add(i)  # yeni adlı listeyi kümeye for döngüsü ile ekledik.
print(küme)  

# update() ile bunu daha kolay yapabiliriz:
küme = set(["elma", "armut", "kebap"])
yeni = [1, 2, 3]
küme.update(yeni)  # tek satırda aynı işlemi yaptık
print(küme)


# symmetric_defference() = kümelerin sadece birinde bulunan öğeleri almamızı sağlar
k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
print(k1.symmetric_difference(k2))  # {2, 4, 5, 7} çıktısına bakarsak iki kümenin ortak olarak sahip olmadığı öğeleri almış olduk.


# symmetric_difference_update() 
k1.symmetric_difference_update(k2)
print(k1)  # {1, 2, 3, 4} değil {2, 4, 5, 7} çıktısı aldı. Yani k1 kümesi symmetric_difference() metodunun sonucuna göre güncellenmiş oldu. 


# pop() = kümelerin öğelerini silip ekrana basar. **küme öğelerini rastgele siler
hayvanlar = set(["kedi","köpek","kuş","ördek"])
print(hayvanlar.pop())



# Dondurulmuş Kümeler (Frozenset)
# Eğer öğeleri üzerinde değişiklik yapılamayan bir küme oluşturmak isterseniz set() yerine frozenset() fonksiyonunu kullanabilirsiniz.
degismeyen = frozenset("değiştirilemeyen içerik")

# Dondurulmuş kümeler ile normal kümeler arasında işlev olarak hiçbir fark yoktur. Kümenin metotlarında değişiklik yapmaya yönelik metotlar yok.