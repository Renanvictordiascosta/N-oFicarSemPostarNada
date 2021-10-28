# inserir um elemento na lista e somar todos os elementos da lista e mostrá-los
def inserir_e_somar_elementos_da_lista(soma):
    i = 0
    j = 0
    lista = [ ]
    for i in range(0, 5):
        numero = float(input("Digite um número qualquer: "))
        lista.append(numero)
        i += 1
        if i == 5:
            while j < 5:
                soma = soma + lista[j]
                j += 1
    print(f"Os elementos da lista são{lista}")
    print(f"O valor da soma dos elementos da lista é {soma}")

# chamada da função principal 
soma = 0
# chamada da função de inserir, somar e mostrar valores na função principal
inserir_e_somar_elementos_da_lista(soma)