pessoas ={}

def add_pessoa(mapa,cpf,nome,ende,tele):
    mapa[str(cpf)] = {
        "cpf" : str(cpf),
        "nome": nome,
        "endereço" : ende,
        "telefone" : tele
    }

def buscar_cpf(mapa,cara):
    if cara in mapa:
        return mapa[cara]
     
    return 'Pessoa não encontrada'

def buscar_tele(mapa,tele):
     for pessoa in mapa.values():
        if pessoa["telefone"] == tele:
            return pessoa
    
     return 'Pessoa não encontrada'

       
     
if __name__ == "__main__":

    while True:

        op = int(input("1. Inserir pessoa:\n2. Listar pessoas cadastradas:\n3. Buscar pessoa por CPF:\n4. Buscar pessoa por Telefone:\n5. Remover pessoa por CPF:\n6.Sair:\nescolha a opção"))

        if op == 1 :
            try :
                cpf = int(input(" insira o cpf"))
                name = input('insira o nome')
                ende = input('o endereço')
                #trocar a variavel unica por uma lista se op tiver mais de um numero
                num = int(input('insira o numero'))

                add_pessoa(pessoas,cpf,name,ende,num)

            except:
                print("dado invalido ")

        elif op == 2:
            print(pessoas)

        elif op == 3:
            try:
                cpf = input(" insira o cpf que deseja encontrar")
                print(buscar_cpf(pessoas,cpf))
            except:
                print("dado invalido ")
        

        elif op == 4:
            try:
                num = int(input(" insira o num que deseja encontrar"))
                print(buscar_tele(pessoas,num))
            except:
                print("dado invalido ")
        
        elif op == 5:
            try:
                item = input('coloque o cpf que deseja apagar')
                pessoas.pop(item)
                print(pessoas)

            except:
                print('dado invalido')    

