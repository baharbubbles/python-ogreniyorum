# replace() metodu
kardiz ="elma"
kardiz=kardiz.replace("e","E") # 2 parametre kullanarak (eski karakter dizisi, yeni karakter dizisi)
print(kardiz)

#kardiz ="memleket"
#kardiz=kardiz.replace("e","",1) # 3 parametre kullanarak (eski kardiz, yeni kardiz, kardiz içindeki karakterlerin kaç tanesinin değiştirileceği)
#print(kardiz)
#replace() metodunu üçüncü bir parametre ile birlikte kullandık. Üçüncü parametre
#olarak 1 sayısını verdiğimiz için replace() metodu sadece tek bir “e” harﬁni sildi.

# split(), rsplit(), splitlines() metotları
# 1-split() 
# Bu metodun görevi karakter dizilerini belli noktalardan bölmektir
kardiz="İstanbul Büyükşehir Belediyesi"
for i in kardiz.split():
   print(i)

kardiz= input("kısaltmasını öğrenmek istediğiniz kıurumun ismini yazınız: ")
for i in kardiz.split():
    print(i[0], end="")
# split() metodunu bu şekilde parametresiz olarak kullandığımızda bu metot karakter dizilerini bölerken boşluk
# karakterini ölçüt alacaktır. Yani karakter dizisi içinde karşılaştığı her boşluk karakterinde bir bölme işlemi uygulayacaktır.

# 2-rsplit()
# split() ile rsplit() arasındaki tekfark, split() metodunun karakter dizisini soldan sağa, rsplit() metodunun ise sağdan sola
# doğru okumasıdır. rsplit() metodu pek yaygın kullanılan bir metot değildir.

# 3-splitlines() metodu
# splitlines() metodunu bir karakter dizisini satır satır ayırmak için kullanabiliriz.

# lower() metodu
#lower() metodu, karakter dizisindeki bütün harﬂeri küçük harfe çeviriyor.
kardiz="bAhAR"
kardiz=kardiz.lower()
print(kardiz)

iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"
iller = iller.replace("I", "ı").replace("İ", "i").lower() # replace() metotları I'yı ı, İ'yi i ile değiştirdi; 
# lower() metotu ile de kalan harfleri küçülttük
print(iller)