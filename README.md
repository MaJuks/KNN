# Explicação do Funcionamento e Resultado do Código

O código foi desenvolvido utilizando a linguagem Python de maneira manual, sem o auxílio de bibliotecas de treinamento e previsão de dados. O objetivo foi aplicar os métodos ensinados em aula para realizar uma análise de dados de maneira prática, para maior entendimento futuro das bibliotecas de treinamento de máquinas.

## Funcionamento do Código

1. **Carregamento de Dados**: 
É realizado um carregamento de um arquivo no formato .xlsx e convertido em um dataframe para a manipulação dos dados.

2. **Tratamento de Dados**:
   A string `"?"` é removida de todas as células e transformada em um valor nulo (null).

3. **Identificação de Categorias**:
   Para cada coluna do dataframe, é identificada a quantidade total de subtipos (ou categorias) presentes. Cada categoria é atribuída um valor numérico entre 0 e 1, normalizando os dados.

4. **Substituição de Valores**:
   Com a normalização, um novo dataframe é criado, onde as strings originais são substituídas pelos valores numéricos calculados.

5. **Separação das Linhas**:
   O código separa as linhas com dados completos das linhas com dados incompletos. Para ambas as situações, a coluna que contém a variável não reconhecida é removida.

6. **Cálculo da Distância Euclidiana**:
   As linhas incompletas são comparadas com as linhas completas utilizando a **distância euclidiana**. Essa distância é calculada para os valores de cada coluna.

7. **Cálculo das Distâncias**:
   Um total de 13 distâncias é acumulado. A menor distância identificada é considerada como **KNN1**.

8. **Cálculo de KNN3 e KNN5**:
   As distâncias menores são utilizadas para calcular o **KNN3** e **KNN5**, onde se considera a moda do tipo de proteína para identificar as classificações.

## Resultado Atingido

A classificação de proteínas com base na comparação entre linhas de dados completos e incompletos, utilizando o método KNN para determinar a melhor correspondência.

