from pastml.acr import pastml_pipeline

dados = "dados.csv"
arvore = "arvore.tre"

#nome e número de colunas deve ser o mesmo do arquivo de dados
colunas = ['Coluna1', 'Coluna2','Coluna3','Coluna4','Coluna5','Coluna6']

for nome_coluna in colunas:

     arv_compl = "arv_compl_"+nome_coluna+".html"
     arv_compr = "arv_compr_"+nome_coluna+".html"

     pastml_pipeline(data = dados,
                data_sep = ",",
                columns = colunas,
                name_column = nome_coluna,
                tree = arvore,
                html_compressed = arv_compr,
                html = arv_compl,
                verbose = True)
     print("coluna " + nome_coluna+" pronta!")

print("Uhuuul! Terminou :D")
