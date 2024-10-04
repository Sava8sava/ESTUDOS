class No:
    def __init__(self,Name,age):
        self.data = Name 
        self.next = None
        self.priori = None
#classe queue teste
class Queue:
    def __init__(self):
        self.head = None
        self.val = 0
            
    def addQ(self,data,datage):

        if self.head is None:
            self.head = No(data,datage)
            self.val +=1


        else :
            aux = self.head
            while aux.next is not None:
                aux = aux.next 
            
            aux.next = No(data,datage)
            self.val +=1

    def displayList(self):
        disaux = self.head
        while disaux :
            print(disaux.data, end=" -> " if disaux.next else "\n")
            disaux = disaux.next








 # type: ignore