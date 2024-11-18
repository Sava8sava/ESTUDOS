import re
path1 = r"/home/macaxeira/projetos/ESTUDOS/DataStruct/TS/leipzig100k.txt"
path2 = r"/home/macaxeira/projetos/ESTUDOS/DataStruct/TS/teste.txt"
'''
# Ler o arquivo de entrada
with open(path1, 'r', encoding='utf-8') as file:
    content = file.read()

# Usar regex para encontrar palavras
words = re.findall(r'\w+', content)

# Remover duplicatas e ordenar insensivelmente a maiúsculas/minúsculas
unique_sorted_words = sorted(set(words), key=str.lower)

# Salvar no arquivo de saída
with open(path2, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(unique_sorted_words))

print("Palavras únicas ordenadas salvas em 'output.txt'")
'''
import subprocess

# Comando que será executado
command = "grep -o -E '\\w+' leipzig100k.txt | sort -u -f"

# Executar o comando no shell
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Salvar o resultado em um arquivo
with open(path2, 'w', encoding='utf-8') as output_file:
    output_file.write(result.stdout)

print("Resultado do comando salvo em 'output.txt'")
