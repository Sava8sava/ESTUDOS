class Node:
    def __init__(self,key,value):
            self.key = key
            self.value = value
            self.next = None


        
class LLSymbolTable:
      def __init__(self):
            self.head = None       
      
      def insertdata(self,key,value):
            aux = self.head
            while aux:
                  if aux.key == key:
                        aux.value = value
                        return

                  aux = aux.next

            new_node = Node(key,value)
            new_node.next = self.head
            self.head = new_node      
      
      def get(self,key):
            aux = self.head
            while aux:
                  if aux.key == key:
                        return aux.value
                  aux = aux.next

            raise KeyError(r"KEY '{key}' not found")

      def rmv(self,key):
            aux = self.head
            aux_prev = None
            while aux:
                  if aux.key == key:
                        if aux_prev == None:
                              self.head = aux.next
                        else:
                              aux_prev.next = aux.next
                        return
                  aux_prev = aux 
                  aux = aux.next
            raise KeyError(r"KEY '{key}' not found")
            




                  


            
 