'''
Dado um array de strings, todas elas possuem caracteres similares exceto uma, e deve ser encontrada
As strings podem possuir espaços. Espaços nao sao significativos, podem ser considerados como uma
string vazia
O array possui mais que duas strings
Não é case sensitive
*Edge-cases: quando a string assímilar está no início do array

set(string1) <= set(string2)

Verificar se tds os chars da primeira string estão na segunda
Caso nao estejam, verificar se estão na terceira string
    Caso sim, retornar segunda string
    Caso nao, retornar primeira string
Caso estejam, guardar eles como os chars 'similares'
Verificar qual string possui chars diferentes de 'similares' e retornar
'''
def find_uniq(arr):
    arr_l = [s.lower() for s in arr]
    if not(set(arr_l[0]) <= set(arr_l[1])) or not(set(arr_l[1]) <= set(arr_l[0])):
        if not(set(arr_l[0]) <= set(arr_l[2])) or not(set(arr_l[2]) <= set(arr_l[0])):
            return arr[0]
        else:
            return arr[1]
    else:
        for i in range(len(arr_l)):
            if not(set(arr_l[i]) <= set(arr_l[0])) or not(set(arr_l[0]) <= set(arr_l[i])):
                return arr[i]
