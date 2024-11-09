import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame com dados fictícios
data = {
    'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio'],
    'Vendas': [150, 200, 250, 300, 350]
}

df = pd.DataFrame(data)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['Mes'], df['Vendas'], marker='o')

# Adicionando título e rótulos
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.grid()

# Exibindo o gráfico
plt.show()
