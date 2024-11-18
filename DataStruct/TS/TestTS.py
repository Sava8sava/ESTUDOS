from SYMBOLtableLL import LLSymbolTable
from SYMBOLtablearr import TSarr
import time

def measure_time(TS,arr):
    time_init = time.time()
    TS(arr)
    end_time = time.time()
    return end_time -time_init

def Createlist(path):
    words = []
    try:
        with open(path,'r') as file:
            for line in file:
                #strip para retirar os espaços 
                word = line.strip()
                if word is not None:
                    words.append(word)
    except FileNotFoundError:
        print("erro arquivo não encontrado")
    return words

def LLTS(arr):
    table = LLSymbolTable()
    for index,word in enumerate(arr):
        #adicionando o index como chave 
        table.insertdata(index,word)
    return table

def ARRTS(arr):
    table = TSarr()
    for word in arr:
        #adicionando o index como chave 
        table.insertdata(word,1)
    print(table.get('0'))    
    return table



if __name__ == "__main__":
    path = "teste.txt"
    words = Createlist(path)
    sorted(words)
    

if words is not None:
    #tempo = measure_time(lambda arr:LLTS(arr),words)
    tempo = measure_time(ARRTS,words)
    print(f"Tempo para adicionar {len(words)} palavras: {tempo:.6f} segundos.")    
    