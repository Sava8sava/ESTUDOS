class No:
    def __init__(self,Name,age,prio):
        self.data = Name 
        self.next = None
        self.age = age
        self.prior= prio
    


class Queue:
    def __init__(self):
        self.head = None
        self.val = 0
            
    def addQ(self,data,datage):
        priority_value = self.priority(datage)
    
      
        if priority_value is None:
            raise ValueError("Prioridade não pode ser None")

        aux1 = No(data,datage,self.priority(datage))

        if self.head is None:
            self.head = aux1
            self.val +=1
            return


        if aux1.prior > self.head.prior:
           aux1.next = self.head
           self.head = aux1
           self.val +=1
         
        else :
           aux2 = self.head
           while aux2.next is not None and aux2.next.prior >= aux1.prior:
              aux2 = aux2.next

           aux1.next = aux2.next
           aux2.next = aux1
           self.val += 1   


             

    def displayList(self):
        disaux = self.head
        while disaux :
            print(disaux.data, end=" -> " if disaux.next else "\n")
            disaux = disaux.next

    def dequeue(self):
      if self.head is None:
        print('não ten ninguém na fila')
        return
      
      else:
        self.head = self.head.next
        return
        
    def priority(self,age):
      if age <60 :
         return 0 
      if age >= 60 and age< 70 :
         return 1
      if age >= 70 and age< 80 :
         return 2
      if age >= 80 and age< 90 :
         return 3
      if age >= 90 and age< 100 :
         return 4
      if age >=100 :
         return 5
      else:
         raise ValueError("valor invalido")
     
      




 # type: ignore