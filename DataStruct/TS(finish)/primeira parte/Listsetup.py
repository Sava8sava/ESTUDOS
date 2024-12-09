import re

class TSLL:
    def __init__(self,path):
        self.Word_list = []
        self.pathL = path
        

    def filter(self,words):
       for word in words:
           
           filtred_word  =re.sub(r"(?<![a-zA-Z])'|'(?![a-zA-Z])|(?<![a-zA-Z0-9])[^\w']+|[^\w']+(?![a-zA-Z0-9])", "", word)
           if filtred_word:
               self.Word_list.append(filtred_word)

         
    def readf(self):

        with open(self.pathL,'r') as file:
            for lines in file:
                words = lines.strip().split()
                self.filter(words)
            
            
    def writef(self,newpath,arr):
        with open(newpath,'w') as newfile:
            for word in arr:
                newfile.write(word + '\n')
                

            

