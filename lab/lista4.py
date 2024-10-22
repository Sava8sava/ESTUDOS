import os 

class Pessoa:

    def __init__(self):
        pessoas ={}
        self.menu(pessoas)

    def add_pessoa(self,mapa,cpf,nome,ende,tele):
        mapa[cpf] = {
            "cpf" : cpf,
            "nome": nome,
            "endereço" : ende,
            "telefone" : tele
        }
        self.salvar_dados_em_arquivo(mapa,"pessoas.txt") 
    

    def salvar_dados_em_arquivo(self,mapa,nome_arquivo):
        with open(nome_arquivo, 'a') as arquivo:  
            for cpf, dados in mapa.items():
                arquivo.write(f"CPF: {dados['cpf']}\n")
                arquivo.write(f"Nome: {dados['nome']}\n")
                arquivo.write(f"Endereço: {dados['endereço']}\n")
                arquivo.write(f"Telefone: {dados['telefone']}\n")
                arquivo.write("\n") 


    def buscar_pessoa_no_arquivo(self,cpf,nome_arquivo):
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

    def buscar_tele_no_arquivo(self,telefone, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.readlines()
                pessoa_encontrada = False
                dados_pessoa = {}
                
                for i in range(len(conteudo)):
                    linha = conteudo[i].strip()
                    #startswitch retorna true ou false se a string começa com argumento passado para ela
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
        
    def mostrar_pessoas(self,nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            dados = arquivo.read()       
            print(dados)

    def validar_cpf(self,cpf,nome_arquivo):
        try:
            with open(nome_arquivo,'r') as arquivo:
                lines = arquivo.readlines()
                for line in lines:
                    if f"CPF: {cpf}\n" in line:
                        return True 

            return False
        except FileNotFoundError:
            return False
        
    def remover_pessoa(self,cpf,nome_arquivo):
        lineauxs = []
        with open(nome_arquivo,'r') as arquivo:
            lineauxs = arquivo.readlines()

        newlineaux = []#salvar os dados que nao vao ser apagados para retornar ao arquivo
        skip = False
        for lineaux in lineauxs:
            if lineaux.startswith(f"CPF: {cpf}"):
                skip = True
            elif skip and lineaux.strip() == "":
                skip = False
            elif not skip:
                newlineaux.append(lineaux)    

        with open(nome_arquivo, 'w') as arquivo:
            for line in newlineaux:
                arquivo.write(line)
                    
             
    def menu(self,pessoas):
        while True:
            op = int(input("1. Inserir pessoa:\n2. Listar pessoas cadastradas:\n3. Buscar pessoa por CPF:\n4. Buscar pessoa por Telefone:\n5. Remover pessoa por CPF:\n6.Sair:\nescolha a opção "))
            print("######################")
            if op == 1 :
                try :
                    num = [ ]
                    cpf = input(" insira o cpf: ")

                    if self.validar_cpf(cpf,"pessoas.txt"):
                        print("o cpf ja foi adcionado: \n")
                    else:    
                        name = input('insira o nome: ')
                        ende = input('o endereço: ')

                        aux = int(input("quantos numeros de telefone o usario tem?: "))
                        for i in range(aux):
                            nume = input("entre com os numero(s): ")
                            num.append(nume)
                        self.add_pessoa(pessoas,cpf,name,ende,num)
                        print("######################")
                        

                except:
                    print("dado invalido \n")

            elif op == 2:
                self.mostrar_pessoas("pessoas.txt")
                print("######################")
                

            elif op == 3:
                try:
                    cpf = input(" insira o cpf que deseja encontrar")
                    print(self.buscar_pessoa_no_arquivo(cpf,"pessoas.txt"))
                    print("######################")
                except:
                    print("dado invalido ")
            
            elif op == 4:
                try:
                    num = input(" insira o num que deseja encontrar")
                    print(self.buscar_tele_no_arquivo(num,"pessoas.txt"))
                    print("######################")
                except:
                    print("dado invalido ")
            
            elif op == 5:
                try:
                    item = input('coloque o cpf que deseja apagar')
                    if self.validar_cpf(item,"pessoas.txt"):
                        self.remover_pessoa(item,"pessoas.txt")
                        print(f"cpf[{item}] apagado\n")
                    else:
                        print("essa pessoa não esta na lista")
                    print("######################")    
                    
                except Exception as e:
                     print(f"Dado inválido: {e}")

            elif op == 6:
                print("saindo")
                break

            else :
                print("opção inválida")


if __name__ == "__main__":
    teste = Pessoa()
          