# projeto feito em 26/09/2020
opcao = ["0- para ver as opcoes", "1- ver a lista de tarefas", "2- adicionar item a lista de tarefas", "3- remover item da lista de tarefas", "4- sair"]
opcaoDigitada = 0
listaTarefas = []


def escolher(num):
    if num == 0:
        print("---------------------------------------------")
        for i in opcao:
            print(i)
    elif num == 1:
        print("---------------------------------------------")
        count = 0
        for i in listaTarefas:
            print(count, "-", i)
            count = count + 1
    elif num == 2:
        print("---------------------------------------------")
        print("Para voltar e escolher uma opção digite 0!!!")
        add = True
        while add:
            valor = input("Digite uma tarefa: ")
            if valor != '0': 
                listaTarefas.append(valor)
            else:
                add = False
    elif num == 3:
        print("---------------------------------------------")
        remover = int(input("Digite o numer de qual tarefa deseja remover: "))
        del listaTarefas[remover]

while True:
    if opcaoDigitada != 4:
        escolher(opcaoDigitada)
        print("___________")
        opcaoDigitada = int(input("Digite a opcao: "))
    else:
        print("Esse programa foi desenvolvido para o curso \nSistemas de informacao 1 semestre. \nBy Daniel Pinhal Filho")
        break
