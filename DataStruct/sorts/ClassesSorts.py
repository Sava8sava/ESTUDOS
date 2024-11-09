#fonte geek for geeks + gpt 

#-------------- primeiro grupo (n^2)---------------#

class Bubblesort:
    #https://users.cs.duke.edu/~ola/bubble/bubble.html informaçoes sobre o bubble sort

 
    def __init__(self):
        pass

    def compare(self,a,b):
        return ((a<b)-(a>b))
    
    def Bsort(self,lista,lista_tam):
        aux = ""
        for i in range(lista_tam-1):
            #print(f"fila:{i}")
            for j in range(i+1,lista_tam):
                if self.compare(lista[j],lista[i])>0:
                    aux = lista[j]
                    lista[j] = lista[i] 
                    lista[i] = aux



        print("ordenado")
        return lista


class Selectionsort:

    def __init__(self):
        pass   

    def Secsort(self,lista,lista_tam):

        for i in range(lista_tam):
       
            indexmin = i
            auxstrmin = lista[i]

            for j in range(i+1,lista_tam):
            
                if auxstrmin > lista[j]:
                    indexmin = j
                    auxstrmin = lista[j]

            if indexmin != i:

                aux = lista[i]
                lista[i] = lista[indexmin]
                lista[indexmin] = aux


        return lista     


class Insertsort:
    def __init__(self):
        pass

    def Inssort(self,lista,lista_size):

        for i in range(lista_size):
            aux = lista[i]
            j = i - 1

            while j >= 0 and lista[j]>aux:
                lista[j+1] = lista[j]
                j-=1

            lista[j+1] = aux

        return lista;   

#-------------- segundo grupo n*log(n)---------------#
     
class Shellsort:
    #https://www.geeksforgeeks.org/python-program-for-shellsort/

    def __init__(self):
        pass

    def Shlsort(self,arr,n):
        gap = n//2

        while gap > 0:

            for i in range(gap,n):
                aux = arr[i]
                j = i
                while j >= gap and arr[j-gap]>aux:
                    arr[j] = arr[j-gap]
                    j -= gap
                arr[j] = aux 

            gap = gap//2  

        return arr           


class Heapsort:
   #https://www.geeksforgeeks.org/heap-sort/

    def __init__(self):
        pass

    def heapify(self,arr,n,i):
        maior  = i

        esq = 2 * i + 1
        dir = 2 * i + 2

        if esq < n and arr[esq] > arr[maior]:
            maior = esq

        if dir < n and arr[dir]> arr[maior]:
            maior = dir

        if maior != i :
            arr[i],arr[maior] = arr[maior],arr[i]

            #recursividade 
            self.heapify(arr,n,maior)
            
    
    def Hsort(self,arr,n):

        for i in range(n// 2 - 1,-1,-1):
            self.heapify(arr,n,i)

        for i in range(n-1,0,-1):
            arr[0],arr[i] = arr[i],arr[0]

            self.heapify(arr,i,0)

        return arr       


class Mergesort:
    #https://www.geeksforgeeks.org/merge-sort/?ref=header_outind + gpt

    def merge(self, left, right):
        sorted_array = []
        i = j = 0

        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        
        while i < len(left):
            sorted_array.append(left[i])
            i += 1

       
        while j < len(right):
            sorted_array.append(right[j])
            j += 1

        return sorted_array
     
    def Msort(self,arr):
        
        n = len(arr)
        if n <= 1:
            return arr
        
        mid = n//2
        met_esq = self.Msort(arr[:mid]) #metade da esquerda
        met_dir = self.Msort(arr[mid:]) #metade da direita

        return self.merge(met_esq,met_dir)
    
class Quicksort:
    #https://www.geeksforgeeks.org/quick-sort-algorithm/?ref=header_outind
    def __init__(self):
        pass

    def partition(self,arr,low,high):
        pivo = arr[high]
        i = low - 1 #menor elemento

        for j in range(low,high):
            if arr[j] < pivo:
                i += 1
                arr[i],arr[j] = arr[j],arr[i] #swap do java

        arr[i + 1], arr[high] = arr[high], arr[i + 1] 
        return i + 1

    def quicksort(self, arr, low, high):
        if low < high:
            p1 = self.partition(arr,low,high)
            self.quicksort(arr, low, p1 - 1)
            self.quicksort(arr, p1 + 1, high)


    def Qsort(self,arr):
        self.quicksort(arr,0,len(arr)-1)
        return arr















        


    

    
