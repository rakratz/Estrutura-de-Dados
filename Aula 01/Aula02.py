# Estrutura de Dados: Lista, Tupa e Dicionário
# Em Python, listas, tuplas e dicionários são
# tipos de dados usados para armazenar coleções de elementos.
# Cada um deles tem suas características distintas.

# lista de de comprar

# Lista
# Uma lista é uma coleção ordenada e mutável de elementos.
# Lista = [ ]
#             0        1        2         3
compras = ['Arroz', 'Leite', 'Carne', 'Manteiga']

compras[1] = "Leite Desnatado"

compras.append("Ovo")



compras.insert(0, "Margarina")
print(compras)

for x in range(len(compras)):
    print(compras[x])

for item in compras:
    print(item)