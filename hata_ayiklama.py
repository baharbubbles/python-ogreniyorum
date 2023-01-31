# hata ayıklama--> try..except.. bloklarının kullanımı
while True:
   ilk_sayi = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")
   if ilk_sayi =="q":
      break
   ikinci_sayi = input("ikinci sayı: ")
   try:
      sayi1 = int(ilk_sayi)
      sayi2 = int(ikinci_sayi)
      print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
   except ZeroDivisionError:
      print("Bir sayıyı 0'a bölemezsiniz!")

# kullanıcı sayı değil de harf değerli veri girerse
   except ValueError:                                  
      print("Lütfen sadece sayı girin!")  

#----- bu kodlar sayesinde kullanıcı sayi dğeri yerine 0 veya harf değeri girerse veriye,
#----- yanlışını ona göstermiş olucaz. her hata türü için kullanıcıya
#----- ayrı bir uyarı mesajı gösteriyoruz


# --->raise 
# eğer kullanıcı, içinde Türkçe karakter geçen bir parola yazarsa
# kendisine TypeError tipinde bir hata mesajı gösteriyoruz

tr_karakter = "şçğüöıİ"
parola = input("Parolanız: ")
for i in parola:
   if i in tr_karakter:
      raise TypeError("Parolada Türkçe karakter kullanılamaz!")
   else:
      pass
print("Parola kabul edildi!")
