# função de pause
from time import sleep

# função para obter a média usando for
def media_com_for(i, soma, media):
    for i in range(1, 6):
        nota = int(input(f"Digite a nota[{i}]: "))
        soma += nota
    media = soma / 5
    print("A média do aluno é {:.2f}".format(media))
    sleep(3)

# função para obter a média usando while
def media_com_while(i, soma, media):
    while i < 5:
        i += 1
        nota = float(input(f"Digite a nota[{i}]: "))
        soma += nota
    media = soma / 5
    print("A média do aluno é {:.2f}".format(media))
    sleep(3)

# função para se obter a tabuada usando for
def multiplicacao_por_5_com_for(i, multiplicacao, numero_que_sera_multiplicado):
    print("*=====TABUADA=====*")
    sleep(3)
    for i in range(0, 11):
        multiplicacao = numero_que_sera_multiplicado * i
        print(f"5 x {i} = {multiplicacao}")
        sleep(3)

# função para se obter a tabuada usando while
def multiplicacao_por_5_com_while(i, multiplicacao, numero_que_sera_multiplicado):
    print("*=====TABUADA=====*")
    sleep(3)
    while i < 11:
        multiplicacao = numero_que_sera_multiplicado * i
        print(f"5 x {i} = {multiplicacao}")
        i += 1
        sleep(3)
        
# chamada da função principal
while True:
    print("Digite a operação correspondente ao seu interesse: ")
    sleep(3)
    print("[ 1 ] Cálculo de média usando a condicional for ")
    sleep(3)
    print("[ 2 ] Cálculo de média usando a condicional while")
    sleep(3)
    print("[ 3 ] Tabuada de um número usando a condicional for")
    sleep(3)
    print("[ 4 ] Tabuada de um número usando a condicional while")
    sleep(3)
    # escolha de opção
    x = int(input("Digite a sua opção que você quer testar: "))
    i = 0
    soma = 0
    multiplicacao = 0
    media = 0
    if x == 1:
        # chamada da função de média com for na função principal
        media_com_for(i, soma, media)
    elif x == 2:
        # chamada da função de média com while na função principal
        media_com_while(i, soma, media)
    elif x == 3:
        # informando o número que terá sua tabuada mostrada
        numero_que_sera_multiplicado = int(input("Digite o número inteiro que terá sua tabuada mostrada: "))
        # chamada da função de tabuada com for na função principal
        multiplicacao_por_5_com_for(i, multiplicacao, numero_que_sera_multiplicado)
    elif x == 4:
        # informando o número que terá sua tabuada mostrada
        numero_que_sera_multiplicado = int(input("Digite o número inteiro que terá sua tabuada mostrada: "))
        # chamada da função de tabuada com while na função principal
        multiplicacao_por_5_com_while(i, multiplicacao, numero_que_sera_multiplicado)
    else:
        # encerramento do programa
        print("Obrigado por usar esse programa. Tenha um excelente dia!")
        sleep(3)
        break