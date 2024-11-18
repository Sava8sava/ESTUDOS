import re

class TSLL:
    def __init__(self):
        self.Word_list = set()
        pathL = r"/home/macaxeira/projetos/ESTUDOS/DataStruct/TS/leipzig100k.txt"
        self.readf(pathL)

    def filter(self,word):
        #ler no arquivo linha,seprarar as palavras dessa linha,jogar pra essa funçao de filtrar feita pelo vitor retornar a palvra
        pass
    def readf(self,path):

        with open(path,'r') as file:
            content = file.read()
            newpat = r"/home/macaxeira/projetos/ESTUDOS/DataStruct/TS/teste.txt"

            '''
            aqui modificar a funçao para lert linha por linha,separar as palavras dessa linha e mandar para funçao filtradora 
            '''

            words = modContent.split(' ')
            
            
            self.Word_list.update(word.lower() for word in words)
            
            
            self.writef(newpat)

    def writef(self,newpath):
        with open(newpath,'w') as newfile:
            for word in sorted(self.Word_list):
                newfile.write(word + '\n')
                

            

    
if __name__ == "__main__":
    TSLL()
