#range() [aralık] fonksiyonu -- range(ilk_sayı, son_sayı)
for i in range(3): #burada döngünün kaç kere dönceğini belirledik
   parola = input("parola belirleyin: ")
   if not parola:
      print("parola bölümü boş geçilemez!")
   elif len(parola) in range(3, 8):
      print("Yeni parolanız", parola)
      break
   elif i == 2: #burda da döngü sayısını sınırladıktan sonra sınır aşılınca olacakları yazdık
      print("parolayı 3 kez yanlış girdiniz.",
      "Lütfen 30 dakika sonra tekrar deneyin!")
   else:
      print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

# range(ilk_sayı, son_sayı) ile ilgili önemli bilgi de ilk_sayı dahil, son_sayı hariç anlamı vardır  
# -----------------------------------------   
# range(ilk_sayı, son_sayı, atlama_değeri)
#Formüldeki son parametre olan atlama_değeri, aralıktaki sayıların kaçar kaçar ilerleyeceğini gösterir. 