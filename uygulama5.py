#Karakter Dizisindeki Karakterleri Sayma
#metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
#tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
#isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
#yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
#adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
#Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
#gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
#da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
#edilmesi neredeyse bir gelenek halini almıştır."""
#harf = input("Sorgulamak istediğiniz harf: ")
#sayı = ''
#for s in metin:
#   if harf == s:
#      sayı += harf
#print(len(sayı))

#-----------aynı işlemi sayı değerinde oynama yaparak da yazabiliriz.Bunu gösterdik

metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır."""
harf = input("Sorgulamak istediğiniz harf: ")
sayı = 0    #sorgulanan harﬁn dosyada kaç kez geçtiği bilgisini tutacak olan sayı adlı bir değişken tanımlıyoruz
for s in metin:
   if harf == s:
      sayı += 1
print(sayı)
