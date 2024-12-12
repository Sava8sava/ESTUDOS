class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self,valor):
        try:
            aux = Node(valor)
            if(self.root == None):
                self.root = aux
                self._size += 1
                return

            next = self.root
            while True:
                if aux.data <= next.data:
                    if next.left is None:
                        next.left = aux
                        self._size += 1
                        break
                    next = next.left

                elif aux.data > next.data:
                    if next.right is None:
                        next.right = aux
                        self._size += 1
                        break
                    next = next.right
        except:
            print("ERRO AO INSERIR NA ARVORE\n")

    def get(self,key):
        try:
            if self.root == None:
                print("ARVORE VAZIA\n")
                return
            
            next = self.root
            while next is not None:

                if key == next.data:
                    print(f"VALOR ({key}) ENCONTRADO!\n")
                    return next.data
                
                elif key < next.data:
                    next = next.left
                else:
                    next = next.right   
            
            print("VALOR NÃO ENCONTRADO!\n")
            return None

        except:
            print("erro")

    def size(self):
        print(f"O TAMANHO DA ARVORE(QUANTIDADE DE NÓS): {self._size}\n")

    def getheight(self,key):
        if self.root == None:
                print("ARVORE VAZIA\n")
                return
        
        next = self.root

        if key == next.data:
            print("O VALOR ESTA LOCALIZADO NA RAIZ,LOGO H = 0\n")

        h = 0

        while next is not None:
            if key == next.data:
                print(f"ALTURA DO NÓ({key}):({h})")
                return h 
            elif key < next.data:
                h += 1
                next = next.left
            else:
                h += 1
                next = next.right   

        print("valor não encontrado")
        return 
           
if __name__ == "__main__":
    teste = BinaryTree()
    teste.get(10)
    teste.insert(20)
    teste.insert(10)
    teste.insert(30)
    teste.insert(17)
    teste.get(30)
    teste.get(17)
    teste.get(15)
    teste.size( )
    teste.getheight(17)
    




