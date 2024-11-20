import re

class TSLL:
    def __init__(self):
        self.Word_list = set()
        pathL = r"leipzig100k.txt"
        self.readf(pathL)

    def filter(self,words):
       for word in words:
           
           filtred_word  =re.sub(r"(?<![a-zA-Z])'|'(?![a-zA-Z])|(?<![a-zA-Z0-9])[^\w']+|[^\w']+(?![a-zA-Z0-9])", "", word)
           if filtred_word:
               self.Word_list.add(filtred_word)

       
        
    def readf(self,path):

        with open(path,'r') as file:
            for lines in file:
                words = lines.strip().split()
                self.filter(words)
            
            
            newpat = r"teste.txt"
            self.writef(newpat)

    def writef(self,newpath):
        with open(newpath,'w') as newfile:
            for word in self.Word_list:
                newfile.write(word + '\n')
                

            

