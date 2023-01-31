# format() Metodu ile Biçimlendirme (Yeni Yöntem)
print("{} ve {} iyi bir ikilidir!".format("Django", "Python"))
# Küme parantezleri içinde sayı kullanabilme imkanı sayesinde değerlerin sırasını istediğiniz gibi düzenleyebilirsiniz
print("{1} {0}".format("bahar","ırmak"))
# {:<Q} sağa yaslama, {:>Q}sola yaslama, {:^Q}ortalama. hizalama işlemleri bu şekilde yapılır. Q, hizalama işleminin Q (yerine girilen sayı) 
# karakterlik bir alan ile ilgili olduğunu söylüyor
for sıra, karakter in enumerate(dir(str)):
    if sıra % 3 == 0:
        print("\n", end="")
    print("{:<20} ".format(karakter), end="")

# {:s}, karakter dizilerini temsil eder. format() metodunun alabileceği parametreyi karakter dizisiyle sınırlandırmış oluruz.
# {:c}, 0 ile 256 arası sayıların ASCII tablosundaki karşılıklarını temsil eder.
# {:d}, sayıları temsil eder.
# {:o}, onlu düzendeki sayıları sekizli düzendeki karşılıklarına çevirir
# {:x} ve {:X}, onlu düzendeki sayıları onaltılı düzendeki karşılıklarına çevirir
# {:b}, onlu düzendeki sayıları ikili düzendeki karşılıklarına çevirir
# {:f}, float sayıları temsil eder. default olarak virgülden sonra 6 basamak vardır. {:.2f} yaparak virgülden sonra 2 basamak gösterebiliriz
# {:,}, : işaretini , işareti (basamak ayracı) ile birlikte kullanarak, sayıları basamaklarına ayırabilirsiniz
print("{:,} ".format(1234567890))