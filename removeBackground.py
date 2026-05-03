from rembg import remove

input_path = "image.jpeg" # Değiştirilecek resim dosyasının adı veya yolu
output_path = "output.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)