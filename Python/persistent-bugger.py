'''
Dado um número inteiro positivo 'num', retornar sua persistência multiplicativa, que é igual ao número de vezes que você deve multiplicar os dígitos
em 'num' até atingir um resultado de um dígito único

Variavel persist = 0, para contar o número de multiplicações

Enquanto len(n_str) != 1

    Transforma num em string n_str

    Multiplica todos dígitos em n_str

    Armazena o resultado em n_str e converte para string

Converte n_str para inteiro e retorna o resultado

'''
import math

def persistence(n):

    n_str = str(n)

    persist = 0
    while len(n_str) != 1:
        n = [int(i) for i in n_str]
        mul = math.prod(n)
        n_str = str(mul)
        persist += 1

    return int(persist)
