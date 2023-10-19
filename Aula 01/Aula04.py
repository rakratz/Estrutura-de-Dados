# Dicionário
# Um dicionário é uma coleção desordenada de elementos,
# onde cada elemento é representado por um par chave-valor.
# Os dicionários são definidos usando chaves {}.
# As chaves devem ser únicas e imutáveis, geralmente são strings.

biblioteca = []

livro = {"Título": "A Sociedade do Anel", "Autor": "J.R.R. Token", "Ano": "1954", "Editora": "Alllen & Unwin"}
biblioteca.append(livro)

livro = {"Título": "Duas Torres", "Autor": "J.R.R. Token", "Ano": "1954"}
biblioteca.append(livro)

livro = {"Autor": "J.R.R. Token", "Ano": "1955", "Editora": "Alllen & Unwin"}
biblioteca.append(livro)

print(biblioteca[0])
print(biblioteca[1])
print(biblioteca[2])

for livro in biblioteca:
    print()
    if "Título" in livro:
        print("Título" , livro["Título"])
    if "Autor" in livro:
        print("Autor", livro["Autor"])
    if "Ano" in livro:
        print("Ano", livro["Ano"])
    if "Editora" in livro:
        print("Editora", livro["Editora"])