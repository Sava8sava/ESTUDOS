import matplotlib.pyplot as plt 
import numpy as np

# Dados
tipo_de_ts = ['Lista Encadeada com BS', "Array com Binary Search", "Hash Table"]
tempoTs = [106.19, 0.18, 0.88]

# Criação do gráfico
plt.figure(figsize=(8, 6))
bars = plt.bar(tipo_de_ts, tempoTs, color="red")

# Rótulos do gráfico
plt.ylabel("Tempo médio (s)", fontsize=12)
plt.xlabel('Tipo de tabela de símbolos', fontsize=12)
plt.title('Tempo médio x Tipo de tabela de símbolos', fontsize=14)
plt.xticks(rotation=15, fontsize=10)
plt.yticks(fontsize=10)

# Adicionar valores acima das barras
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
             f"{bar.get_height():.2f}",
             ha='center', va='bottom', fontsize=10)

# Mostrar o gráfico
plt.tight_layout()
plt.show()
