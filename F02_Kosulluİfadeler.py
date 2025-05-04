print("🔍 Kapsamlı Karar Sistemi\n")

# Kullanıcıdan bazı temel bilgiler alınır
yas = int(input("Yaşınızı girin: "))
cinsiyet = input("Cinsiyetinizi girin (E/K): ").strip().upper()
calisiyor_mu = input("Şu anda çalışıyor musunuz? (Evet/Hayır): ").strip().lower()

print("\n📊 Değerlendirme Başlıyor...\n")

# 1. Yaşa göre değerlendirme
if yas < 0:
    print("❌ Geçersiz yaş girdiniz.")
elif yas < 18:
    print("🧒 Reşit değilsiniz.")
    if yas < 13:
        print("👶 Çocuksunuz.")
    elif yas < 16:
        print("🧑 Ergenlik dönemindesiniz.")
    else:
        print("🧑‍🎓 Genç bireysiniz.")
elif yas <= 65:
    print("🧔 Yetişkin bireysiniz.")
    # Çalışma durumu ile birlikte değerlendir
    if calisiyor_mu == "evet":
        if yas < 25:
            print("📚 Muhtemelen yeni mezun veya öğrencisiniz.")
        elif yas <= 40:
            print("💼 Kariyerinizin aktif dönemindesiniz.")
        else:
            print("👔 Deneyimli bir çalışan olabilirsiniz.")
    elif calisiyor_mu == "hayır":
        print("🛋️ Şu an çalışmıyor olabilirsiniz ya da farklı bir süreçtesiniz.")
    else:
        print("⚠️ Çalışma durumu geçersiz girildi.")
else:
    print("👴 Emeklilik yaşındasınız.")
    if calisiyor_mu == "evet":
        print("👏 Emekli olmanıza rağmen hala çalışıyorsunuz, takdir edilesi.")
    elif calisiyor_mu == "hayır":
        print("🧘 Emeklilik hayatınızın tadını çıkarıyor olabilirsiniz.")
    else:
        print("⚠️ Çalışma durumu geçersiz girildi.")

# 2. Cinsiyet bilgisine göre ekstra mesaj (Bağımsız koşul)
if cinsiyet == "E":
    print("👨 Erkek olarak işlenmiştir.")
elif cinsiyet == "K":
    print("👩 Kadın olarak işlenmiştir.")
else:
    print("⚠️ Cinsiyet bilgisi doğru formatta girilmedi.")

# 3. Mantıksal operatörlerle birleşik karar
print("\n📌 Ek Karar:")
if yas > 18 and calisiyor_mu == "evet":
    print("✅ Yetişkin ve çalışan bir bireysiniz.")
elif yas > 18 and calisiyor_mu == "hayır":
    print("🧐 Yetişkinsiniz ancak şu an çalışmıyorsunuz.")
elif yas <= 18 or calisiyor_mu != "evet":
    print("🔎 Ya reşit değilsiniz ya da çalışmıyorsunuz.")
else:
    print("❓ Koşullar değerlendirilmedi.")

#-----------------------------

kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız : ")
toplam_uzunluk = len(kullanıcı_adı) + len(parola)

mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor!"
print(mesaj.format(toplam_uzunluk))
if toplam_uzunluk > 40:
    print("Kullanıcı adınız ile parolanızın ",
          "toplam uzunluğu 40 karakteri geçmemeli!")
else:
    print("Sisteme hoşgeldiniz!")
