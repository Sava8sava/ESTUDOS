class Node :
    def __init__(self,key,data):
        self.key = key  
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self,_node):
        _node.next = self.head
        self.head = _node

    def _search(self,key):
        aux = self.head
        while aux:
            if aux.key == key:
                return aux
            aux = aux.next
        return None 
    
    def __str__(self):
        n = self.head
        res = ""
        while n is not None:
            res += f'"{n.key}": {n.val}; '
            n = n.next
        return res
                      
class Hashtable:
    def __init__(self,capacity):
        self.m = capacity
        self.n = 0
        self.table = [Linkedlist() for _ in range(capacity)]

    def _hash(self,value):
        return hash(value) % self.m

    def put(self,key,data):
        pos = self._hash(key)
        existing_node = self.table[pos]._search(key)
        if existing_node is None:
            n =  Node(key,data)
            self.table[pos].add(n)
            self.n += 1
        else:
            existing_node.data = data
            
    def get(self,key):
        aux = self.search(key)
        if aux:
            return aux.data
        else:
            f"valor não encontrado"

    def search(self,key):
        pos = self._hash(key)
        node = self.table[pos]._search(key)
        return node if node else None

    def isEmpty(self):
        return self.n == 0

    def Show(self):
        for i,lista in enumerate(self.table):
            print(f'Bucket {i}:{lista}')

    def _size(self):
        return self.n
    
         
        
           