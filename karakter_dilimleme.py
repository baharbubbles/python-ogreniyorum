# karakter dizilerini dilimleme
site1="www.google.com"
site2="www.istihza.com"
site3="www.yahoo.com"

for isim in site1,site2,site3:
   print("site: ",isim[4:-4])    # verilen sayı eksi değerliyse Python karakter dizisini sağdan sola (yani sondan başa doğru) okuyacaktır
                                     
 # isim[4:-4] yapısını kullanarak, site1,site2, site3, site4 adlı karakter dizilerini, ilk dört ve son dört karakterler 
 # hariç olacak şekilde dilimledik. Böylece elimizde ilk dört ve son dört karakter arasındaki bütün karakterler kalmış oldu

ata1="el elden üstündür!"
ata2="damlaya damlaya göl olur!"
ata3="ağaç yaşken eğilir!"
ata4="su testisi su yolunda kırılır!"
for ata in ata1,ata2,ata3,ata4:
    print(ata[0:-1])  # görevimiz, bu atasözlerinin sonunda bulunan ünlem işaretlerini ortadan kaldırmak

# ünlem işaretlerini kaldırdıktan sonra bunların yerine birer nokta koymak istersek
# for ata in ata1,ata2,ata3,ata4:
#    print(ata[0:-1] + ".")
#------------------------------------------- ---------------------------------------------------------

# >>>kardiz = "Sana Gül Bahçesi Vadetmedim"

# Eğer karakter dizisi içinden alınan ilk karakterin sırasını gösteren sayı 0 ise, bu sayıyı belirtmesek de olur.
# Yani kardiz[0:4] kodunu şöyle de yazabiliriz => kardiz[:4]= 'Sana'

# Tıpkı,alacağımız ilk karakterin sırası 0 olduğunda bu sayıyı belirtmemize gerek olmadığı gibi,
# alacağımız son karakterin sırası karakter dizisinin sonuncu karakterine denk geliyorsa o sayıyı da yazmamıza gerek yok.
# Yani kardiz[17:27] kodunu şöyle de yazabiliriz => kardiz[17:]= 'Vadetmedim'