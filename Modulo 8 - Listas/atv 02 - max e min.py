# O código a seguir encontra o produto com maior e menor estoque

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

maiorEstoque = max(estoque)
menorEstoque = min(estoque)

i = estoque.index(maiorEstoque)
j = estoque.index(menorEstoque)

print("O produto com maior estoque é {} com {} unidades disponíveis." .format(produtos[i], estoque[i]))

print("O produto com menor estoque é {} com {} unidades disponíveis." .format(produtos[j], estoque[j]))