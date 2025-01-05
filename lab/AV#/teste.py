from Imagem import Imagem

imagem = Imagem()
imagem.set_public_img(r"https://www.revistaveterinaria.com.br/wp-content/uploads/2018/11/gatinho-preguicoso1.jpg")
print(imagem.get_img_path())
imagem.set_local_img(r"imagens teste/Captura de imagem_20250105_103714.png")
print(imagem.get_img_path())
