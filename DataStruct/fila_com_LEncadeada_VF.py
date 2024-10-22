class No:
    def __init__(self, name, age, prio):
        self.name = name
        self.age = age
        self.prior = prio
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.size = 0
        self.prio_count = 0
        self.common_count = 0
        self.prior_waiting = 0
        self.common_waiting = 0

    def addQ(self, name, age):
        priority_value = self.priority(age)
        if priority_value is None:
            raise ValueError("Prioridade não pode ser None")

        new_node = No(name, age, priority_value)

        # Atualizar contagem de espera
        if priority_value > 0:
            self.prior_waiting += 1
        else:
            self.common_waiting += 1

        if self.head is None:  # Se a fila está vazia
            self.head = new_node
        else:
            if new_node.prior > self.head.prior:  # Nova pessoa com maior prioridade
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                while current.next is not None and current.next.prior >= new_node.prior:
                    current = current.next
                new_node.next = current.next
                current.next = new_node

        self.size += 1

    def dequeue(self):
        if self.head is None:
            print('Não há ninguém na fila.')
            return None
        
        person = self.head
        self.head = self.head.next
        self.size -= 1

        # Atualizar contagem de atendimentos
        if person.prior > 0:
            self.prio_count += 1
            self.prior_waiting -= 1
        else:
            self.common_count += 1
            self.common_waiting -= 1

        print(f"{person.name} atendido, idade: {person.age}, prioridade: {person.prior}.")
        return person

    def displayList(self):
        current = self.head
        if current is None:
            print("A fila está vazia.")
            return

        print("Fila atual:")
        while current:
            print(f"Nome: {current.name}, Idade: {current.age}, Prioridade: {current.prior}")
            current = current.next

    def priority(self, age):
        if age < 60:
            return 0
        elif 60 <= age < 70:
            return 1
        elif 70 <= age < 80:
            return 2
        elif 80 <= age < 90:
            return 3
        elif 90 <= age < 100:
            return 4
        elif age >= 100:
            return 5
        else:
            raise ValueError("Idade inválida")

    def get_info(self,loop_cont):
        print("Número de pessoas atendidas:")
        print(f"Atendimento normal: {self.common_count}")
        print(f"Atendimento prioritário: {self.prio_count}")
        print(f"Tamanho atual da fila: {self.size}")
        print(f"Número de pessoas aguardando atendimento:")
        print(f"Atendimento normal: {self.common_waiting}")
        print(f"Atendimento prioritário: {self.prior_waiting}")

        if loop_cont ==  False:
            total_attended = self.common_count + self.prio_count
            if total_attended > 0:
                normal_percentage = (self.common_count / total_attended) * 100
                priority_percentage = (self.prio_count / total_attended) * 100
                print(f"Porcentagem de pessoas atendidas:")
                print(f"Atendimento normal: {normal_percentage:.2f}%")
                print(f"Atendimentos prioritários: {priority_percentage:.2f}%")
            
    def menu(self):
        loopcon = True
        while loopcon:
            print("\n###############")
            print("1. Adicionar cliente")
            print("2. Atender cliente")
            print("3. Mostrar ordem da fila")
            print("4. Gerar dados de consulta")
            print("5. Sair")
            print("###############")
            opt = input("Escolha uma opção: ")

            if opt == '1':
                name = input("Informe o nome: ")
                age = int(input("Informe a idade: "))
                self.addQ(name, age)
            elif opt == '2':
                self.dequeue()
            elif opt == '3':
                self.displayList()
            elif opt == '4':
                self.get_info(loopcon)
            elif opt == '5':
                if self.size > 0:
                    print("A fila ainda não está vazia.")
                else:
                    loopcon = False
                    self.get_info(loopcon)
                    break
            else:
                print("Opção inválida. Tente novamente.")


# Executar o menu
fila = Queue()
fila.menu()
