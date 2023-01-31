# upper() metodu
# lower() metodunun yaptığı işin tam tersini yapar. upper() metodu bu harﬂeri büyütmemizi sağlar.
iller = "istanbul, izmir, siirt, mersin"
iller = iller.replace("i", "İ").upper()  #önce karakter dizisi içinde geçen ‘i’ harﬂerini ‘İ’ ile değiştiriyoruz.
#Öteki harﬂeri de büyütebilmek için karakter dizisine upper() metodunu uyguluyoruz.
print(iller)

# -> programlamada çok kullanılan iki metot = isupper(), islower()
# islower() metodu
# lower() metodu bir karakter dizisini tamamen küçük harﬂerden oluşacak şekle getiriyordu. islower() metodu ise 
# bir karakter dizisinin tamamen küçük harﬂerden oluşup oluşmadığını sorguluyor.
veri = input("Adınız: ")
if not veri.islower():
  print("Lütfen isminizi sadece küçük harflerle yazın")

# isupper() metodu
# isupper() metodu da islower() metodunun yaptığı işin tam tersini yapar.isupper() metodu ise bir karakter dizisinin 
# tamamen büyük harﬂerden oluşup oluşmadığını sorguluyor.
kardiz = "İSTİHZA"
print(kardiz.isupper())  # true cevabı geliyor. İSTİHZA kelimesi büyük harflerden oluştuğu için

# endswith()
# Bu metodun görevi karakter dizisinin durumunu sorgulamaktır.
# Bu metot yardımıyla bir karakter dizisinin hangi karakter dizisi ile bittiğini sorgulayabiliyoruz.
kardiz = "istihza"
print(kardiz.endswith("b"))  # istihza kelimesinin b harfi ile bittiğini sorguladım. a harfiyle bittiği için false cevabını verdi

d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"
for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
    if i.endswith("mp3"):
        print(i)
# endswith() metodu özellikle dosya uzantılarına göre dosya türlerini tespit etmede oldukça işe yarar bir metottur.

# startswith() metodu
# startswith() metodu ise bir karakter dizisinin hangi karakter veya karakterlerle başladığını denetler.
d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"
for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
    if i.startswith("p"):  #Burada ‘p’ harﬁyle başlayan bütün dosyaları listeledik.
        print(i)