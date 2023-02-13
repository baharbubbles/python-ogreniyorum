# tic-tac-toe oyunu 
# Burada ilk yapmamız gereken şey, üzerinde oyun oynanacak tahtayı çizmek olmalı. Amacımız şöyle bir görüntü elde etmek:
# " _ _ _   _ _ _   _ _ _
#   _ _ _   _ _ _   _ _ _
#   _ _ _   _ _ _   _ _ _ "  şeklinde oyun tahtası. 
# Bu tahtada oyuncu soldan sağa ve yukarıdan aşağıya doğru iki adet konum bilgisi girecek ve oyunu oynayan kişinin gireceği 
# bu konumlara “X” ve “O” harﬂeri işaretlenecek.

tahta = [["___", "___", "___"],
["___", "___", "___"],
["___", "___", "___"]]

# bilgide verilen tahta görüntüsünü çıktıda elde etmek için şu kodları yazıyoruz:
print("\n"*15)

for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)
# *i'de Yıldız işareti yardımıyla, tahta adlı listeyi oluşturan iç içe geçmiş listeleri liste dışına çıkarıp düzgün
# bir şekilde kullanıcıya gösterdik.

# Şimdi yapmamız gereken şey, oyundaki kazanma ölçütlerini belirlemek. herhangi bir işaretin şu konumlarda bulunması o işaretin kazandığını gösteriyor:
# yukarıdan aşağıya 0; soldan sağa 0             yukarıdan aşağıya 0; soldan sağa 0
# yukarıdan aşağıya 1; soldan sağa 0             yukarıdan aşağıya 0; soldan sağa 1
# yukarıdan aşağıya 2; soldan sağa 0             yukarıdan aşağıya 0; soldan sağa 2

# liste içinde her biri üçer öğeden oluşan 2 liste var. bu listeler kendi içinde ikişer öğeden oluşan bazı listeler içeriyor.
# Burada her bir liste içindeki ilk sayı oyun tahtasında yukarıdan aşağıya doğru olan düzlemi; ikinci sayı ise soldan sağa doğru olan düzlemi gösteriyor.
# Tabii ki oyun içindeki tek kazanma ölçütü bu ikisi olmayacak. 
kazanma_olcütleri = [[[0,0], [1,0], [2,0]], 
                     [[0,1], [1,1], [2,1]],
                     [[0,2], [1,2], [2,2]],
                     [[0,0], [0,1], [0,2]],
                     [[1,0], [1,1], [1,2]],
                     [[2,0], [2,1], [2,2]],
                     [[0,0], [1,1], [2,2]],
                     [[0,2], [1,1], [2,0]]]

# X ve O işaretlerinin oyun tahtasındaki konumu, oyunun gidişatı açısından önem taşıyor.
x_durumu = []
o_durumu = []
# Bu değişkenler sırasıyla X işaretinin ve O işaretinin oyun içinde aldıkları konumları kaydedecek. Bu konumlarla, bir önceki adımda tanımladığımız kazanma 
# ölçütlerini karşılaştırarak oyunu kimin kazandığını tespit edebileceğiz.

# oyunda iki farklı işaret var: X ve O. Dolayısıyla oynama sırası sürekli olarak bu iki işaret arasında değişmeli. Mesela oyuna 0 işareti ile başlanacaksa, 
# 0 işaretinin yerleştirilmesinden sonra sıranın X işaretine geçmesi gerekiyor. X işareti de yerleştirildikten sonra sıra tekrar 0 işaretine geçmeli
# ve oyun süresince bu böyle devam edebilmeli.
sira = 1
while True:
    if sira % 2 == 0:
        isaret = "X".center(3)
    else:
        isaret = "O".center(3)
    print()
    print("İşaret: {}\n".format(isaret))


    x = input("yukarıdan aşağıya [1,2,3]: ".ljust(30))
    if x == "q":
        break
    y = input("soldan sağa [1,2,3]: ".ljust(30))  # ljust() metotlarını, kullanıcıya gösterilecek verinin düzgün bir şekilde hizalanması amacıyla kullandık.
    if y == "q":
        break
    x = int(x)-1
    y = int(y)-1
    # Burada X veya O işaretlerini tahta üzerinde uygun yerlere yerleştirebilmek için kullanıcının konum bilgisi girmesini istiyoruz. x değişkeni
    # yukarıdan aşağıya doğru olan düzlemdeki konumu, y değişkeni ise soldan sağa doğru olan düzlemdeki konumu depolayacak. Oyunda kullanıcının girebileceği değerler 1, 2 veya 3 olacak
    # **son iki satırında ise kullanıcıdan gelen karakter dizilerini birer sayıya dönüştürüyoruz. Bu arada, bildiğiniz gibi Python saymaya 0’dan başlıyor. Ama insanlar
    # açısından doğal olan saymaya 1’den başlamaktır. O yüzden mesela kullanıcı 1 sayısını girdiğinde Python’ın bunu 0 olarak algılamasını sağlamamız gerekiyor. Bunun için x ve y
    # değerlerinden 1 çıkarıyoruz.

    print("\n"*15)
    if tahta[x][y] == "___":
        tahta[x][y] = isaret
        if isaret == "X".center(3):
            x_durumu += [[x,y]]
        elif isaret == "O".center(3):
            o_durumu += [[x,y]]
        sira += 1
    else:
        print("\nOrası dolu! Lütfen tekrar dene!\n")

# Eğer işaret sırası X’te ise oyuncunun girdiği konum bilgilerini x_durumu adlı değişkene, eğer işaret sırası O’da ise konum bilgilerini o_durumu adlı değişkene yolluyoruz. Oyunu
# hangi işaretin kazandığını tespit edebilmemiz açısından bu kodlar büyük önem taşıyor.
# x_durumu ve o_durumu değişkenlerini kazanma_ölçütleri adlı liste ile karşılaştırarak oyunu kimin kazandığına karar vereceğiz.

# Bu arada, oyunun en başında tanımladığımız sıra adlı değişkeni if bloğu içinde artırdığımıza dikkat edin. **Bu sayede, kullanıcının yanlışlıkla aynı konuma iki kez işaret yerleştirmeye
# çalışması halinde işaret sırası değişmeyecek. Yani mesela o anda sıra X’te ise ve oyuncu yanlış bir konum girdiyse sıra yine X’te olacak. Eğer sıra değişkenini if bloğu içine yazmazsak, yanlış
# konum girildiğinde işaret sırası O’a geçecektir.

    for i in tahta:
       print("\t".expandtabs(30), *i, end="\n"*2)

    for i in kazanma_olcütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        print("o: ",o)
        print("x: ",x)
        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()
# Bu kodlar içindeki en önemli öğeler o ve x adlı değişkenlerdir. Burada, o_durumu veya x_durumu adlı listelerdeki değerlerle kazanma_ölçütleri adlı listedeki değerleri karşılaştırarak,
# ortak değerleri o veya x değişkenlerine yolluyoruz. Eğer ortak öğe sayısı 3’e ulaşırsa ( if len(o) == len(i): veya if len(x) == len(i): ), bu sayıyı yakalayan ilk işaret hangisiyse oyunu o
# kazanmış demektir.