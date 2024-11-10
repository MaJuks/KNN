import numpy as np
import pandas as pd

## CRIANDO O DATAFRAME EM PYTHON
caminho_do_arquivo = "Lanches.xlsx"
tabela = pd.read_excel(caminho_do_arquivo)
tabela.replace("?", pd.NA, inplace=True)

print("Tabela original:")
print(tabela)

## PEGANDO CADA SUBTIPO DENTRO DAS COLUNAS
opcoes_tipo_pao = tabela["Tipo de pão"].unique()
opcoes_tipo_queijo = tabela["Tipo de queijo"].unique()
opcoes_vegetais = tabela["Vegetais"].unique()
opcoes_tipo_molho = tabela["Tipo de molho"].unique()
opcoes_tipo_proteina = tabela["Tipo de proteína"].unique()


## FUNCAO PARA CONVERTER OS SUBTIPOS EM VALORES NUMÉRICOS DE 0 A 1
def normalizar_opcoes(opcoes):
    n = len(opcoes) - 1
    return {valor: i / n if n > 0 else 0 for i, valor in enumerate(opcoes)}


## CONVERTENDO TIPOS EM NUMEROS
mapeamento_pao = normalizar_opcoes(opcoes_tipo_pao)
mapeamento_queijo = normalizar_opcoes(opcoes_tipo_queijo)
mapeamento_vegetais = normalizar_opcoes(opcoes_vegetais)
mapeamento_molho = normalizar_opcoes(opcoes_tipo_molho)
mapeamento_proteina = normalizar_opcoes(opcoes_tipo_proteina)

## CRIANDO UMA NOVA TABELA COM NUMEROS
tabela_numerica = tabela.copy()
tabela_numerica["Tipo de pão"] = tabela_numerica["Tipo de pão"].map(mapeamento_pao)
tabela_numerica["Tipo de queijo"] = tabela_numerica["Tipo de queijo"].map(mapeamento_queijo)
tabela_numerica["Vegetais"] = tabela_numerica["Vegetais"].map(mapeamento_vegetais)
tabela_numerica["Tipo de molho"] = tabela_numerica["Tipo de molho"].map(mapeamento_molho)
tabela_numerica["Tipo de proteína"] = tabela_numerica["Tipo de proteína"].map(mapeamento_proteina)

print("\nTabela numérica:")
print(tabela_numerica)


## PEGANDO LINHA COM VALOR INCOMPLETO
linha_incompleta = tabela_numerica.iloc[-1]
linha_incompleta = linha_incompleta[:-1]

## LINHAS COMPLETAS PRA FAZER COMPARACAO
matriz_completa = tabela_numerica.iloc[:-1, :-1]

## CALCULANDO DISTANCIAS
distancias = np.sqrt(((matriz_completa - linha_incompleta) ** 2).sum(axis=1))
indices_distancias = np.argsort(distancias)

# PEGANDO INDICES DAS LINHAS COM AS MENORES DISTANCIAS
indices_knn1 = distancias.idxmin()
indices_knn3 = indices_distancias[:3]
indices_knn5 = indices_distancias[:5]


print("\nAs 5 linhas mais próxima encontrada:")
for indice in indices_knn5:
    print(tabela.iloc[indice])
    print()
# KNN1
print("KKN1 = " + tabela.at[indices_knn5[0], "Tipo de proteína"])

# KNN3 - Predição baseada nas 3 primeiras distâncias

knn3_proteinas = [tabela.at[i, "Tipo de proteína"] for i in indices_knn3]
mais_repetida_knn3 = max(set(knn3_proteinas), key=knn3_proteinas.count)
print("KNN3 = " + mais_repetida_knn3)

# KNN5 - Predição baseada nas 5 primeiras distâncias
knn5_proteinas = [tabela.at[i, "Tipo de proteína"] for i in indices_knn5]
mais_repetida_knn5 = max(set(knn5_proteinas), key=knn5_proteinas.count)
print("KNN5 = " + mais_repetida_knn5)
