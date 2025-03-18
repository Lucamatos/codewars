'''
Dado uma sequencia 'seq' com uma série de itens, retornar uma lista de itens, tal qual preserve
a ordem original dos elementos e que os mesmo não se repitam lado a lado

Funcionar para sequencias vazias
Funcionar para sequencias com único elemento
Deve reduzir duplicatas
Deve ser case-sensitive
Deve funcionar para elementos de tipos diferentes

Criar lista vazia 'res'
Loop que passa pelos elementos em 'seq'
    Se for o primeiro elemento, adiciona em 'res' e pula para proxima iteração
    Verificamente se o lemento atual é diferente do anterior
        Caso for, adiciona em 'res'

Retorna 'res'
'''
def unique_in_order(seq):
    res = []
    if len(seq) == 0:
        return res
    res.append(seq[0])
    for i in range(1,len(seq)):
        if type(seq[i]) is str:
            if seq[i] != seq[i-1]:
                res.append(seq[i])
        elif seq[i] != seq[i-1]:
            res.append(seq[i])
    return res
