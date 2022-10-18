
#Kullanıcıdan dairenin çapını girmesini istiyoruz.
çap = input("Dairenin çapı: ")
#Kullanıcının verdiği çap bilgisini kullanarak
#yarıçapı hesaplayalım. Buradaki int() fonksiyonu string olarak aldığımız çap
#bilgisini integer değere çevirerek matematiksel işleme tabi tutmamızı sağlıyo
yarıçap = int(çap) / 2
#pi sayımız sabit
pi = 3.14159
#Yukarıdaki bilgileri kullanarak artık
#dairenin alanını hesaplayabiliriz
alan = pi * (yarıçap **2)   # (değer)**sayı = değerin yazılan sayı kadar üssünü almak demek
#Son olarak, hesapladığımız alanı yazdırıyoruz
print("Çapı", çap, "cm olan dairenin alanı: ", alan, "cm2'dir")
