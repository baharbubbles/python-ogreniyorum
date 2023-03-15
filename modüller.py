# Hazır modüller
# Hazır modüller kendi içinde ikiye ayrılabilir:
# 1. Standart Kütüphane Modülleri = doğrudan Python geliştiricileri tarafından yazılıp dile kaynaştırılmış modüllerdir.
# 2. Üçüncü Şahıs Modülleri = 

# Modüllerin içe aktarılması: İçe aktarmak, bir modül içindeki fonksiyon ve nitelikleri başka bir program (veya ortam) içinden kullanılabilir hale getirmek demektir.
# import modül_adı komutuyla içe aktarma yapmadan modülün fonksiyon veya niteliklerine erişemeyiz!!

# Farklı İçe Aktarma Yöntemleri
# 1.import modül_adı as farklı_isim = Modülü hangi adla içe aktaracağınız tamamen size kalmış

# subprocess modülü, harici komutları Python içinden çalıştırabilmemizi sağlayan oldukça faydalı bir araçtır. Bu modülü kullanarak Python programlarımızın içinden başka
# programları çalıştırabiliriz.
import subprocess
import subprocess as sp
# webbrowser modülü, bilgisayarımızda kurulu internet tarayıcısını kullanarak internet sitelerini açabilmemizi sağlar.
import webbrowser
import webbrowser as br


# 2.from modül_adı import isim1, isim2
import os 
# import os gibi bir komutla bütün o isimleri içe aktarmak yerine, yalnızca kullanacağınız isimleri içe aktarmayı tercih de edebilirsiniz.
from os import name
print(name)  # print(os.name) dersek hata verir Çünkü biz from os import name komutunu verdiğimizde, os modülünü değil, bu modül içindeki bir nitelik olan name’i içe aktarmış oluyoruz.

from os import name, listdir, getcwd
# Bu komutla os modülü içinden yalnızca name niteliğini, listdir() fonksiyonunu ve getcwd() fonksiyonunu aktarmış olduk


# 3.from modül_adı import isim as farklı_isim  = **Yalnız bu yöntem çok sık kullanılmaz.
from os import listdir as ld


# 4.from modül_adı import *  = Ancak bu yöntem pek tavsiye edilmez. Çünkü bu şekilde, modül içindeki bütün isimleri kontrolsüz bir şekilde mevcut ortama ‘boşaltmış’ oluyoruz.
# (bu yönteme ‘yıldızlı içe aktarma’ diyebilirsiniz). Bu şekilde bir modül içindeki bütün fonksiyon ve nitelikleri içe aktarmış oluruz (ismi _ ile başlayanlar hariç)
from sys import *
print(version)
# Böylece sys modülü içindeki bütün fonksiyon ve nitelikleri, başlarına modül adını(sys.version gibi) eklemeye gerek olmadan kullanabiliriz

# Mesela eğer modül bu şekilde içe aktarılmadan önce version diye başka bir değişken tanımlamışsanız, modül içe aktarıldıktan sonra, önceden tanımladığınız bu version değişkeninin değeri kaybolacaktır:
version = "1.0"
print(version)
from sys import * 
print(version)  # sys modülünün içindeki version niteliği bizim önceden tanımladığımız version değişkeniyle çakıştı ve herhangi bir uyarı vermeden, bizim tanımladığımız version
# değerini silip kendi version değerini bizimkinin yerine geçirdi
# ** Bir modülü yıldızlı olarak içe aktaracaksak, bu işlemi lokal etki alanları içinden gerçekleştiremeyiz.
#def fonk():
#    from os import *      # yazamayız kod direk hata verir çalışmaz. bu yıldızlı içe aktarmanın istisnasıdır!1

from os import *
def fonk():
    print("doğru kullanımı bu şekilde yani globalde içe aktarılır")
# Yıldızlı içe aktarma işlemleri ancak modül seviyesinde, yani global isim alanında gerçekleştirilebilir. Dolayısıyla yukarıdaki içe aktarma işlemini ancak fonksiyonun
# dışında gerçekleştirebiliriz!



# Kendi Tanımladığımız Modüller
# Programınız da .py uzantılı bir metin dosyası içinde yer alıyor. İşte bütün bu öğeleri ve veri tiplerini içeren .py uzantılı dosyaya ‘modül’ adı verilir. Yani şimdiye kadar
# yazdığınız ve yazacağınız bütün Python programları aynı zamanda birer modül adayıdır.


# modüllerin yolu:
# Kütüphane modüllerini her yerden içe aktarabiliyoruz. Yani, komut satırını çalıştırdığımız her konumda veya program dosyamızın bulunduğu her dizin altında bu modülleri rahatlıkla
# kullanabiliyoruz.
# Ama kendi yazdığımız modülleri içe aktarabilmemiz için, bu modüllerin o anda içinde bulunduğumuz dizin altında yer alması gerekiyor.

# kendi modüllerimizi de her yerden içe aktarabilmek istersek:
# Bunun için iki seçeneğimiz var: Birincisi, modülün yolunu sys.path listesine ekleyebiliriz. İkincisi, modülümüzü sys.path içinde görünen dizinlerden birine kopyalayabilir veya
# taşıyabiliriz.
# - sys.path komutunun çıktısı aslında basit bir listeden başka bir şey değildir. Dolayısıyla Python’da liste adlı veri tipi üzerinde ne tür işlemler yapabiliyorsanız, sys.path
# üzerinde de aynı şeyleri yapabilirsiniz.
# - ikinci yönteminin, ilgili modül dosyasını sys.path çıktısında görünen dizinlerden herhangi birine kopyalamak olduğunu söylemiştik. Dolayısıyla, sys.path çıktısına bakıp, modül dosyanızı 
# orada görünen dizinlerden herhangi biri içine kopyalayabilirsiniz. Yaygın olarak tercih edilen konum, Python kurulum dizini içindeki site-packages adlı dizindir.
# dizinin yerini tespit için: from distutils import sysconfig  >>> sysconfig.get_python_lib()

