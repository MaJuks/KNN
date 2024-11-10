import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# 1. Carregar a tabela de dados corretamente usando pd.read_excel
df = pd.read_excel("Lanches.xlsx")

# 2. Substituir '?' por valores nulos
df.replace("?", pd.NA, inplace=True)
print(df)
# 3. Verificar se há valores faltantes
print("Contagem de valores nulos por coluna:")
print(df.isnull().sum())

# 4. Codificar dados categóricos (se houver)
label_encoders = {}
for column in df.select_dtypes(include=["object"]).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column].astype(str))
    label_encoders[column] = le

# 5. Separar as features (X) e a variável target (y)
target_column = "Tipo de proteína"  # Ajuste se necessário
X = df.drop(columns=[target_column])
y = df[target_column]

# 6. Verificar e imprimir valores nulos na variável target
print("Valores nulos na variável target:")
print(y.isnull().sum())

# 7. Tratar valores faltantes
X_train = X[y.notnull()]
y_train = y[y.notnull()]
X_missing = X[y.isnull()]

# 8. Verificar se temos dados para treinar o modelo
print("Shape de X_train:", X_train.shape)
print("Shape de y_train:", y_train.shape)
print("Shape de X_missing:", X_missing.shape)

if X_train.shape[0] > 0 and y_train.shape[0] > 0:
    # 9. Treinar o modelo KNN com diferentes valores de K
    knn_values = [1, 3, 5]
    predictions = {}

    for k in knn_values:
        knn_model = KNeighborsClassifier(n_neighbors=k)
        knn_model.fit(X_train, y_train)

        if X_missing.shape[0] > 0:
            y_pred = knn_model.predict(X_missing)
            # Armazenar as predições
            predictions[f"KNN{k}"] = y_pred
        else:
            print(f"Nenhum dado faltante para previsão com KNN{k}.")
else:
    print("Não há dados suficientes para treinar o modelo.")

# 10. Preencher a coluna 'Tipo de proteína' com as predições do KNN
for k in knn_values:
    if f"KNN{k}" in predictions:
        df.loc[df[target_column].isnull(), target_column] = predictions[f"KNN{k}"]

# 11. Se ainda houver valores nulos, preencher com a moda
if df[target_column].isnull().sum() > 0:
    moda_tipo_proteina = df[target_column].mode()[0]
    df[target_column].fillna(moda_tipo_proteina, inplace=True)

# 12. Decodificar as predições de volta para strings
for k in knn_values:
    if f"KNN{k}" in predictions:
        predictions[f"KNN{k}"] = [label_encoders[target_column].inverse_transform([pred])[0] for pred in predictions[f"KNN{k}"]]

# 13. Imprimir resultados das predições
for k in knn_values:
    if f"KNN{k}" in predictions:
        print(f"Predições para KNN{k}: {predictions[f'KNN{k}']}")
    else:
        print(f"Nenhuma predição disponível para KNN{k}.")

# 14. Verificar o resultado final
print(df)
