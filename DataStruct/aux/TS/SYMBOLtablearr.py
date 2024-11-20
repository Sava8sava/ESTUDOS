class TSarr:
    def __init__ (self):
        self.table = []
        self.keys = []

    def Binarysearch(self,key):
        ini,fim = 0,len(self.keys) - 1
        while ini <= fim:
            mid = (ini+fim)//2
            if self.keys[mid] == key:
                return mid 
            elif self.keys[mid] < key:
                ini = mid + 1
            else:
                fim = mid - 1
        return ini          
    
    def insertdata(self,key,data):
        index = self.Binarysearch(key)
        if index < len(self.keys) and self.keys[index]== key:
            self.table[index] = data
        else:
            self.keys.insert(index,key)
            self.table.insert(index,data)
            #assert self.is_ordered(), "Erro: Lista de chaves não está ordenada!"

    def get(self,key):
        index = self.Binarysearch(key)
        if index < len(self.keys) and self.keys[index]== key:
            return self.table[index]
        return None 
    
    def rmv(self,key):
        try:
            index = self.Binarysearch(key)
            if index < len(self.keys) and self.keys[index]== key:
                self.keys.pop(index)
                self.table.pop(index)
        except IndexError:
            print('erro no remove')

    def is_ordered(self):
        return all(self.keys[i] <= self.keys[i+1] for i in range(len(self.keys) - 1))
  



