from pastml.acr import pastml_pipeline

dados = "dados.csv"
arvore = "arvore.tre"

#no arquivo de exemplo, a coluna é nomeada 'traits'
colunas = ['Coluna1']

arv_compl = "arv_compl.html"
arv_compr = "arv_compr.html"

pastml_pipeline(data=dados,
                data_sep = ',',
                columns=colunas,
                name_column='Coluna1',
                tree=arvore,
                html_compressed=arv_compr,
                html=arv_compl,
                verbose=True)

print("Uhuuul! Terminou :D")
