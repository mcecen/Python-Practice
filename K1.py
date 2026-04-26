"""
Aylık yol masrafı hesaplayan bir program yazmak istiyoruz. Elimizdeki veriler;

1. Cumartesi-Pazar günleri çalışmıyoruz.
2. Dolayısıyla ayda 22 gün çalışıyoruz.
3. Evden işe gitmek için kullandığımız vasıtanın ücreti 1.5 TL
4. İşten eve dönmek için kullandığımız vasıtanın ücreti 1.4 TL

Aylık yol masrafı nedir?
"""

gün = 20
gidiş_ücreti = 1.5
dönüş_ücreti = 1.4

masraf = gün * (gidiş_ücreti + dönüş_ücreti)

print("-"*30)
print("çalışılan gün sayısı\t:", gün)
print("işe gidiş ücreti\t:", gidiş_ücreti)
print("işten dönüş ücreti\t:", dönüş_ücreti)
print("-"*30)
print("AYLIK YOL MASRAFI\t:", masraf)