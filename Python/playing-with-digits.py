'''
Dado dois inteiros positivos 'n' e 'p', queremos achar um inteiro positivo 'k'(caso exista), em que
a soma dos dígitos em 'n' elevados a uma potência consecutiva que começa em 'p', seja igual a 'k'*'n'
=> (a^p + b^(p+1) + c^(p+2) + d^(p+3) +...) = n ∗ k
Caso exista o número exista, retornar 'k', caso não, retornar -1.

=> 1°: Acessar cada dígito de 'n' separadamento para realizar operações individuais:


=> 2°: Calcular a soma dos dígitos elevados a uma potência consecutiva iniciando em 'p'


=> 3°: Dividir a soma por 'n' e verificar se é decimal ou não. Retornar de acordo
    => Edge Cases: Resultado da divisão pode ser 1.0, ou 2.0... O número vai ser inteiro, porém
    vai ser computacionalmente identificado como decimal:
    Verificar se n % soma é 0, caso seja retornar n // soma, caso contrário, retornar -1
'''

def dig_pow(n, p):
    num = n
    #Get every digit individually:
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    #Revert list order
    digits = digits[::-1]

    #Calculate the sum of digits in powers of p...
    sum = 0
    for i in digits:
        sum += i**p
        p += 1

    #Verify if k is integer
    k = sum % num
    res = sum//num
    if k == 0:
        return res
    else:
        return -1
