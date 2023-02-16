# keys() = sözlüklerin anahtar-değer çiftlerinden oluşan bir veri tipi olduğunu söylemiştik. Bir sözlüğü normal yollardan ekrana yazdırırsanız 
# size hem anahtarları hem de bunlara karşılık gelen değerleri verecektir. Ama eğer bir sözlüğün sadece anahtarlarını almak
# isterseniz keys() metodundan yararlanabilirsiniz
sozluk = {"a":1,
          "b":2,
          "c":3,
          "d":4}
print(sozluk.keys()) # dict_keys(['a', 'b', 'c', 'd']) şeklinde bir dict_keys nesnesi verir. Bu nesneyi programda kullanabilmek için bunu, listeye,
# demete veya karakter dizisine dönüştürebiliriz.
demet = tuple(sozluk.keys())
print(demet)
kardiz = ",".join(sozluk.keys())  # Eğer sözlük anahtarlarını str() fonksiyonu yardımıyla karakter dizisine dönüştürmeye kalkışırsanız beklemediğiniz bir çıktı alırsınız.
print(kardiz)



# values() = keys() metodu bir sözlüğün anahtarlarını veriyor. Bir sözlüğün değerlerini ise values() metodu verir
print(sozluk.values()) # bu metottan bir dict_values nesnesi alıyoruz. Tıpkı keys() metodunda olduğu gibi, values() metodunda da bu çıktıyı başka veri tiplerine 
# dönüştürme imkanına sahibiz
liste = list(sozluk.values())
print(liste)

#**Yalnız bu verileri karakter dizisine dönüştürmeye çalıştığınızda ufak bir problemle karşılaşacaksınız. Bunun sebebi sözlükteki değerlerin 'int'
# tipinde olmasıdır
kardiz = ",".join([str(i) for i in sozluk.values()])
print(kardiz)  # sözlükteki değerlerin her birini, tek bir liste üreteci içinde karakter dizisine dönüştürdük ve ortaya çıkan listeyi karakter dizilerinin 
# join() metodu yardımıyla kardiz adlı bir karakter dizisi içine yerleştirdik



# items() = Bu metot, bir sözlüğün hem anahtarlarını hem de değerlerini aynı anda almamızı sağlar
print(sozluk.items())
# dict_items([('a', 0), ('c', 2), ('b', 1)]) çıktısını verir. Tek bir liste içinde ikili demetler halinde hem anahtar hem de değeri barındırır

# Bu metot sıklıkla for döngüleri ile birlikte kullanılarak bir sözlüğün anahtar ve değerlerinin manipüle edilebilmesini sağlar:
for anahtar,deger in sozluk.items():
    print("{} = {}".format(anahtar,deger))



# get() = get() metodu, parantez içinde iki adet argüman alır. Birinci argüman sorgulamak istediğimiz sözlük öğesidir. İkinci argüman ise bu öğenin 
# sözlükte bulunmadığı durumda kullanıcıya hangi mesajın gösterileceğini belirtir
ing_sozlük = {"kitap":"book", "kalem":"pencil", "silgi":"eraser"}
sorgu = input("Karşılığını merak ettiğiniz kelimeyi yazınız: ")
#print(ing_sozlük[sorgu])
# kullanıcı sözlükte yer almayan bir kelime aradığında, for döngüsü gibi işlevi az bir alternatif yerine get() metodunu kullanıcaz
print(ing_sozlük.get(sorgu,"Bu kelime sözlükte bulunmamaktadır!"))

# hava durumu programı yazalım:
soru = input("hava durumunu öğrenmek istediğiniz şehrin ismini küçük harflerle yazın: ")
cevap = {"istanbul":"çok bulutlu", "ankara":"kar yağışlı", "antalya":"çok güneşli", "izmir":"parçalı bulutlu"}
print(cevap.get(soru, "Bu şehre ilişkin hava durumu bilgisi bulunmamaktadır!"))



# clear() = Görevi sözlükteki öğeleri temizlemektir.Yani içi dolu bir sözlüğü bu metot yardımıyla tamamen boşaltabiliriz
sozluk.clear()
print(sozluk)   # {} boş bir sözlüğümüz kaldı. Sözlüğü silmedik, bellekte hala sözlük var
# sözlüğün kendisini silmek için ** del parçacığından yararlanıyoruz: del sozluk dediğimizde bellekten silinir



# copy() 
hava_durumu = {"istanbul":"çok bulutlu", "ankara":"kar yağışlı", "antalya":"çok güneşli", "izmir":"parçalı bulutlu"}
# yedek_hava_durumu = hava_durumu -> dersek yaptığımız değişiklik her iki sözlükte de görünür. bunu istemiyorsak:
yedek_hava_durumu = hava_durumu.copy()
hava_durumu["mersin"] = "sisli"
print(hava_durumu)
print(yedek_hava_durumu)   # mersin diye ekleme yapmamız burada görünmeyecek 



# fromkeys() = Bu metot mevcut sözlük üzerinde işlem yapmaz*. fromkeys() ’in görevi yeni bir sözlük oluşturmaktır. Bu metot yeni bir sözlük
# oluştururken listeler veya demetlerden yararlanır.
eleman = "ahmet", "mehmet", "koray"
adres = dict.fromkeys(eleman, "ısparta")
print(adres)
# “eleman” adlı bir demet tanımladık. Daha sonra da “adres” adlı bir sözlük tanımlayarak, fromkeys() metodu yardımıyla anahtar olarak “eleman”
# demetindeki öğelerden oluşan, değer olarak ise "ısparta"yı içeren bir sözlük meydana getirdik.



# pop() = metodun parantezi içinde mutlaka bir sözlük öğesi belirtmeliyiz!
sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye"), "içecekler": ("su", "kola", "ayran")}
print(sepet.pop("meyveler"))  # Bu komut, sözlükteki “meyveler” anahtarını silecek ve sildiği bu öğenin değerini ekrana basacaktır.
print(sepet.pop("tatlılar", "Silinecek öğe yok!")) # silmeye çalıştığımız anahtar sözlükte yok ise bu şekilde oluşturabiliriz



# popitem() = popitem() metodu da bir önceki bölümde öğrendiğimiz pop() metoduna benzer. Ancak pop() metodu parantez içinde bir parametre
# alırken, popitem() metodunun parantezi boş, yani parametresiz olarak kullanılır. Bu metot bir sözlükten son eklenen öğeyi silmek için kullanılır
print(sepet.popitem())  # eğer sözlük boş ise KeyError hata mesajı verir



# setdefault() 
yemek = {"meyve": ("erik","kiraz"), "sebze": ("domates","marul")}
yemek.setdefault("içecek",("su","ayran"))
print(yemek)  # içecek adlı bir anahtar oluşturduk sözlükte
yemek.setdefault("meyve",("badem","üzüm"))
print(yemek)  # zaten var olan bir meyve anahtarı bulunduğu için aynı adı taşıyan ama değerleri farklı olan yeni bir anahtar tanımlamadı
# Demek ki bu metot yardımıyla bir sözlük içinde arama yapabiliyor, eğer aradığımız anahtar sözlükte yoksa, setdefault() metodu içinde belirttiğimiz özellikleri
# taşıyan yeni bir anahtar-değer çifti oluşturabiliyoruz.



# update() = Bu metot yardımıyla oluşturduğumuz sözlükleri yeni verilerle güncelleyeceğiz
stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}
# stoğumuz değişti ve mal giriş-çıkışı oldu:
yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}
stok.update(yeni_stok)
print(stok)  # yeni stok bilgileri ekrana basılır.

