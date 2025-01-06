from Imagem import Imagem

imagem = Imagem()
imagem.set_public_img(r"https://www.revistaveterinaria.com.br/wp-content/uploads/2018/11/gatinho-preguicoso1.jpg")
print(imagem.get_img_path())
imagem.show_image()
print(imagem.get_img_extension())

