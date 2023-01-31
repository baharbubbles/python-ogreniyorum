# karakter dizilerini alfabe sırasına dizme
print(*sorted("kitap"), sep="")

for i in sorted("dolap"):
  print(i, end="")

# karakter dizisi üzerinde değişiklik yapma
# -adreslerin her birinin baş tarafına http:// ifadesini ekleme
site1="www.google.com"
site2="www.yahoo.com"
site3="www.gnu.com"
for i in site1,site2,site3:
    print("http://", i, sep="")  
    #print("http://", i[4:], sep="") =>  www. kısımlarını atmak isterseniz karakter dizisi birleştirme işlemleri ile birlikte
    #dilimleme yöntemini de kullanmanız gerekir

# Python’da bir karakter dizisini bir kez tanımladıktan sonra bu karakter dizisi üzerinde artık değişiklik yapamazsınız.
# Eğer bir karakter dizisi üzerinde değişiklik yapmanız gerekiyorsa, yapabileceğiniz tek şey
# o karakter dizisini yeniden tanımlamaktır.  =>>  kardiz = "İ" + kardiz[1:]