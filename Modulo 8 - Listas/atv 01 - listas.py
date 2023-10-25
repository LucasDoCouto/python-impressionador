# Crie um programa para fazer uma consulta de estoque. 
# O usuário do programa deve inserir o nome do produto e, caso ele não exista na lista, ele deve ser avisado. 
#Caso exista, o programa deve dizer a quantidade de unidades em estoque do produto


produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

busca = input("Insira o nome do produto: ")

# Usando If e Else:

#if busca in produtos:
#    i = produtos.index(busca)
#    print("Você tem {} unidades do produto {} em estoque" .format(estoque[i], produtos[i]))
#else:
#    print("Produto não encontrado")

# Usando Try:

try:
    i = produtos.index(busca)
    print("Você tem {} unidades do produto {} em estoque" .format(estoque[i], produtos[i]))
except:
    print("Produto não encontrado")