from ImgDownload import Download
from PIL import Image,UnidentifiedImageError
import matplotlib.pyplot as plt #pequeno erro no visualizador do linux corrigir depois 

class Imagem:
    def __init__(self):
        self.img_path = None
        self.img = None
   
    def set_local_img(self,path):
        #fazer um menu para a pessoa escolher no gui
        try:
            self.img_path = path
            self.img = Image.open(path)

        except (FileNotFoundError,UnidentifiedImageError) as e:
            print(f"erro encontrado: {e}")

    def set_public_img(self,url):
        aux = Download()
        aux_path = aux.download_img(url)
        if aux_path:
            try:
                self.img_path = aux_path
                self.img = Image.open(aux_path)
            except UnidentifiedImageError as e:
                print(f"erro encontrado: {e}")

        else:
            print("erro ao baixar")

    def get_img_path(self) -> str:
        return self.img_path
    
    def show_image(self):
        if self.img:
            try:
                plt.imshow(self.img)
                plt.axis("off")
                plt.show()
            except Exception as e:
                print(f"Erro encontrado: {e}")
        else:
            print("imagem não encontrada")

    def get_img_extension(self) -> str:
        return self.img_path.split(".")[1]
    