# str.maketrans(), translate()
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"
cevir = str.maketrans(kaynak, hedef) #str.maketrans() metodu kaynak ve hedef karakter dizilerini alıp bunları birleştirerek
# bize bir sözlük veri tipinde bir nesne veriyor.
metin = "Bildiğiniz gibi bazı internet sitelerinde Türkçe karakterler desteklenmiyor."
print(metin.translate(cevir))
# maketrans() metodunu boş bir karakter dizisi üzerine de uygulayabilirsiniz. Neticede maketrans() karakter 
# dizilerinin bir metodudur. Bu metot hangi karakter dizisi üzerine uygulandığıyla değil, parametre olarak hangi 
# değerleri aldığıyla (bizim örneğimizde kaynak ve hedef) ilgilenir.

# isalpha()
# Bu metot yardımıyla bir karakter dizisinin ‘alfabetik’ olup olmadığını denetleyeceğiz. Eğer bir karakter dizisi içinde yalnızca 
# alfabe harﬂeri (‘a’, ‘b’, ‘c’ gibi. . . ) varsa o karakter dizisi için ‘alfabetik’ diyoruz

# isdigit()
# Bu metot da isalpha() metoduna benzer. Bunun yardımıyla bir karakter dizisinin sayısal olup olmadığını denetleyebiliriz. 
# Sayılardan oluşan karakter dizilerine ‘sayı değerli karakter dizileri’ adı verilir

# isalnum()
# sayı ve/veya harﬂerden oluşan karakter dizilerine alfanümerik karakter dizileri adı verilir

# isdecimal()
# Bu metot yardımıyla bir karakter dizisinin ondalık sayı cinsinden olup olmadığını denetliyoruz.
print("12.4".isdecimal()) # false çıktısı verir çünkü 12.4 float bir değerdir

# isidentifier()
# değişkenler birer tanımlayıcıdır. Dolayısıyla bir değişken adının geçerli olup olmadığını isidentifier() metodu yardımıyla denetleyebiliriz
print("1a".isidentifier())  # false çıktısı alıyoruz. değişkenler sayı ile başlayamaz çünkü

# isnumeric()
# Bu metot bir karakter dizisinin nümerik olup olmadığını denetler. Yani bu metot yardımıyla
# bir karakter dizisinin sayı değerli olup olmadığını denetleyebiliriz
print("1234".isnumeric())

# isspace()
# Eğer karakter dizimiz boşluklardan oluşuyorsa bu metot True çıktısı verecek, ama eğer karakter dizimizin içinde bir tane bile 
# boşluk harici karakter varsa bu metot False çıktısı verecektir
print("   ".isspace())

# isprintable()
# ekranda görünmeyen karakterlere(\n, \t, \r) ‘basılmayan karakterler’ (non-printing characters) adı verilir. 
# ‘b’, ‘c’, ‘z’, ‘x’, ‘=’, ‘?’, ‘!’ ve benzeri karakterler ise ‘basılabilen karakterler’ (printable characters) olarak adlandırılır
# bu metot bir karakterin basılabilen bir karakter mi yoksa basılmayan bir karakter mi olduğunu söyler
print("\n".isprintable())  # false çıktısı alırız çünkü \n çıktıda görünmez 

