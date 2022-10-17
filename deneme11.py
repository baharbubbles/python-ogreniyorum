#pass kullanımı
while True:
   sayı = int(input("Bir sayı girin: "))
   if sayı == 0:
     break
   elif sayı < 0:
     pass
   else:
      print(sayı)


#continue kullanımı
#
#while True:
#     s = input("Bir sayı girin: ")
#     if s == "iptal":
#       break
#     if len(s) <= 3:
#       continue
#     print("En fazla üç haneli bir sayı girebilirsiniz.")