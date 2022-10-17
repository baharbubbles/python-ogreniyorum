while True:
   parola = input("Bir parola belirleyin: ")
   if not parola:
      print("parola bölümü boş geçilemez!")
   elif len(parola) > 8 or len(parola) < 3:
       print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")
   else:
       print("Yeni parolanız", parola)
       break
      