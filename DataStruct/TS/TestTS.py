from SYMBOLtableLL import LLSymbolTable
from SYMBOLtablearr import TSarr
from SYMBOLtableshash import Hashtable
import time

def measure_time(TS,path,newfilepath,*args):
    time_init = time.time()
    TS(path,newfilepath,*args)
    end_time = time.time()
    return end_time -time_init



def LLTS(path,newfilepath):
    table = LLSymbolTable(path)
    table.GetwordsfromTXT()
    table.ExportToFile(newfilepath)
    return table

def ARRTS(path,newfilepath):
    table = TSarr(path)
    table.GetwordsfromTXT()
    table.ExportToFile(newfilepath)  
    return table

def HASHTS(path,newfilepath,cap):
    table = Hashtable(cap,path)
    table.GetwordsfromTXT()
    table.ExportToFile(newfilepath)
    return table 

if __name__ == "__main__":
    
    pathL = "leipzig100k.txt"
    pathLL = "outputs_das_tabelas/LinkedList.txt"
    pathAR = "outputs_das_tabelas/array.txt"
    pathH = "outputs_das_tabelas/HashTable.txt"
        

    
    # Medindo o tempo para LLTS
    tempo_ll = measure_time(LLTS,pathL,pathLL)
    print(f"LLTS: {tempo_ll:.6f} segundos.")

    # Medindo o tempo para ARRTS
    tempo_arr = measure_time(ARRTS,pathL,pathAR)
    print(f"ARRTS: {tempo_arr:.6f} segundos.")

    # Medindo o tempo para HASHTS 
    capacidade_hash = 227
    tempo_hash = measure_time(HASHTS,pathL,pathH,capacidade_hash)
    print(f"HASHTS: {tempo_hash:.6f} segundos.")


    