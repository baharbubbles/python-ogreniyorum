# % işareti ile biçimlendirme, karakter dizisi biçimlendirmenin eski yöntemidir.
parola = input("parola: ")
print("Girilen parola(%s) kurallara uygundur!" %parola)

print("%s ve %s iyi bir ikilidir." %("Python", "Django"))

yer = "yemeksepeti"
print("%s'nin internet adresi www.%s.com'dur." %(yer,yer))

for i in range(5):
    print("%%%s" %i)  # sayının başına yüzde(%) işareti koyabilmek için %%%s olarak 3 tane '%' yazılır.

sayfa = """
<html>
    <head>
        <title> %(dil)s </title>
    </head>
    <body>
        <h1> %(dil)s </h1>
        <p>Web sitemize hoşgeldiniz! Konumuz: %(dil)s </p>
    </body>
</html>
"""
print(sayfa % {"dil": "Python Programlama Dili"}) # % ile s'nin arasına değişken koyarak aynı olan boşlukları bu şekilde doldurabiliriz
# "%(değişken_adı)s " % {"değişken_adı": "değişken_değeri"}

# biçimlendirme karakterleri
# % sabit, s ise değişkendir. Yani % sabit değerini bazı harﬂerle birlikte kullanarak,
# farklı karakter dizisi biçimlendirme işlemleri gerçekleştirebiliriz. s karakteri string, yani ‘karakter dizisi’
# %d, d harﬁ sayıları temsil eder. d harﬁ aslında tam sayı (integer) değerleri temsil eder. float değer verilirse int'e çevirerek çıktı verir
print("Şubat ayı 4 yılda bir %d gün olur." %29)
# %i, integer, yani ‘tam sayı’ kelimesinin kısaltmasıdır. Kullanım ve işlev olarak, d harﬁnden hiç bir farkı yoktur.
# %o, octal. sekizli düzendeki sayıları temsil eder. Dolayısıyla bu harﬁ kullanarak onlu düzendeki bir sayıyı sekizli düzendeki
# karşılığına dönüştürebilirsiniz. 
# %x, hexadecimal. Buradaki ‘x’ küçük harf olarak kullanıldığında, onaltılı düzende harﬂe gösterilen sayılar da
# küçük harﬂe temsil edilecektir
print("%i sayısının onaltılık karşılığı %x'dir." %(10,10))  
# %X ile harf karşılıkları büyük olur
# %f, ﬂoat, yani ‘kayan noktalı sayı’ kelimesinin kısaltmasıdır.
print("%f" %10) # Python’da bir karakter dizisi içindeki sayıyı %f yapısı ile kayan noktalı sayıya çevirdiğimizde
# noktadan sonra öntanımlı olarak 6 hane yer alacaktır
print("%.2f" %10)  # .2 ile virgülden sonra kaç basamak göstereceğini belirledik
# %c, Python’daki önemli karakter dizisi biçimlendiricilerinden biridir. Bu harf 'tek bir karakteri' temsil eder. c harﬁnin bir başka özelliği de 
# ASCII tablosunda sayılara karşılık gelen karakterleri de gösterebilmesidir.


for sıra, karakter in enumerate(dir(str)):
   if sıra % 3 == 0:             #
      print("\n", end="")        # Şu satırlar yardımıyla tablodaki sütun sayısını 3 olarak belirledik  
   print("%-20s " %karakter, end="")

