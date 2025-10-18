#Faça uma tabuada das quatro operações

#Olá mundo

def somar(nmr):
    for fixo in range(1,11):
        return nmr + fixo

def subtrair(nmr):
        return nmr
    
def multiplicar(nmr):
    for fixo in range(1,11):
        return nmr * fixo

def divisao(nmr):
    for fixo in range(1,11):
        return nmr / fixo

print("Olá")
usuario = input("Digite seu nome: ").title()
print(f"Seja bem vindo {usuario}!")

while True:
    print("\n     MENU\n" "1 - Adição\n" "2 - Subtração\n" "3 - Multiplicação\n" "4 - Divisão\n" "5 - Sair")

    opcao = int(input("Digite o índice da função: "))
    opcoes ={
        1 : somar,
        2 : subtrair,
        3 : multiplicar,
        4 : divisao
    }

    if opcao == 5:
        print("Saindo... até logo!")
        break

    elif opcao in opcoes:
        while True:
            try:
                nmrUsuario = float(input("Digite o número: "))
                if nmrUsuario == True:
                    break
            except ValueError:
                print("Digite apenas número")
                continue
            resultado = opcoes[opcao](nmrUsuario)
            for fixo, i in enumerate, range(1, 11, start=1):
                print(f"Resultado por {i} : {resultado * fixo}")

    else: print("Opção inválida, tente novamente!")


