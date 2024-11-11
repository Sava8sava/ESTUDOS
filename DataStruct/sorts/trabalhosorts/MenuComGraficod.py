import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

class Menu:
    x_geral = [50000, 100000, 250000, 500000, 1000000]

    # O(n log(n))
    y_shell = [0.177, 0.431, 1.454, 3.396, 8.423]
    y_merge = [0.108, 0.243, 0.671, 1.505, 3.214]
    y_quick = [0.069, 0.177, 0.584, 1.53, 4.177]
    y_heap = [0.165, 0.345, 1.073, 2.481, 5.533]

    # O(n^2)
    y_bubble = [160.77, 658.62, 9037.143, 51281.251, 86000]  # O último teste de bubble demorou mais de 24 horas (individualmente), e não terminou; 50000 é uma aproximação e o valor real deve superar isso.
    y_selec = [52.631, 287.513, 3603.861, 14720.246, 33665.1167]
    y_insert = [46.54, 255.798, 2270.733, 9340.451, 29738.359]

    def __init__(self):
        print("APRESENTAÇÃO DOS GRÁFICOS DOS ALGORITMOS DE ORDENAÇÃO\n")
        
        print("# Algumas ressalvas:\nOs valores, na maioria dos casos, foram obtidos tirando a média de 10 operações. Ainda assim, podem estar um pouco inflados pelo uso de multiprocessing para acelerar os 10 testes.")
        print()
       
        try:
            while True:
                op = input("Aperte 1 para mostrar os gráficos ou 2 para sair:\n")
                if op == '1':
                    self.mostrar_graficos()
                elif op == '2':
                    print("SAINDO")
                    break
                               
        except:
            print("ALGO DEU ERRADO. TENTE NOVAMENTE")            

    def mostrar_graficos(self):
        # Gráfico para algoritmos O(n log(n))
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(self.x_geral, self.y_shell, marker='o', linestyle='-', color='red', label='Shellsort')
        plt.plot(self.x_geral, self.y_merge, marker='o', linestyle='-', color='blue', label='Mergesort')
        plt.plot(self.x_geral, self.y_quick, marker='o', linestyle='-', color='green', label='Quicksort')
        plt.plot(self.x_geral, self.y_heap, marker='o', linestyle='-', color='black', label='Heapsort')
        plt.gca().xaxis.set_major_formatter(FuncFormatter(self.formatar_eixo_x))
        plt.xlabel('Número de Elementos')
        plt.ylabel('Média de tempo (segundos)')
        plt.title('Algoritmos O(n log(n))')
        plt.legend()  # Adiciona a legenda para identificar cada conjunto
        plt.grid(True)

        # Gráfico para algoritmos O(n^2)
        plt.subplot(1, 2, 2)
        plt.plot(self.x_geral, self.y_bubble, marker='o', linestyle='-', color='purple', label='Bubblesort')
        plt.annotate("Excedeu 24H",
                     xy=(self.x_geral[-1], self.y_bubble[-1]),
                     xytext=(self.x_geral[-1], self.y_bubble[-1] * 0.5), 
                     arrowprops=dict(facecolor='black', arrowstyle="->"),
                     fontsize=10, color='red')
        
        plt.plot(self.x_geral, self.y_selec, marker='o', linestyle='-', color='orange', label='Selectionsort')
        plt.plot(self.x_geral, self.y_insert, marker='o', linestyle='-', color='cyan', label='Insertionsort')
        plt.gca().xaxis.set_major_formatter(FuncFormatter(self.formatar_eixo_x))
        plt.xlabel('Número de Elementos')
        plt.ylabel('Média de tempo (segundos)')
        plt.title('Algoritmos O(n^2)')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    def formatar_eixo_x(self, valor, posicao):
        return f'{int(valor):,}'


if __name__ == "__main__":
    Menu()    
