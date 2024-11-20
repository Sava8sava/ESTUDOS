from SYMBOLtableLL import LLSymbolTable
from SYMBOLtablearr import TSarr
from SYMBOLtableshash import Hashtable
from Listsetup import TSLL
import time

def measure_time(TS,arr,*args):
    time_init = time.time()
    TS(arr,*args)
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
    for word in arr:
        #adicionando o index como chave 
        table.insertdata(word,1)
    return table

def ARRTS(arr):
    table = TSarr()
    for word in arr:
        #adicionando o index como chave 
        table.insertdata(word,1)  
    print(table.keys == sorted(arr))  
    return table

def HASHTS(arr,cap):
    table = Hashtable(cap)
    for word in arr:
        table.put(word,1)
     
    return table 

if __name__ == "__main__":
    TSLL()
    path = "teste.txt"
    words = Createlist(path)
    sorted(words)
    

if words is not None:
        # Medindo o tempo para LLTS
        tempo_ll = measure_time(LLTS, words)
        print(f"Tempo para adicionar {len(words)} palavras com LLTS: {tempo_ll:.6f} segundos.")

        # Medindo o tempo para ARRTS
        tempo_arr = measure_time(ARRTS, words)
        print(f"Tempo para adicionar {len(words)} palavras com ARRTS: {tempo_arr:.6f} segundos.")

        # Medindo o tempo para HASHTS 
        capacidade_hash = 227
        tempo_hash = measure_time(HASHTS, words, capacidade_hash)
        print(f"Tempo para adicionar {len(words)} palavras com HASHTS: {tempo_hash:.6f} segundos.")


    