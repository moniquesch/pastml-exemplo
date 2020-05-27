# Exemplo de uso PastML 

[Link para o site oficial](https://pastml.pasteur.fr/)

## Arquivos necessários
- Árvore filogenética
- Tabela de dados categóricos

As espécies da tabela e da árvore devem ser as mesmas.

## Variáveis
- dados: caminho para o arquivo da tabela de dados
- arvore: caminho para o arquivo da árvore
- colunas: lista com o nome das colunas da tabela de dados
- arv_compl: caminho onde será gerada a árvore completa (.html)
- arv_compr: caminho onde será gerada a árvore resumida (.html)
- data_sep: separador dos dados na tabela de dados (geralmente vírgula, ponto-e-vírgula ou tab)
- columns: colunas
- name_column: coluna da qual será feita a análise
- tree: arvore
- html_compressed: arv_compr
- html: arv_compl
- Verbose: log do processo (True para aparecer o log, False para não aparecer)
