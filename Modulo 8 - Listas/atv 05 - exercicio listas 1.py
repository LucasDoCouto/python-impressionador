#Exercícios
#1. Faturamento do Melhor e do Pior Mês do Ano
#Qual foi o valor de vendas do melhor mês do Ano? E valor do pior mês do ano?

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_total = vendas_1sem + vendas_2sem

melhor_mes =  max(vendas_total)
pior_mes = min(vendas_total)

print('O valor de vendas do melhor mês do ano é: {}' .format(melhor_mes))
print('O valor de vendas do pior mês do ano é: {}' .format(pior_mes))

# 2. Continuação
# Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.
# Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.
# Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista

i = vendas_total.index(melhor_mes)
j = vendas_total.index(pior_mes)
faturamento_total = sum(vendas_total)

percentual = melhor_mes / faturamento_total

print('O melhor mês do ano foi {} com {} vendas' .format(meses[i], vendas_total[i]))
print('O pior mês do ano foi {} com {} vendas' .format(meses[j], vendas_total[j]))
print('O faturamento total foi de R$ {:,}' .format(faturamento_total))
print('O melhor mês representa {:.1%} do faturamento anual' .format(percentual))

# 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")
# Dica: o método remove retira um item da lista.
top3 = []

consulta = vendas_total.copy()

i = 1
while i <= 3:
    maior_valor = max(consulta)
    top3.append(maior_valor)
    consulta.remove(maior_valor)
    i += 1

print(top3)
