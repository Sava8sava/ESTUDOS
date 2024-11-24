from GraphMnotPrimo import NotPrimeGraph
from GraphMPrimo import PrimeGraph
from GraphGen import Graph_AlphaXpy

class Menu:
    def __init__(self):
        self.PG = PrimeGraph()
        self.NPG = NotPrimeGraph()
        self.GAXGPY = Graph_AlphaXpy()
        self.print_menu()

    def print_menu(self):
        while True:
            print("Menu de escolhas de graficos:\n")
            print("OP-1 : Gráfico de comparação de colisões entre a função hash alphabética e a função hash da própria linguagem para M26:\n")
            print("OP-2 : Gráfico para a distribuição de nomes da tabela Hash usando M = números primos:\n")
            print("OP-3 : Gráfico para a distribuição de nomes da tabela Hash usando M = números não primos primos:\n")
            print("OP-4 : SAIR\n")

            op = int(input("Escolha uma opção:\n"))

            if op == 1:
                self.GAXGPY.print_graph()

            elif op == 2:
                self.PG.printgraph(self.PG.listaM19,"grafico para M = 19","green")
                self.PG.printgraph(self.PG.listaM31,"grafico para M = 31","red")    
                self.PG.printgraph(self.PG.listaM47,"grafico para M = 47","yellow") 

            elif op == 3 :
                self.NPG.printgraph(self.NPG.listaNaoPrimos16,"grafico para M = 16","purple")
                self.NPG.printgraph(self.NPG.listaNaoPrimos32,"grafico para M = 32","red")       
                self.NPG.printgraph(self.NPG.listaNaoPrimos64,"grafico para M = 64","cyan")  
                #ps: os valores embaixo da colunas estao virados para impedir bugs graphicos quando M é muito grande

            elif op == 4:
                break

            else:
                print("valor invalido")    

if __name__ == "__main__":
    Menu()


