def find_it(seq):
    '''
Dado um array de números, retornar aquele aparece um número ímpar de vezes
Sepre haverá apenas um número que aparece um número ímpar de vezes

Lista vazia 'numbers' de números presentes no array seq

Loop que passa pelo array seq
Verifica se o elemento já esta na lista 'numbers', se não estiver adiciona

Passa pelos elementos em 'numbers'
Conta quantas vezes ele aparece em 'seq'
Se for ímpar, retorna o elemento
    '''
    numbers = []

    for i in seq:
        if i not in numbers:
            numbers.append(i)

    for i in numbers:
        if seq.count(i)%2 != 0:
            return i

'''
Ou poderia ser simplesmente:
    for i in seq:
        if seq.count(i)%2 != 0:
            return i
'''
