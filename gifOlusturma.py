import os
from PIL import Image, ImageDraw

def ellipse(x, y, offset):
    # Her kare için yeni bir mavi arka plan oluşturur
    image = Image.new("RGB", (400, 400), "blue")
    draw = ImageDraw.Draw(image)
    # Kırmızı bir daire çizer
    draw.ellipse((x, y, x + offset, y + offset), fill="red")
    return image

def make_gif():
    frames = []
    x, y = 0, 0
    offset = 50
    
    # 10 kare oluşturuyoruz (400x400 dışına çıkmaması için sınırı azalttım)
    for _ in range(10):
        frames.append(ellipse(x, y, offset))
        x += 35
        y += 35
        
    if frames:
        # Mevcut çalışma dizinini al ve tam yolu yazdır
        output_path = os.path.join(os.getcwd(), "circle.gif")
        
        # save_all=True ile kareleri birleştiriyoruz
        # frames[1:] kullanarak ilk karenin tekrarlanmasını engelliyoruz
        frames[0].save(
            output_path, 
            format="GIF", 
            append_images=frames[1:],
            save_all=True, 
            duration=100, 
            loop=0
        )
        print(f"Başarılı! GIF şuraya kaydedildi: {output_path}")
    else:
        print("Hata: Kareler oluşturulamadı.")

if __name__ == "__main__":
    make_gif()