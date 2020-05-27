from pastml.acr import pastml_pipeline

dados = "dados.csv"
arvore = "arvore.tre"

colunas = ['Coluna1']

arv_compl = "arv_compl.html"
arv_compr = "arv_compr.html"

pastml_pipeline(data=dados, #dados
                data_sep = ',', #separador dos dados 
                columns=colunas, #lista de colunas
                name_column='Coluna1', #coluna com a qual será feita a análise
                tree=arvore, #árvore filogenética
                html_compressed=arv_compr, #árvore resumida
                html=arv_compl, #árvore completa
                verbose=True) # verbose serve para aparecer um log do que está sendo executado

print("Uhuuul! Terminou :D")
