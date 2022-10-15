
#Kullanıcıdan dairenin çapını girmesini istiyoruz.
çap = input("Dairenin çapı: ")
#Kullanıcının verdiği çap bilgisini kullanarak
#yarıçapı hesaplayalım. Buradaki int() fonksiyonunu
#ilk kez görüyoruz. Biraz sonra bunu açıklayacağız
yarıçap = int(çap) / 2
#pi sayımız sabit
pi = 3.14159
#Yukarıdaki bilgileri kullanarak artık
#dairenin alanını hesaplayabiliriz
alan = pi * (yarıçap * yarıçap)
#Son olarak, hesapladığımız alanı yazdırıyoruz
print("Çapı", çap, "cm olan dairenin alanı: ", alan, "cm2'dir")
