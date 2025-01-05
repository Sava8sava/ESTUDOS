class ListTs:
    def __init__(self):
        # Usando uma lista de tuplas (chave, valor)
        self.tabela = []
        self.tamanho = 0

    def busca_binaria(self, chave):
        inicio, fim = 0, len(self.tabela) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.tabela[meio][0] == chave:
                return meio  # Encontrou a chave
            elif self.tabela[meio][0] < chave:
                inicio = meio + 1
            else:
                fim = meio - 1
        return inicio  # Retorna onde a chave deveria estar

    def inserir(self, chave, valor):
        index = self.busca_binaria(chave)
        if index < len(self.tabela) and self.tabela[index][0] == chave:
            # Atualiza o valor se a chave já existir
            self.tabela[index] = (chave, valor)
        else:
            # Insere na posição correta para manter ordenado
            self.tabela.insert(index, (chave, valor))
            self.tamanho += 1

    def buscar(self, chave):
        index = self.busca_binaria(chave)
        if index < len(self.tabela) and self.tabela[index][0] == chave:
            return self.tabela[index][1]
        return None  # Retorna None se não encontrar a chave

    def remover(self, chave):
        index = self.busca_binaria(chave)
        if index < len(self.tabela) and self.tabela[index][0] == chave:
            del self.tabela[index]
            self.tamanho -= 1
            return True
        return False  # Retorna False se não encontrar a chave

    def mostrar(self):
        # Mostra todos os pares chave-valor
        for chave, valor in self.tabela:
            print(f"{chave}: {valor}")
    
    def __len__(self):
        return self.tamanho

    def existe(self,chave):
        if self.buscar(chave) is not None:
            return True
        return False