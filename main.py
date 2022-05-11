from googlesearch import search

# Texto de busca
busca = 'Digite a palavra de busca'

# Faz uma busca e cria lista com os link's do resultado
resultado = list(
       search(
           busca,
           lang='pt-br',
           num_results=8
       )
)

# Mostrar resultados
print(resultado)
