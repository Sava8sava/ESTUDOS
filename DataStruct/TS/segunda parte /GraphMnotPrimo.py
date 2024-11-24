import matplotlib.pyplot as plt


class NotPrimeGraph:
    def __init__(self):
               
        self.listaNaoPrimos16 = [
            24, 20, 27, 29, 26, 17, 17, 25, 17, 20, 25, 16, 23, 26, 19, 24
        ]

       
        self.listaNaoPrimos32 = [
            18, 11, 15, 8, 14, 7, 9, 11, 8, 15, 9, 13, 13, 12, 8, 8, 
            13, 12, 9, 13, 10, 11, 11, 13, 9, 11, 12, 14, 12, 4, 11, 11
        ]

        
        self.listaNaoPrimos64 = [
            5, 4, 3, 4, 7, 6, 8, 11, 4, 4, 2, 7, 7, 5, 6, 6, 4, 2, 
            2, 4, 8, 9, 4, 6, 2, 5, 8, 3, 3, 6, 5, 5, 6, 4, 6, 7, 3, 
            7, 7, 4, 4, 9, 5, 12, 3, 6, 7, 9, 7, 6, 8, 3, 4, 5, 8, 7, 
            10, 6, 6, 6, 3, 4, 5, 3
        ]


    def printgraph(self,lista,titulo,cor):
        plt.figure(figsize=(10, 6))
        # Cria as colunas para cada valor específico na lista
        buckets = range(1, len(lista) + 1)

        plt.bar(buckets, lista, color=cor, edgecolor='black', alpha=0.7)

        plt.title(titulo, fontsize=16)
        plt.xlabel('Buckets', fontsize=12)
        plt.ylabel('Quantidade de palavras', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Adiciona os valores no topo de cada coluna
        for i in range(len(lista)):
            plt.text(buckets[i], lista[i] + 0.5, str(lista[i]), ha='center', fontsize=10)

        plt.xticks(buckets, rotation=45)  # Rotaciona os rótulos do eixo x
        plt.show()