# **Python, içe aktarmak istediğimiz bir modülü bulabilmek için dizinleri ararken sys.path listesindeki dizin adlarını 'soldan sağa doğru' okur. Modül dosyasını bulduğu anda da arama işlemini sona erdirir
# ve modülü içe aktarır.


# modüllerde değişiklik yapmak:
# Tıpkı kütüphane modüllerini işlerken yaptığımız gibi, dir() fonksiyonundan yararlanarak, içe aktardığımız bu modül içindeki kullanılabilir fonksiyon ve nitelikleri görebilirsiniz

# etkileşimli kabukta modül bir kez içe aktarıldıktan sonra, o modülde yapılan değişikliklerin otomatik olarak etkinleşmez. Yani değişikliklerin etkileşimli kabukta etkinleşebilmesi için o modülü 
# yeniden yüklememiz lazım. Bunu iki şekilde yapabiliriz:
# Birincisi, etkileşimli kabuğu kapatıp yeniden açtıktan sonra import sözlük komutuyla sözlük modülünü tekrar içe aktarabiliriz.
# İkincisi, importlib adlı bir kütüphane modülünden yararlanarak kendi modülümüzün tekrar yüklenmesini sağlayabiliriz:
# import importlib
# importlib.reload()
# importlib modülünün reload() fonksiyonu, bir modüle yeni eklenen öğeleri yeniden yükleyerek, bunların etkileşimli kabukta kullanılabilir hale gelmesini sağlar.
# Eğer bir modüldeki bazı nitelik veya fonksiyonları silerseniz, importlib modülünün reload() fonksiyonu ile bu modülü yeniden yükledikten sonra bile bu nitelik ve fonksiyonlar önbellekte
# tutulmaya devam eder.



# Üçüncü Şahıs Modülleri
# Üçüncü şahıs modülleri, başka Python programcıları tarafından yazılıp hizmetimize sunulmuş programlardır. Bu yönüyle bunlar kütüphane modüllerine çok benzer. Ama bu ikisi arasında
# önemli bir fark bulunur: Kütüphane modülleri Python programlama dilinin bir parçasıdır. Dolayısıyla kütüphane modüllerini kullanmak için herhangi bir ek yazılım indirmemiz gerekmez. 
# Üçüncü şahıs modülleri ise dilin bir parçası değildir. Bu modülleri kullanabilmek için, öncelikle bunları modül geliştiricisinin koyduğu yerden bilgisayarımıza indirmemiz gerekir.

# Örneğin amacınız Django adlı üçüncü şahıs modülünü kurmak ise bu modülü şu komut ile kurabilirsiniz:
# pip3 install django  ***(terminalde bu komutu vermeliyiz burada değil!)


# Modüllerin Özel Nitelikleri
modüller = ["os", "sys", "random"]
def kesisim_bul(modüller):
    kümeler = [set(dir(__import__(modül))) for modül in modüller]
    return set.intersection(*kümeler)
print(kesisim_bul(modüller))

# Bir gömülü fonksiyon olan __import__ fonksiyonu, modül adlarını içeren karakter dizilerini kullanarak, herhangi bir modülü içe aktarmamızı sağlayan bir araçtır.
# 1)__doc__ Niteliği
# Teknik dilde, üç tırnak içinde gösterilen karakter dizilerine belge dizisi (docstring) veya belgelendirme dizisi (documentation string) adı verilir. Modüllerin __doc__ niteliğini
# kullanarak, bir modül dosyasının en başında bulunan belgelendirme dizilerine erişebiliriz.

# 2)__name__ Niteliği
# Python’daki herhangi bir modülü içe aktardıktan sonra bu modül üzerine dir() fonksiyonunu uygularsanız, istisnasız her modülün __name__ adlı bir niteliği olduğunu görürsünüz.
# __name__ niteliği iki farklı değer alabilir: İçinde bulunduğu modülün adı veya "__main__" adlı özel bir değer.
# Eğer bir Python programı başka bir program içinden modül olarak içe aktarılıyorsa, __name__ niteliğinin değeri o modülün adı olacaktır.
# Eğer bir Python programı doğrudan bağımsız bir program olarak çalıştırılıyorsa, __name__ niteliğinin değeri bu defa "__main__" olacaktır.

# 3)__loader__ Niteliği
# Bu nitelik, ilgili modülü içe aktaran mekanizma hakkında bize çeşitli bilgiler veren birtakım araçlar sunar. __loader__, günlük olarak kullanacağımız bir araç değil. Eğer yazdığınız 
# kodlarda bu niteliğin sunduğu olanaklara ihtiyaç duyarsanız, doğrudan bu nitelik yerine pkgutil adlı bir modülü kullanabilirsiniz.

# 4)__spec__ Niteliği
# __spec__ niteliği de bize modüller hakkında çeşitli bilgiler sunan birtakım araçları içinde barındırır. Mesela bir modülün ad ve konum bilgilerine ulaşmak için bu niteliği kullanabiliriz:
import subprocess
adı = subprocess.__spec__.name
konumu = subprocess.__spec__.origin
print(adı)
# ** Tıpkı __loader__ gibi, bu nitelik de günlük olarak kullanacağımız bir araç değil.

# 5)__package__ Niteliği



