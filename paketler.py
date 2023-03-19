# paketler modüllere kıyasla çok daha kapsamlı bir yapıdır. Zira bir paket içinde (genellikle) birden fazla modül bulunur.
# bütün paketler aynı zamanda birer modüldür, ancak bütün modüller birer paket değildir. paketlerin __path__ adlı özel bir niteliği bulunur. Modüllerde ise bu nitelik
# bulunmaz.

# Standart Paketler
# Standart paketlere Python kurulum dizini içindeki Lib klasöründen erişebilirsiniz. Bir standart paketin tam olarak hangi konumda bulunduğunu öğrenmek için ise
# ilgili paketin __path__ niteliğini sorgulayabilirsiniz.

# Üçüncü Şahıs Paketleri

# Paketlerin İçe Aktarılması
# 1.import paket
import urllib # ancak bu her modülü import ettirmez o yüzden;

# 2.import paket.modül
import urllib.request  # modül içindeki nitelik ve metotlara urllib.request önekiyle erişebiliriz

# 3.from paket import modül
# urllib.request ismi altında içe aktarıldığından, urllib paketi içindeki request modülünün nitelik ve metotlarına ulaşabilmek için her defasında urllib.request önekini
# kullanmamız gerekir. Eğer her defasında uzun uzun urllib.request yazmak istemiyorsanız paket içindeki modülü şu şekilde içe aktarabilirsiniz:
from urllib import request
# Böylece request modülünün nitelik ve metotlarına yalnızca request önekiyle erişebilirsiniz.

# 4.from paket.modül import nitelik_veya_metot
# bir paket içinde yer alan herhangi bir modül içindeki nitelik ve metotlara öneksiz olarak erişmek için:
from urllib.request import urlopen
# metodu dümdüz kullanabiliriz = örn: urlopen('https://yazbel.com/')

# 5.from paket.modül import *
# Eğer bir paket içindeki bir modülün bütün nitelik ve metotlarını mevcut isim alanına olduğu gibi aktarmak isterseniz:
from urllib.request import *


# Paket Oluşturmak
# Program kodlarını içeren .py dosyasını bir klasör içine koyduğunuz anda, o klasörün adını taşıyan bir paket meydana getirmiş olursunuz.
import siparis_takip
print(dir(siparis_takip))
# listede __path__ adlı bir nitelik var. Bu niteliğin yalnızca paketlerde bulunduğunu biliyorsunuz. Demek ki siparistakip gerçekten de bir Python paketiymiş. 
# Bunun dışında, listede gördüğünüz __package__ niteliğini kullanarak da bir modülün paket olup olmadığını kontrol edebilirsiniz
print(siparis_takip.__package__)  # Eğer test ettiğimiz modül bir paketse, __package__ niteliği bize bir paket adı verecektir.

# İçe Aktarma
from siparis_takip import komut
print(komut)

from siparis_takip.komut import komut
print(komut)


# İçe Aktarma Mantığı











