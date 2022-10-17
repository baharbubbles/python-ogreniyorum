#Karakter Dizilerinin İçeriğini Karşılaştırma
ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
fark = ""
for s in ikinci_metin:                  
   if not s in ilk_metin:
      if not s in fark:
         fark += s
print(fark)   

 #Amacımız ilk_metin’de olan, ama ikinci_metin’de olmayan öğeleri görmek. Bunun için
#ilk_metin’deki öğeleri tek tek ikinci_metin’deki öğelerle karşılaştırmamız gerekiyor.  
# ----------------------
# arklı olan her harften yalnızca bir tanesini çıktıda görmeyi de tercih edebiliriz  
# aşağıdaki kodlarda bunu yaptık        

ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
for s in ilk_metin:
   if not s in ikinci_metin:
      print(s)
   