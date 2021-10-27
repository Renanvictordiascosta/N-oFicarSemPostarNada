#função de média para informar a situação do aluno
def situacao_aluno(x):
    if x>=0 and x<4:
        return print("Sua média é {:.2f}, logo, você foi reprovado!".format(x))
    elif x>=4 and x<6:
        return print("Sua média é {:.2f}, logo, você está de recuperação!".format(x))
    elif x>=6:
        return print("Sua média foi {:.2f}, logo, você foi aprovado! Parabéns!".format(x))

# notas dos alunos
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# cálculo da média
media_nota = (nota_1 + nota_2 + nota_3)/3

#chamada da função da média
situacao_aluno(media_nota)



