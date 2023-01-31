# capitalize() metodu
# görevi karakter dizilerinin yalnızca ilk harﬁni büyütmektir. 
# !!!-birden fazla kelimeden oluşan karakter dizilerine bu metodu uyguladığımızda bütün kelimelerin ilk harﬁ büyümez. 
# Yalnızca ilk kelimenin ilk harﬁ büyür.
kardiz = "İstanbul Büyükşehir Belediyesi"
if kardiz.startswith("i"):
    kardiz = "İ"+ kardiz[1:]
kardiz = kardiz.capitalize()
print(kardiz)

# title() metodu
# title() metodu da karakter dizilerinin ilk harﬁni büyütür. Ama capitalize() metodundan farklı olarak bu metot, 
# birden fazla kelimeden oluşan karakter dizilerinin her kelimesinin ilk harﬂerini büyütür.
a = "python programlama dili"
a = a.title()
print(a)
b = a.capitalize()
print(b)

kardiz = "on iki ada"
for kelime in kardiz.split():   # split() metodu "on iki ada" adlı karakter dizisini kelimelerine ayırıyor.İşte biz de kelimelerine 
    if kelime.startswith("i"):   # ayrılmış bu yapı üzerinde bir for döngüsü kurarak herbir öğenin ilkharﬁnin ‘i’ olup olmadığını kontrol edebiliyoruz.
        kelime = "İ" + kelime[1:]  
    
    kelime = kelime.title()
    print(kelime, end=" ")

# swapcase() metodu
# swapcase() metodu da büyük-küçük harﬂe ilgili bir metottur. Bu metot bir karakter dizisi içindeki 
# büyük harﬂeri küçük harfe; küçük harﬂeri de büyük harfe dönüştürür.
kardiz= "Python"
kardiz = kardiz.swapcase()
print(kardiz)

sehir ="istanbul"
for i in sehir:
    if i == "İ":
        sehir = sehir.replace("İ", "i")
    elif i == "i":
        sehir = sehir.replace("i", "İ")
    else:
        sehir = sehir.replace(i, i.swapcase())
print(sehir)
# bu kodlarda da ‘i’ ve ‘I’ harﬂerini tek tek kontrolden geçiriyoruz. Eğer bir karakter dizisi içinde bu iki harften biri varsa,
# bunların büyük harf veya küçük harf karşılıklarını elle yerine koyuyoruz. Bu karakterler dışında kalan karakterlere ise
# doğrudan swapcase() metodunu uygulayarak istediğimiz sonucu elde ediyoruz.


# casefold()
# Bu metot işlev olarak lower() metoduna çok benzer. Hatta Türkçe açısından, bu metodun lower() metodundan hiçbir farkı yoktur. 
# Almanca gibi dillerde alfabeleri için kullanılır.

