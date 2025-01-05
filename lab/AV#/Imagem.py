from ImgDownload import Download
class Imagem:
    def __init__(self):
        self.img_path = None

    def set_local_img(self,path):
        self.img_path = path
    
    def set_public_img(self,url):
        aux = Download()
        aux_path = aux.download_img(url)
        if aux_path:
            self.img_path = aux_path
        else:
            print("erro ao baixar")

    def get_img_path(self):
        return self.img_path