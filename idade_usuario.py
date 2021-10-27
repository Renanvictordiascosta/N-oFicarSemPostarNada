# informar a fase da vida do usuário
def idade_do_usuario(x):
    if x >= 0 and x < 13:
        return print("Esse usuário é uma criança!")
    elif x >= 13 and x < 18:
        return print("Esse usuário é um adolescente!")
    elif x >= 18:
        return print("Esse usuário é um adulto!")
    elif x < 0:
        return print("Idade digitada é inválida!")

# ler a idade do usuário
idade = float(input("Digite a sua idade: "))
idade_do_usuario(idade)


