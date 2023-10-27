# A ideia é usar o join para printar uma lista de produtos ao invés de simplesmente utilizar o comando print
# Dessa forma ela aparece em uma formatação mais próxima do que o usuário final precisaria

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']

# usando o método tradicional:

# print(produtos)

# usando join nós podemos definir o separador dos itens da lista,
# nesse caso eu usei o \n para poder separar cada um em uma linha, mas pode ser utilizado virgula, ponto e vírgula, etc.

print('\n' .join(produtos))