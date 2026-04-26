"""
Aylık yol masrafı hesaplayan bir program yazmak istiyoruz. Elimizdeki veriler;

1. Cumartesi-Pazar günleri çalışmıyoruz.
2. Dolayısıyla ayda 22 gün çalışıyoruz.
3. Evden işe gitmek için kullandığımız vasıtanın ücreti 1.5 TL
4. İşten eve dönmek için kullandığımız vasıtanın ücreti 1.4 TL

Aylık yol masrafı nedir?

"""

calismaGunSayisi=22
evdenIseUcret=1.5
isdenEveUcret=1.4

masraf = calismaGunSayisi * (evdenIseUcret + isdenEveUcret)
print("Aylık yol masrafınız:", masraf, "TL")