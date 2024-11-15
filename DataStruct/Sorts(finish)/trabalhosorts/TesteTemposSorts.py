import random
import multiprocessing
import time
import os
from sorts import *



def measure_time(sort_function, arr,arr_size):
    start_time = time.time()
    try:
        sort_function(arr, arr_size)  
    except TypeError:
        sort_function(arr) 
    end_time = time.time()
    return end_time - start_time

def parallel_test(sort_func, arr, n, case_number):
    random.shuffle(arr)  # Embaralha os dados para um caso específico
    time_taken = measure_time(sort_func, arr.copy(), n)  # Mede o tempo de execução
    print(f"Caso {case_number}: {time_taken:.4f} segundos")
    return time_taken    

def listanomes(lista):
    try:
        with open(lista,"r") as arquivo:
           with open(lista, "r", encoding='utf-8') as arquivo:
                lista_str = [linha.strip() for linha in arquivo.readlines()]
                return lista_str
    
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return []
            



if __name__ == "__main__":
    
    path50k = r"sorts\Lista dos nomes\nomes50k.txt"
    path100k = r"sorts\Lista dos nomes\nomes100k.txt"
    path250k = r"sorts\Lista dos nomes\nomes250k.txt"
    path500k = r"sorts\Lista dos nomes\nomes500k.txt"
    path1000k = r"sorts\Lista dos nomes\nomes1000k.txt"

    ''' esse teste esta usando multiprocess ou seja fazendo mais de teste ao mesmo tempo,isso afeta um pouco a
    velocidade do processador mais pelo na minha maquina nao faz diferença,entao vc devia checar na sua,no meu
    individualmente ele deixA 12-14% individualmente e 10-11% no multiprocess,cheque na sua'''
    
    #o multi processing coloca 10% da cpu para cada caso o que faz com que o resultado fique mais inflado que 
    #fazer um por um

    
    
    
    arr = listanomes(path250k) #essa funçao copia os nomes do txt para uma lista,eu ja define as variaveis acima,para testar os outros e so trocar por outro path 
    
    #objetos 
    ordenador = Bubblesort()
    ordenador2 = Selectionsort()
    ordenador3 = Insertsort()
    ordenador4 = Shellsort()
    ordenador5 = Heapsort()
    ordenador6 = Mergesort()
    ordenador7 = Quicksort()
    n = len(arr) # e o tamanho da lista
    ''' alguns objetos usam 'n' outros nao,se atentar a isso '''
    
    num_tests = 2 # aqui quantos testes a maquina vai fazer em paralelo,quanto maior for ele mais o resultado vai ficar inflado,entao eu recomendo usar 2 ou 3

    #aqui e onde voce define qual algoritimo de organização vc vai usar no teste,na classe sorts,tem a classe,la vc olha qual e metodo que tu tem que usar,exemplo esse e o do selectionsort
    # o do bubble sort por exemplo Bsort,ps se atentar tambem se vc ta puxando o metodo do objeto certo
    sort_func = ordenador.Bsort

    # aqui e a bateria de teste,ele esta fazendo 5 teste,sendo que cada teste,faz duas organizaçoes em paralelo(ou mais se tu mudou num_tests)

    for i in range(5):
        print(f"BATERIA DE TESTES {i+1}")
        with multiprocessing.Pool(processes=num_tests) as pool:
            # Configura os argumentos para cada caso
            tasks = [(sort_func, arr, n, i+1) for i in range(num_tests)]
            # Executa em paralelo
            results = pool.starmap(parallel_test, tasks) 
            
        
        





