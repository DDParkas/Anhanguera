opcao = ["0- para ver as opcoes", "1- ver a lista", "2- adicionar item a lista", "3- remover item da lista", "4- sair"]
opcaoDigitada = 0

def escolher(num):
    if num == 0:
      for i in opcao:
            print(i)
    elif num == 1:
        print("opcao 1")
    elif num == 2:
        print("opcao 2")
    elif num == 3:
        print("opcao 3")

while True:
    if opcaoDigitada != 4:
        escolher(opcaoDigitada)
        opcaoDigitada = int(input("digite a opcao: "))
    else:
        print("Esse programa foi desenvolvido para o curso de sistemas de informacao 1 semestre. By Daniel Pinhal Filho")
        break