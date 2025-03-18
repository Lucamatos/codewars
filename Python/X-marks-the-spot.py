=> DESCRIÇÃO: Escreva uma função 'x(n)' que recebe como entrada um número n e retorna um array nxn com um 'X' no meio, o x vai ser representado por 1's e o resto será 0.
 - Exemplo: x(5) ==  [[1, 0, 0, 0, 1],
                     [0, 1, 0, 1, 0],
                     [0, 0, 1, 0, 0],
                     [0, 1, 0, 1, 0],
                     [1, 0, 0, 0, 1]];

x(6) ==  [[1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 1]];


=> ALGORÍTMO:

 - A matriz será composta por array multidimensional, em que cada linha será um subarray.
 - Criamos o array 'matriz' vazio.
 - Criamos variável 'coluna1'com valor igual a 0 e 'coluna2' com valor igual a n-1, sendo n a dimensão da matriz..


 - Criamos um loop para construir as linahs da matriz.
 - Criamos um array 'linha' populado com zero n vezes


 - Verificamos se o resto da divisão da dimensão da matriz por 2 é diferente de 0, no caso, uma matriz de dimensão impar:

 - Criamos a variável 'meio', igual a (n//2) + 1.
 - Verificamos se iteração atual é menor que 'meio' - 1, se for:
 - Mudamos para 1 no array 'linha' os elementos em linha[coluna1] e linha[coluna2]
 - Adicionamos uma unidade para 'coluna1' e subtraímos um para 'coluna2'
 - Adicionamos o array linha à 'matriz.

 - Verificamos se a iteração atual é igual a variável 'meio'-1, se for:
 - Mudamos para 1 o elemento do array 'linha' que está no meio.
 - Adicionamos o array linha na matriz.

 - Verificamos se a iteração atual é maior que 'meio'-1, se sim:
 - Subtraímos uma unidade de 'coluna1' e adicionamos um para 'coluna2'
 - Mudamos para 1 os elementos referentes a linha[coluna1] e linha[coluna2]
 - Adicionamos o array 'linha' na matriz.


 - Verificamos se o resto da divisão da dimensão da matriz por 2 é igual a 0, se for, a matriz tem um dimensão par:

 - Criamos a variável 'meio' = n//2
 - Verificamos se iteração atual é menor 'meio', se for:
 - Mudamos para 1 no array 'linha' os elementos em linha[coluna1] e linha[coluna2]
 - Adicionamos uma unidade para 'coluna1' e subtraímos uma para 'coluna2'
 - Adicionamos o array 'linha' na matriz.

 - Verificamos se iteração atual é igual a 'meio', se for:
 - Alteramos o valor de linha[coluna1] e linha[coluna2] para 1
 - Adicionamos o array 'linha' na matriz.

 - Verificamos se a iteração atual é maior que 'meio', se sim:
 - Somamos uma unidade de 'coluna1' e subtraímos uma para 'coluna2'
 - Mudamos para 1 os elementos referentes a linha[coluna1] e linha[coluna2]
 - Adicionamos o array 'linha' na matriz.

 - Fora do loop, retornamos a matriz para a função.


 => IMPLEMENTAÇÃO DO ALGORÍTMO:
 def x(n):
    matriz = []
    coluna1 = 0
    coluna2 = n-1
    for j in range(0,n):
        linha = [0]*n
        if n%2 != 0:
            meio = (n//2) + 1
            if j < meio-1:
                linha[coluna1] = 1
                linha[coluna2] = 1
                coluna1 += 1
                coluna2 -= 1
                matriz.append(linha)
            if j == meio-1:
                linha[coluna1] = 1
                matriz.append(linha)
            if j > meio-1:
                coluna1 -= 1
                coluna2 += 1
                linha[coluna1] = 1
                linha[coluna2] = 1
                matriz.append(linha)
        if n%2 == 0:
            meio = n//2
            if j < meio:
                linha[coluna1] = 1
                linha[coluna2] = 1
                coluna1 += 1
                coluna2 -= 1
                matriz.append(linha)
            if j == meio:
                linha[coluna1] = 1
                linha[coluna2] = 1
                matriz.append(linha)
            if j > meio:
                coluna1 += 1
                coluna2 -= 1
                linha[coluna1] = 1
                linha[coluna2] = 1
                matriz.append(linha)

    return matriz


