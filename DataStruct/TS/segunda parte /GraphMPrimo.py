#graficos para m sendo um numero primo 
import matplotlib.pyplot as plt

class PrimeGraph:
    def __init__(self):
        self.listaM19 = [
    14, 28, 22, 16, 17, 18, 19, 17, 15, 21, 14, 26, 22, 18, 
    17, 22, 16, 17, 16]

    # Segunda lista
        self.listaM31 = [
        14, 9, 9, 10, 8, 12, 8, 11, 6, 14, 9, 13, 14, 13, 12, 
        9, 12, 12, 18, 13, 11, 8, 6, 15, 20, 9, 12, 18, 11, 8, 11]

    # Terceira lista
        self.listaM47 = [
        4, 10, 9, 8, 8, 4, 8, 6, 7, 4, 4, 5, 8, 9, 10, 6, 8, 12, 
        7, 11, 8, 6, 12, 7, 3, 4, 6, 2, 7, 9, 5, 10, 10, 9, 10, 
        9, 5, 6, 6, 11, 11, 12, 11, 4, 7, 10, 7]


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

        plt.xticks(buckets, rotation=75)  # Rotaciona os rótulos do eixo x
        plt.show()


