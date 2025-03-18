def answer(question, information):
    points = [0] * len(information)
    question = question.split()

    for pointsIdx,info in enumerate(information):
        info = info.lower().split()
        for i in info:
            for q in question:
                if q.lower() == i:
                    points[pointsIdx] += 1

    if max(points) == 0 or points.count(max(points)) > 1:
        return None

    answer = points.index(max(points))
    return information[answer]

'''

Exemplo 1: Utilizando conjuntos (sets) para acelerar a verificação de pertinência

Raciocínio:
Ao converter a lista de palavras da pergunta para um conjunto, você passa de uma operação de busca O(n) para O(1) em cada verificação. Assim, para cada palavra da informação, basta verificar se ela está no conjunto das palavras da pergunta. Essa abordagem é especialmente eficiente quando o número de palavras na pergunta é grande.

Implementação:
def answer(question, information):
    # Converte todas as palavras da pergunta para minúsculas e cria um conjunto para buscas rápidas
    question_set = set(question.lower().split())

    scores = []
    for info in information:
        # Divide a string de informação em palavras e converte para minúsculas
        info_words = info.lower().split()
        # Conta as palavras em comum utilizando a interseção dos conjuntos
        common = question_set.intersection(info_words)
        scores.append(len(common))

    max_score = max(scores)
    # Retorna None se não houver correspondência ou se houver empate
    if max_score == 0 or scores.count(max_score) > 1:
        return None

    return information[scores.index(max_score)]

Exemplo 2: Usando list comprehension e o método sum() para simplificar os loops

Raciocínio:
Podemos melhorar a legibilidade e reduzir a quantidade de linhas usando list comprehensions. Nesse caso, pré-processamos a pergunta para que fique tudo em minúsculas e, para cada item de informação, usamos uma expressão compacta que soma 1 para cada palavra que esteja presente no conjunto de palavras da pergunta.

Implementação:
def answer(question, information):
    # Pré-processa a pergunta uma única vez
    question_set = set(question.lower().split())

    # Calcula os pontos para cada item em information de forma compacta
    scores = [
        sum(1 for word in info.lower().split() if word in question_set)
        for info in information
    ]

    max_score = max(scores)
    if max_score == 0 or scores.count(max_score) > 1:
        return None

    return information[scores.index(max_score)]

Caminhos de pensamento para chegar a essas soluções

    Reduzir repetições e operações desnecessárias:
    Em vez de chamar q.lower() dentro dos loops internos para cada comparação, convertemos as palavras da pergunta uma única vez e armazenamos em um conjunto. Isso diminui a quantidade de chamadas de função e acelera as comparações.

    Aproveitar estruturas de dados apropriadas:
    Ao usar um conjunto para as palavras da pergunta, aproveitamos a eficiência da verificação de pertinência (membership test) em O(1). Essa mudança de estrutura de dados faz com que o algoritmo seja mais escalável quando o volume de palavras aumenta.

    Utilizar list comprehensions para concisão e clareza:
    Com list comprehensions, conseguimos reduzir a verbosidade do código sem perder a clareza. Isso também facilita a manutenção, pois o código se torna mais compacto e expressa diretamente a ideia de "para cada informação, some os acertos".

'''
