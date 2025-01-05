import matplotlib.pyplot as plt



# Dados de inserção após 10 repetições
insertion_data = {
    'dict': 0.178596,
    'list': 7.618402,
    'ord dict': 0.168107,
    'default dict': 0.122328,
    'counter' : 0.463565
}

# Dados de checagem pós 10 repetições
check_data = {
    'dict': 0.000011,
    'list': 0.000076,
    'ord dict': 0.000007,
    'default dict': 0.000001,
    'counter' : 0.000003
}

# Dados de remoção pós 10 repetições
removal_data = {
    'dict': 0.000004,
    'list': 0.000176,
    'ord dict': 0.000007,
    'default dict': 0.000003,
    'counter' : 0.000003
}

# Função para criar gráficos de barras
def plot_bar_chart(data, title, ylabel, color):
    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values(), color=color)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel('Estrutura de Dados')
    plt.xticks(rotation=45)
    plt.show()

# Criar os gráficos
plot_bar_chart(insertion_data, 'Tempo de Inserção por Estrutura(144256 palavras)', 'Tempo (s)', 'skyblue')
plot_bar_chart(check_data, 'Tempo de Checagem por Estrutura(10 palavras)', 'Tempo (s)', 'lightgreen')
plot_bar_chart(removal_data, 'Tempo de Remoção por Estrutura(10 palavras)', 'Tempo (s)', 'salmon')
