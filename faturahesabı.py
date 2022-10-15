#her bir ayın kaç gün olduğunu tanımlıyoruz
ocak= mart= mayıs= temmuz= ağustos= ekim= aralık= 31
nisan= haziran= eylül= kasım= 30
şubat= 28

#doğalgazın vergiler dahil metreküp fiyatı
birimFiyat = 0.79

#kullanıcının aylık kullandığı doğalgaz
aylıkSarfiyat = input("aylık kullanılan doğalgazı metreküp olarak girin: ")

#kullanıcı hangi aya ait faturasını öğrenmek istiyor?
dönem = input("""hangi aya ait faturayı hesaplamak istersiniz?
(lütfen ay adının tamamını küçük harflerle yazın)\n""")

#input() fonk. gelen veriyi python diline çeviriyoruz
ay = eval(dönem)

#kullanıcının günlük doğalgaz sarfiyatı
günlükSarfiyat = int(aylıkSarfiyat)/ay

#fatura tutarı
fatura = birimFiyat * günlükSarfiyat * ay

print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
"tahmini fatura tutarı: \t", fatura, " TL", sep="")

