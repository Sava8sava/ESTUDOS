import re

class _Filter:
    def __init__(self):
        self.path = r"leipzig100k.txt"
        self.cont = r"trated.txt"
        self.words_list = []
        self.open_file()
        #self.write_file(self.words_list)


    def open_file(self):
        with open(self.path,'r') as file:
            for line in file:
                words = line.strip().split()
                self.words_list.extend(words)
        
    
    def write_file(self,arr):

        with open(self.cont,"w") as newfile:
            for word in arr:
                newfile.write(word+'\n')   






        