# index(), rindex()
# Karakterlerin, bir karakter dizisi içinde hangi sırada bulunduğunu öğrenmek için index() adlı bir metottan yararlanabiliriz.
# **Bu metodun özelliği, sorguladığımız karakterin, karakter dizisi içinde geçtiği ilk konumu vermesidir. 
kardiz = "adana"
print(kardiz.index("a"))  # 0 çıktısı alırız yani ilk a'nın indeksi
# metodun ikinci parametresi, Python’ın aramaya kaçıncı sıradan itibaren başlayacağını gösteriyor.
kardiz = "adana"
print(kardiz.index("a", 1))
# Python’ın, karakter dizisini soldan sağa doğru değil de, sağdan sola doğru okumasını da
# sağlayabilirsiniz. Bu iş için rindex() adlı bir metottan yararlanacağız

# find(), rfind()
# find() ve rfind() metotları tamamen index() ve rindex() metotlarına benzer. find() ve rfind() metotlarının görevi 
# de bir karakter dizisi içindeki bir karakterin konumunu sorgulamaktır
# *** index() ve find() metotlarının farkı; index'te karakter sorgulanırken o karakter bulunamazsa ValuError hatası verir,
# find ise -1 çıktısı verir. Bu iki metot çifti arasındaki tek fark budur.

# center()
# center() metodunu karakter dizilerini ortalamak için kullanabilirsiniz.
# center() metoduna verilen genişlik parametresi aslında bir karakter dizisinin toplam kaç karakterlik bir yer kaplayacağını gösteriyor.
kardiz = "python"
for i in range(1,20):
   # print(kardiz.center(i))
    print(kardiz.center(i, "-"))  # ikinci parametresi boşluğa koyulacak olan şeyi ifade ediyor

# rjust(), ljust()
# Bu metotlar da tıpkı bir önceki center() metodu gibi karakter dizilerini hizalama vazifesi görür. 
# rjust() metodu bir karakter dizisini sağa yaslarken, ljust() metodu karakter dizisini sola yaslar.
# kullanıcılarınıza göstereceğiniz çıktıların düzgün görünmesini sağlamak açısından oldukça faydalıdır.

# zfill()
# zfill() metodu yardımıyla karakter dizilerinin sol tarafına istediğimiz sayıda sıfır ekleyebiliriz
for i in range(11):
    print(str(i).zfill(2))
# **Burada str() fonksiyonunu kullanarak, range() fonksiyonundan elde ettiğimiz sayıları birer
# ** karakter dizisine çevirdiğimize dikkat edin. ***Çünkü zfill() karakter dizilerinin bir metodudur.

# partition(), rpartition()
# Bu metot yardımıyla bir karakter dizisini belli bir ölçüte göre üçe bölüyoruz
b = "ikramiye"
print(b.partition("i"))
print(b.rpartition("i"))  # bu sağdan sola okur kelimeyi

# encode()
# Bu metot yardımıyla karakter dizilerimizi istediğimiz kodlama sistemine göre kodlayabiliriz.
# Python 3.x’te varsayılan karakter kodlaması utf-8’dir. Eğer istersek şu karakter dizisini utf-8
# yerine cp1254 ile kodlayabiliriz

# expandtaps()
# Bu metot yardımıyla bir karakter dizisi içindeki sekme boşluklarını genişletebiliyoruz.
