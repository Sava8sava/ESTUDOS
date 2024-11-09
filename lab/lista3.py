import os 

pessoas ={}
#lista 4 e colocar isso aqui num arquivo txt
def add_pessoa(mapa,cpf,nome,ende,tele):
    mapa[cpf] = {
        "cpf" : cpf,
        "nome": nome,
        "endereço" : ende,
        "telefone" : tele
    }

    salvar_dados_em_arquivo(mapa,"pessoas.txt")
    

def salvar_dados_em_arquivo(mapa, nome_arquivo):
    with open(nome_arquivo, 'a') as arquivo:  
        for cpf, dados in mapa.items():
            arquivo.write(f"CPF: {dados['cpf']}\n")
            arquivo.write(f"Nome: {dados['nome']}\n")
            arquivo.write(f"Endereço: {dados['endereço']}\n")
            arquivo.write(f"Telefone: {dados['telefone']}\n")
            arquivo.write("\n")  

def mostrar_pessoas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = arquivo.read()       
        print(dados)



def buscar_pessoa_no_arquivo(cpf, nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.readlines()
            pessoa_encontrada = False
            dados_pessoa = {}
            
            for i in range(len(conteudo)):
                linha = conteudo[i].strip()
                if linha.startswith(f"CPF: {cpf}"):
                    pessoa_encontrada = True
                    dados_pessoa["cpf"] = linha.split(": ")[1]
                    dados_pessoa["nome"] = conteudo[i + 1].split(": ")[1]
                    dados_pessoa["endereço"] = conteudo[i + 2].split(": ")[1]
                    dados_pessoa["telefone"] = conteudo[i + 3].split(": ")[1]
                    break
            
            if pessoa_encontrada:
                return dados_pessoa
            else:
                return 'Pessoa não encontrada'
    except FileNotFoundError:
        return 'Arquivo não encontrado'


def buscar_cpf(mapa,cara):
    if cara in mapa:
        return mapa[cara]
     
    return 'Pessoa não encontrada'

def buscar_tele(mapa,tele):
     for pessoa in mapa.values():
        if tele in pessoa["telefone"]:
            return pessoa
    
     return 'Pessoa não encontrada'

def buscar_tele_no_arquivo(telefone, nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.readlines()
            pessoa_encontrada = False
            dados_pessoa = {}
            
            for i in range(len(conteudo)):
                linha = conteudo[i].strip()
                if linha.startswith("Telefone: ") and telefone in linha.split(": ")[1]:
                    pessoa_encontrada = True
                    dados_pessoa["cpf"] = conteudo[i - 3].split(": ")[1]
                    dados_pessoa["nome"] = conteudo[i - 2].split(": ")[1]
                    dados_pessoa["endereço"] = conteudo[i - 1].split(": ")[1]
                    dados_pessoa["telefone"] = linha.split(": ")[1]
                    break
            
            if pessoa_encontrada:
                return dados_pessoa
            else:
                return 'Pessoa não encontrada'
    except FileNotFoundError:
        return 'Arquivo não encontrado'

       
     
if __name__ == "__main__":

    while True:

        op = int(input("1. Inserir pessoa:\n2. Listar pessoas cadastradas:\n3. Buscar pessoa por CPF:\n4. Buscar pessoa por Telefone:\n5. Remover pessoa por CPF:\n6.Sair:\nescolha a opção "))

        if op == 1 :
            try :
                num = [ ]
                cpf = input(" insira o cpf: ")

                if cpf in pessoas :
                    print("o cpf ja foi adcionado: ")

                else:    

                    name = input('insira o nome: ')

                    ende = input('o endereço: ')

                    aux = int(input("quantos numeros de telefone o usario tem?: "))
                    for i in range(aux):
                        nume = input("entre com os numero(s): ")
                        num.append(nume)

                    add_pessoa(pessoas,cpf,name,ende,num)

            except:
                print("dado invalido ")

        elif op == 2:
            mostrar_pessoas("pessoas.txt")

        elif op == 3:
            try:
                cpf = input(" insira o cpf que deseja encontrar")
                print(buscar_pessoa_no_arquivo(cpf,"pessoas.txt"))
            except:
                print("dado invalido ")
        

        elif op == 4:
            try:
                num = input(" insira o num que deseja encontrar")
                print(buscar_tele_no_arquivo(num,"pessoas.txt"))
            except:
                print("dado invalido ")
        
        elif op == 5:
            try:
                item = input('coloque o cpf que deseja apagar')
                pessoas.pop(item)
                print(pessoas)

            except:
                print('dado invalido')    

        elif op == 6:
            print("saindo")
            break

        else :
            print("opção inválida")