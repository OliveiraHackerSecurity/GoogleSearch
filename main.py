from googlesearch import search

# Texto de busca
busca = int(input('Digite a palavra de busca: '))

# Faz uma busca e cria lista com os link's do resultado
resultado = list(
       search(
           busca,
           lang='pt-br',
           num_results=5
       )
)

# Mostrar resultados
print(resultado)
