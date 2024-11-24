#graficos para letra A e B da segunda parte
import matplotlib.pyplot as plt

class Graph_AlphaXpy:
    def __init__(self):
        self.X_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.Y_HashalphaM26 = [32, 5, 12, 9, 16, 17, 25, 5, 9, 47, 10, 33, 31, 5, 2, 17, 0, 21, 10, 8, 0, 11, 4, 0, 2, 0]
        self.Y_HashpyM26 = [18, 16, 14, 10, 10, 14, 7, 13, 8, 6, 16, 6, 17, 16, 7, 13, 14, 17, 12, 22, 6, 17, 16, 9, 11, 14]
    
    def print_graph(self):
        # Configuração dos gráficos
        fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

        # Histograma para Y_HashalphaM26
        axes[0].bar(self.X_letters, self.Y_HashalphaM26, color='skyblue', edgecolor='black', width=0.8)
        axes[0].set_title("Distribuição - Y_HashalphaM26")
        axes[0].set_xlabel("Letras do Alfabeto")
        axes[0].set_ylabel("Número de Colisões")
        axes[0].grid(axis='y', linestyle='--', alpha=0.7)

        # Histograma para Y_HashpyM26
        axes[1].bar(self.X_letters, self.Y_HashpyM26, color='lightcoral', edgecolor='black', width=0.8)
        axes[1].set_title("Distribuição - Y_HashpyM26")
        axes[1].set_xlabel("Letras do Alfabeto")
        axes[1].grid(axis='y', linestyle='--', alpha=0.7)

        # Ajustes finais
        #PS o grafico mostra o numero de colisoẽs não o total de nomes na lista,exemplo so tem um nome com U na lista 
        #então esse nome não colide com niguem,então seu valor no grafico e zero
        plt.tight_layout()
        plt.show()


        
        



