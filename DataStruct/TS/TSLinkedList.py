import re

class TSLL:
    def __init__(self):
        self.Word_list = set()
        pathL = r'C:\Users\supre\Projetos de Programa\Gitestudos\ESTUDOS\DataStruct\TS\leipzig100k.txt'
        self.setup(pathL)
        print(self.Word_list)

    def setup(self,path):
        try:
            with open(path,'r') as arquivos:
                for line in arquivos:
                    for word in line.split():
                        self.Word_list.add(word.lower()) 

        except FileNotFoundError:
            print("arquivo não encotrado")


if __name__ == "__main__":
    TSLL()