from collections import deque #para fazer pesquisa em largura 

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.root = None
        self._size = 0
        self._values = set() #evitar duplicatas

    def insert(self,valor):
        try:

            if valor in self._values:
                print("Valor duplicado. Inserção ignorada.")
                return False  

            aux = Node(valor)
            if(self.root == None):
                self.root = aux
                self._values.add(valor) 
                self._size += 1
                return True

            next = self.root
            while True:
                if aux.data <= next.data:
                    if next.left is None:
                        next.left = aux
                        self._values.add(valor) 
                        self._size += 1
                        return True
                    next = next.left

                elif aux.data > next.data:
                    if next.right is None:
                        next.right = aux
                        self._values.add(valor) 
                        self._size += 1
                        return True
                    next = next.right
        except:
            return False

    def get(self,key):
        try:
            if self.root == None:
                print("ARVORE VAZIA\n")
                return None
            
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

    def getdepth(self,key):
        if self.root == None or key == None:
                print("ARVORE VAZIA\n")
                return 'não encotrado'
        
        next = self.root

        if key == next.data:
            print("O VALOR ESTA LOCALIZADO NA RAIZ,LOGO H = 0\n")

        h = 0

        while next is not None:
            if key == next.data:
                print(f"PROFUNDIDADE DO NÓ({key}):({h})")
                return h 
            elif key < next.data:
                h += 1
                next = next.left
            else:
                h += 1
                next = next.right   

        print("valor não encontrado")
        return 

    def _Hnode(self,no):
        if no == None:
            return -1
        else:
            left_H = self._Hnode(no.left)
            right_H = self._Hnode(no.right)

        return 1 + max(left_H,right_H)
        
    def getheight(self):
        if self.root == None:
            print("ARVORE VAZIA\n")
            return 0
        
        height = self._Hnode(self.root)
        print(f"ALTURA DA ARVORE:({height})\n")
        return height

    def auxIPL(self,no,level):
       if no is None:
        return 0

       aux = level 

       return aux + self.auxIPL(no.right,level + 1) +self.auxIPL(no.left,level+1)         
             
    
    def internal_path_lenght(self):
        if self.root == None:
            print("ARVORE VAZIA\n")
            return 
            
        return self.auxIPL(self.root,0)

    def Max_value(self):
            if self.root == None:
                print("ARVORE VAZIA\n")
                return 
            
            next = self.root
            while next:
                if next.right == None:
                    return next.data
                else:
                    next = next.right
    
    def Min_value(self):
            if self.root == None:
                print("ARVORE VAZIA\n")
                return
            
            next = self.root
            while next:
                if next.left == None:
                    return next.data
                else:
                    next = next.left

    def is_balanced(self):
        if self.root is None:
            return False
        
        _, _balanced = self.aux_isbalanced(self.root)

        if _balanced:
            return True
        else:
            return False
        
    def aux_isbalanced(self,node):
        if node is None:
            return 0,True

        #comeca a verificar os filhos do no atual 
        left_h,left_bal = self.aux_isbalanced(node.left)
        right_h,right_bal = self.aux_isbalanced(node.right)

        #calcula a altura atual 
        current_h = max(left_h,right_h)+1

        #verifica a condição de balanceamento para AVL_trees 
        #ps abs para retornar o valor absoluto 
        isbalanced = (left_bal and right_bal and abs(right_h - left_h)<=1)

        return current_h,isbalanced
    
    # funções print em ordens 
    #raiz,esquerda,direita
    def show_pre_order(self):
        arr = []
        if self.root == None:
            return 
        self._preorder(self.root,arr)
        print()
        return arr
        
    def _preorder(self,nodo,arr):
        print(nodo.data,end=' ')
        arr.append(nodo.data)

        if(nodo.left != None):
            self._preorder(nodo.left,arr)

        if(nodo.right != None):
            self._preorder(nodo.right,arr)
    #esquerda,raiz,direita
    def show_in_order(self):
        arr = []
        if self.root == None:
            return      
        self._inorder(self.root,arr)
        print()
        return arr
    
    def _inorder(self,nodo,arr):

        if(nodo.left != None):
            self._inorder(nodo.left,arr)

        print(nodo.data,end=' ')
        arr.append(nodo.data)

        if(nodo.right != None):
            self._inorder(nodo.right,arr)

    #esquerda,direita,raiz
    def show_pos_order(self):
        arr = []
        if self.root == None:
            return     
        self._posorder(self.root,arr)
        print()
        return arr
    
    def _posorder(self,nodo,arr):
        if nodo is not None:
            if(nodo.left != None):
                self._posorder(nodo.left,arr)

            if(nodo.right != None):
                self._posorder(nodo.right,arr)
            
            print(nodo.data,end=' ')
            arr.append(nodo.data)

    #por nivel 
    def show_in_level(self):
        if self.root is None:
            print("A árvore está vazia.")
            return 
        arr = []
        queue = deque([self.root]) 
        
        while queue:
            node = queue.popleft() 
            print(node.data, end=' ')
            arr.append(node.data)  
            
            if node.left is not None:
                queue.append(node.left)  
            if node.right is not None:
                queue.append(node.right)  

        return arr



        
                     
