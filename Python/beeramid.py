'''
Queremos construir uma pirâmide de latinhas, em que o número de latihas em cada nível é igual ao
nível elevado ao quadrado.

Dado dois numeros inteiros, o seu 'bonus', e 'price'(preço da latinha), determinar quantos níveis
completos de latinha podem ser feitos

=> A partir do 'bonus' e 'price', descobrir o custo para cada nível
=> A partir da descoberta do custa de cada nível, esse valor deve ser adicionado ao custo total
=> Deve-se buscar o custo de cada nível enquanto custo_total <= 'bonus'
=> Contar numero de iterações para determinei o n° de níveis possiveis de serem construídos
'''
def beeramid(bonus, price):
    total_cost = 0
    current_level = 1
    total_cans = bonus // price
    pyramid_cans = 0
    while total_cost <= bonus or pyramid_cans <= total_cans:
        level_cost = price * (current_level ** 2)
        pyramid_cans += (current_level ** 2)
        total_cost += level_cost
        current_level += 1
    if (current_level-2) == -1:
        return 0
    return current_level - 2
'''
Alguns pontos importantes:

    Condição de Loop:
    Você está usando while total_cost <= bonus or pyramid_cans <= total_cans:.
        Esse or faz com que o loop continue enquanto uma das condições seja verdadeira.
        No problema, o critério principal é que o custo total não ultrapasse o bônus. A variável pyramid_cans (número de latinhas utilizadas) acaba sendo redundante, pois, se você multiplica esse valor por price, obtém o custo.

    Incremento do current_level:
    Você incrementa current_level no final do loop, mesmo depois de ter ultrapassado o orçamento. Assim, quando o loop termina, current_level é 1 unidade maior do que o número de níveis que realmente conseguiram ser construídos. Por isso, você precisa subtrair 1.
    Entretanto, por causa de como o loop está montado (o uso de duas condições e o fato de que ele roda “a mais”), você acaba tendo que subtrair 2 para obter o resultado esperado.

    Condição para retornar 0:
    O caso em que current_level - 2 == -1 indica que nem o primeiro nível pôde ser construído. Isso acontece, por exemplo, se o bônus é menor que o preço de uma única lata.

Em resumo, a necessidade de subtrair 2 vem de:

    O fato de que você incrementa current_level mesmo após ultrapassar o bônus.
    A forma como o loop é controlado com duas condições que podem levar a uma execução extra.
'''

#OUTRAS SOLUÇÕES:
'''
Em vez de atualizar o nível e depois ajustar, podemos verificar se conseguimos construir o próximo nível antes de adicionar seu custo.
'''
def beeramid(bonus, price):
    levels = 0
    total_cost = 0
    while True:
        next_level_cost = price * ((levels + 1) ** 2)
        if total_cost + next_level_cost > bonus:
            break
        total_cost += next_level_cost
        levels += 1
    return levels
'''
Começamos com 0 níveis e vamos tentando construir o nível levels + 1.
Se o custo total mais o custo do próximo nível ultrapassa o bônus, paramos.
Assim, não precisamos ajustar o índice no final nem usar condições redundantes.
'''

'''
Outra abordagem é calcular progressivamente a soma dos custos e interromper quando ultrapassar o bônus.
'''
def beeramid(bonus, price):
    levels = 0
    cost = 0
    # Enquanto conseguimos adicionar o custo do próximo nível sem ultrapassar o bonus
    while cost + price * ((levels + 1) ** 2) <= bonus:
        levels += 1
        cost += price * (levels ** 2)
    return levels
'''
Semelhante ao exemplo 1, mas condensamos a verificação diretamente na condição do loop.
O loop só continua enquanto o custo acumulado somado ao custo do próximo nível for menor ou igual ao bônus.
'''
