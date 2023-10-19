# Criar um sistema para calcular o IMC de 5 pessoas
# lendo os nomes, pesos e alturas salvando cada dados em uma lista
# diferente. Ao final deve mostrar o imc de cada pessoa

# IMC = peso (em quilogramas) / (altura (em metros) * altura (em metros))

# Listas
nomes = []
pesos = []
alturas = []
# Leitura de dados
for i in range(5):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    altura = float(input(f"Digite o altura da {i+1}ª pessoa: "))
    nomes.append(nome)
    pesos.append(peso)
    alturas.append(altura)

print("Resultados do IMC")
for i in range(5):
    imc = pesos[i]/(alturas[i]*alturas[i])
    print(f"{nomes[i]} com peso {pesos[i]}k e altura {alturas[i]}mt")
    print(f"IMC = {imc:.2f}")
