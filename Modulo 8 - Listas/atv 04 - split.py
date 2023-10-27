# O split serve para separar itens em uma lista
# por vezes quando trabalhamos com tratamento de dados no python, 
# pode ocorrer dos dados importados serem inseridos em uma variável, como no exemplo a seguir:

produtos = 'apple tv, mac, iphone x, iphone 11, IPad, apple watch, mac book, airpods'

# nesse caso temos uma variável chamada produtos, mas ela não é uma lista, e sim um conjunto de caracteres
# para transformar essa variável em uma lista usamos o split

lista = produtos.split(', ')

print(lista)

#OBS: o parâmetro ', ' é fornecido pois, na lista principal, esse era o caracter que separava os itens