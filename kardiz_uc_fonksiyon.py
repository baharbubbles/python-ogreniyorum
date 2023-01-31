# Bu fonksiyonlar sadece karakter dizileri ile değil, başka veri tipleri ile çalışırken de işlerimizi bir hayli kolaylaştıracak.

# 1- dir()
#Bu metot bize Python’daki bir nesnenin özellikleri hakkında bilgi edinme imkanı verecek.


# 2- enumerate()
# yazdığınız bir programda numaralandırmaya ilişkin işlemler yapmanız gerekiyorsa bu metot faydalı olacaktır
# kendisine parametre olarak verilen değer hakkında bize iki farklı bilgi verir: Bir öğe ve bu öğeye ait bir sıra numarası.
for i in enumerate("istihza"):
    print(i)

# enumerate() fonksiyonu numaralandırmaya 0’dan başlıyor. isterseniz değiştirebilirsiniz :
for sıra, harf in enumerate("istihza", 1):
    print(sıra, harf)

# 3- help()
# Python’la ilgili herhangi bir konuda yardıma ihtiyacınız olduğunda. Bu fonksiyonu iki farklı şekilde kullanıyoruz:
# etkileşimli kabuta help() diyerek özel bir yardım sayfası açarak 'help>' yardımı ile örn: help>dir diyerek dir'in 
# ne işe yaradığını öğrenebiliyoruz
# İkincisi ise doğrudan etkileşimli kabukta şu komutu kullanmaktır: örn: help(dir)  diyerek doğrudan dir hakkında bilgi alabiliriz
   