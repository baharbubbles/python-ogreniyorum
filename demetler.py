# Demetler, özellikle görünüş olarak listelere çok benzeyen bir veri tipidir. Bu veri tipi de, tıpkı listeler gibi, 
# farklı veri tiplerini içinde barındıran kapsayıcı bir veri tipidir.
# demetlerin ayırt edici özelliği de normal parantez işaretleridir.  demetler type() sorgusuna tuple cevabı veriyor.
# demet tanımlama çeşitleri:
demet = ("ayşe","fatma",14,15)
demet = "ayşe","fatma",14,15

# Demet oluşturmak için tuple() adlı bir fonksiyondan da yararlanabilirsiniz. Bu fonksiyon, liste oluşturan list() fonksiyonuna çok benzer
tuple("abcdf")
# Bu fonksiyonu kullanarak başka veri tiplerini demete dönüştürebiliriz
tuple(["ayşe","fatma",14,15])

# tek öğeli demet tanımlama:
demet = ("ayşe",)
demet = "ayşe",
# tek öğeli bir demet tanımlarken, o tek öğenin yanına bir tane virgül işareti yerleştiriyoruz. **Böylece demet tanımlamak isterken,
# yanlışlıkla alelade bir şekilde ‘ahmet’ adlı bir karakter dizisini ‘demet’ adlı bir değişkene atamamış oluyoruz

# demet öğelerine erişirken indeksleme ve dilimleme kuralları aynen demetler için de geçerli.

# Demetlerle Listelerin Farkı
# listeler değiştirilebilir (mutable) bir veri tipi iken, demetler değiştirilemez (immutable) bir veri tipidir.
# eğer programın akışı esnasında üzerinde değişiklik yapmayacağınız veya değişiklik yapılmasını istemediğiniz birtakım veriler varsa ve 
# eğer siz bu verileri liste benzeri bir taşıyıcı içine yerleştirmek istiyorsanız, listeler yerine demetleri kullanabilirsiniz.
demet = ("ahmet","mehmet")
demet = demet + ("veli",)   # **Python programlama dilinde sadece aynı tür verileri birbiriyle birleştirebilirsiniz. ("veli",) yazdığına dikkat edin

##########################################################################

# Listelerin metotları
# append() = Bu metodu, bir listeye öğe eklemek için kullanıyoruz. yeni öğeyi listenin en sonuna ekler
liste = ["elma","armut","çilek"]
liste.append("kivi")
# ** append() metodu yalnızca tek bir parametre alabilir. Yani bu metodu kullanarak bir listeye birden fazla öğe ekleyemezsiniz. bu sebeple
# ekleyeceğiniz listelerin üzerinde bir for döngüsü kurmalısınız

# kullanıcının girdiği sayıları birbiriyle çarpan uygulama
kontrol = []
sonuc = 1

while True:
    sayilar = input("çarpmak istediğiniz sayıları girin(hesaplamak için q'ya basın): ")
    if sayilar == "q":
        break
    kontrol.append(sayilar)
    sonuc *= int(sayilar)
if len(kontrol) < 2:
    print("yeterli sayı girilmedi!")
else:
    print(sonuc)


# extend() = extend() adlı metot da kelime anlamına uygun olarak listeleri ‘genişletir’. bir listeye başka bir liste ekleyeceksek
# extend() metodunu kullanmayı tercih edebiliriz.
li1 = [1,2,3]
li2 = [4,5,6]
li1.extend(li2)  # append() ile yazsaydık çıktımız [1,2,3,[4,5,6]] olacaktı yani [4,5,6] listesi öteki listeye tek bir liste halinde eklenecekti
print(li1)


# insert() = öğeleri listenin istediğimiz bir konumuna yerleştirmemizi sağlar
# insert() metodu iki parametre alıyor. İlk parametre, öğenin hangi konuma yerleştirileceğini, ikinci parametre ise yerleştirilecek öğenin ne olduğunu gösteriyor.
liste = ["ayşe","bahar"]
liste.insert(1,"fatma")    # fatma'yı ayşe ile bahar'ın arasına koymasını yani 1.indise koymak istiyoruz
print(liste)
# ìnsert() metodu özellikle dosya işlemlerinde işinize yarar



# remove() = listeden öğe silmemizi sağlar
liste.remove("bahar")
print(liste)



# reverse() = listelerin öğelerini ters çevirmek için kullanılır
meyve = ["muz","çilek","armut","karpuz"]
# liste metodunu list[::-1] yazarak dilimleme yöntemiyle ters çevirebileceğimizi biliyoruz
print(meyve[::-1])
# reversed() fonksiyonunu bir liste üzerine uyguladığımızda ‘list_reverseiterator’ adı verilen bir nesne elde ediyoruz. Bu nesnenin içeriğini
# görmek için birkaç farklı yöntemden yararlanabiliriz:
print(*reversed(meyve))
# ya da
print(list(reversed(meyve)))
# ya da
for i in reversed(meyve):
    print(i)

# Bu yöntemlere ek olarak reverse() metodunu ekliyoruz
meyve.reverse()
print(meyve)



# pop() = remove() metodu gibi, bu metot da bir listeden öğe silmemizi sağlar
# pop() metodunu kullanarak bir liste öğesini sildiğimizde, silinen öğe ekrana basılacaktır. Bu metot parametresiz olarak kullanıldığında 
# listenin son öğesini listeden atar. Alternatif olarak, bu metodu bir parametre ile birlikte de kullanabilirsiniz.
print(meyve.pop(0)) # meyve.pop(0) komutu listenin 0. öğesini listeden atar ve atılan öğeyi ekrana basar.



# sort() = sort() adlı bu önemli metot bir listenin öğelerini belli bir ölçüte göre sıraya dizmemizi sağlar.
# diyelim elimizde bi liste var ve listaedeki isimleri alfabetik sıraya göre dizmek istiyoruz
uyeler = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep',
'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem',
'Sinem', 'Tayfun', 'Tuna', 'Tolga']
uyeler.sort()
print(uyeler)

# sayıları sıralamak için de kullanabiliriz
# ters sıralamak istersek sort() metodunun reverse parametresini kullanacağız
uyeler.sort(reverse=True)
print(uyeler)
# reverse parametresinin öntanımlı değeri False’tur. Yani sort() metodu öntanımlı olarak öğeleri artıra artıra sıralar. Öğeleri azalta azalta
# sıralamak için reverse parametresinin False olan öntanımlı değerini True yapmamız yeterli olacaktır
# *listelerin sort() metodu da Türkçe karakterleri düzgün sıralayamaz.


# index() = Bu metot bir liste öğesinin liste içindeki konumunu bize söyler
print(uyeler.index("Kemal"))


# count() = bir öğenin o veri tipi içinde kaç kez geçtiğini söyler
renk = ["kırmızı","mavi","mor","sarı","mavi","beyaz"]
print(renk.count("mavi"))


# copy() = listeleri, birbirlerini etkilemeyecek şekilde kopyalamak için
boya = renk.copy()
print(boya)


# clear() = görevi bir listenin içeriğini silmektir.
renk.clear()
print(renk)   # [] çıktısı verir (boş liste)



# Demetlerin metotları
# index() = bir demet öğesinin demet içindeki konumunu bize söyler 
demet = ("elma", "armut", "çilek", "elma")
print(demet.index("armut"))


# count() = count() metodu da bir öğenin o veri tipi içinde kaç kez geçtiğini söyler
print(demet.count("elma"))
