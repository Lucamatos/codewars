def tribonacci(signature, n):
    '''
    Dada uma sequencia de numeros 'signature', e um número 'n', retornar uma lista contendo os 3 primeiros números de 'signature' e uma sequencia de
    números resultantes da soma do mesmo e seus dois elementos anteriores, até a lista atingir o tamanho 10

    Criar uma lista vazia 'tribonacci'

    Caso n == 0, retornar 'tribonacci'

    Adiciona em 'tribonacci' os 3 primeiros elementos em 'signature'

    Criar um loop que itera um total de 8x
    A cada iteração, adicionar em 'tribonacci' a soma do elemento atual com seus dois elementos anteriores

    Retornar tribonacci
    '''
    tribonacci = []

    if n == 0:
        return tribonacci
    if n == 1:
        return [signature[0]]
    if n == 2:
        return [signature[0],signature[1]]

    [tribonacci.append(i) for i in signature]

    for i in range(2,n-1):
        e = tribonacci[i] + tribonacci[i-1] + tribonacci[i-2]
        tribonacci.append(e)

    return tribonacci

'''
    ou
def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]



'''
