# strip(), lstrip(), rstrip() metotları
# 1-strip() metodu
isim = " bahar "  # ismin başında ve sonunda gereksiz boşluklar var
isim = isim.strip()  # bu boşlukları silecek
print(isim)
# strip() metodu yukarıdaki örnekte olduğu gibi parametresiz olarak kullanıldığında, bir karakter dizisinin 
# sağında veya solunda bulunan belli başlı karakterleri kırpar.
# strip() metodunun öntanımlı olarak kırptığı karakterler şunlardır:
# "" --> boşluk karakteri
# \t --> sekme oluşturan kaçış dizisi
# \n --> satır başına geçiren kaçış dizisi
# \r --> imleci aynı satırın başına döndüren kaçış dizisi
# \v --> düşey sekme oluşturan kaçış dizisi
# \f --> yeni bir sayfaya geçiren kaçış dizisi

kardiz = "python"
kardiz = kardiz.strip("p")
#"python".strip("p") şeklinde de yazılabilir
print(kardiz)
# !!!-Yalnız strip() metodunu kullanırken bir noktaya dikkat etmelisiniz. Bu metot bir karakter
# dizisinin hem başında, hem de sonunda bulunan karakterlerle ilgilenir.
kardiz = "kazak"
kardiz = kardiz.strip("k")
print(kardiz)

# 2-lstrip()
# lstrip() metodu bir karakter dizisinin sol tarafındaki gereksiz karakterlerden kurtulmamızı sağlar.
kardiz = "kazak"
kardiz = kardiz.lstrip("k")
print(kardiz)

# 3-rstrip()
#yalnızca sağ taraftaki karakteri uçurmak istemeniz halinde ise rstrip() metodundan yararlanacaksınız
kardiz = "kazak"
kardiz = kardiz.rstrip("k")
print(kardiz)


# join()
# join() metodunun görevi bölünmüş karakter dizisi gruplarını birleştirmektir. Bu metot görevini yerine getirirken,
# yani karakter dizisi gruplarını birleştirirken bir birleştirme karakterine ihtiyaç duyar.
kardiz = "Süleyman Demirel Üniversitesi"
böl = kardiz.split()
print(böl)
kardiz = " ".join(böl)  # buradaki " " karakteri birleştirme krakteridir. bu örnekte boşluk kullandık
print(kardiz)

kardiz = "bah ar"
bölünmüş = kardiz.split()
print(bölünmüş)
yeni = "".join(bölünmüş) # burada boşluk bırakmadık mesela
print(yeni)

# count()
# count() metodu da bir karakter dizisi üzerinde herhangi bir değişiklik yapmamızı sağlamaz. Bu metodun görevi 
# bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini sorgulamaktır.
sehir = "Kahramanmaraş"
print(sehir.count("a"))
# count() metodu yaygın olarak yukarıdaki örnekte görüldüğü şekilde sadece tek bir parametre
# ile kullanılır. Ama aslında bu metot toplam 3 parametre alır
sehir = "adana"
print(sehir.count("a",1))
print(sehir.count("a",3))
# Bu ikinci parametre,count() metodunun bir karakteri saymaya başlarken karakter dizisinin kaçıncı sırasından
# başlayacağını gösteriyor.
parola = input("Parolanız: ")
kontrol = True
for i in parola:
    if parola.count(i) > 1:
        kontrol = False

if kontrol:
    print("Parılanız onaylandı!")
else:
    print("Parolanızda aynı harfi bir kere kullanabilirsiniz!")

kelime = input("Herhangi bir kelime: ")
for harf in kelime:
    print("{} harfi {} kelimesinde {} kez geçiyor!".format( harf, kelime, kelime.count(harf)))
    # burdaki çıktımızda kelimedeki aynı harfler çıktıda tekrarlanıyor
#her harﬁn kelime içinde kaç kez geçtiği bilgisinin yalnızca bir kez raporlanmasını isteyebilirsiniz:
kelime = input("Herhangi bir kelime: ")
sayac = ""
for harf in kelime:
    if harf not in sayac:
        sayac += harf
for harf in sayac:
    print("{} harfi {} kelimesinde {} kez geçiyor!".format( harf, kelime, kelime.count(harf)))