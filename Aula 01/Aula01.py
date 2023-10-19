# Exercício: leia o nome de uma pessoa e sua
# idade e ao final mostre se essa pessoa é
# maior de idade.

# Entrada de dados input() retorna um str
nome = input('Qual é seu nome? ')
idade = int(input('Qual é sua idade?'))

if (idade >= 18) and (idade < 65):
    print(f"{nome} é Adulto")
elif (idade >= 65):
    print(f"{nome} é idoso")
else:
    print(f"{nome} é Criança")

