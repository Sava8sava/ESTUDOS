pessoas ={}

def add_pessoa(mapa,cpf,nome,ende,tele):
    mapa[cpf] = {
        "cpf" : cpf,
        "nome": nome,
        "endereço" : ende,
        "telefone" : tele
    }

def buscar(mapa,cara):
    if cara in mapa:
        return mapa[cara]
    else:    
         return 'Pessoa não encontrada'
       
     
if __name__ == "__main__":

    while True:

        op = int(input("1. Inserir pessoa:\n2. Listar pessoas cadastradas:\n3. Buscar pessoa por CPF:\n4. Buscar pessoa por Telefone:\n5. Remover pessoa por CPF:\n6.Sair:\n escolha a opção"))


        

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
                cpf = int(input(" insira o cpf que deseja encontrar"))
                print(buscar(pessoas,cpf))
            except:
                print("dado invalido ")
