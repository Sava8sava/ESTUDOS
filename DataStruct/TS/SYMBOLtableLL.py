from Listsetup import TSLL
class Node:
    def __init__(self,key,value):
            self.key = key
            self.value = value
            self.next = None


#TODO  usar composição para adicionar a classe ttls nas tabelas de simbolos         
class LLSymbolTable:
      def __init__(self,path):
            self.head = None
            self.txt_organizer = TSLL(path)     
      
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
      
      #funções exclusivas para o trabalho:

      def GetwordsfromTXT(self):
            self.txt_organizer.readf()
            print("readf terminou")
            words_already_seen = set()

            for word in self.txt_organizer.Word_list:
                  if word not in words_already_seen:
                        self.insertdata(word,1)
                        words_already_seen.add(word)

      def ExportToFile(self,new_path):
            words = []
            aux = self.head
            while aux:
                  words.append(aux.key)
                  aux = aux.next

            self.txt_organizer.writef(new_path,words)




                  


            
 