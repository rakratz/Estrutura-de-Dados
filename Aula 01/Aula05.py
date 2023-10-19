# Função
# Funções são definidas para realizar operações e retornar valores.

# Função que receba dois valores e retone a soma

def soma(a, b):
    resultado = a + b
    return resultado

# Somar n valores
def soma_valores(valores):
    soma = 0
    for valor in valores:
        soma += valor
    return soma

print(soma(3, 4))
print(soma_valores([3, 4, 5, 10]))

# Procedimento
# Funções são definidas para realizar operações sem retorno

def saudacao(msn):
    print("********************************")
    print(f"Olá {msn}, seja bem vindo")
    print("********************************")

saudacao("Ricardo")
saudacao("Ana")

# Fatorial 5! = 5 x 4 x 3 x 2 x 1 = 120
#          7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5040

def fatorial(valor):
    resultado = 1
    for i in range(1, valor + 1):
        resultado *= i
    return resultado

print(fatorial(5))
print(fatorial(7))

def fatorial_recursivo(valor):
    if valor == 0:
        return 1
    else:
        return valor * fatorial_recursivo(valor - 1)

print(fatorial_recursivo(5))
print(fatorial_recursivo(7))