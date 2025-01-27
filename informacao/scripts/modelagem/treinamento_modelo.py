# /Users/eddieferb/informacao/informacao/scripts/modelagem/treinamento_modelo.py
# Este script treina modelos de aprendizado de máquina para prever a taxa de evasão,
# bem como explorar as relações entre taxa de ingresso, taxa de evasão e taxa de conclusão,
# e realizar previsões para ingressantes e concluintes.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def main():
    # Caminho para os dados processados
    caminho_dados = '/Users/eddieferb/informacao/informacao/dados/processado/dados_ingresso_evasao_conclusao.csv'
    df = pd.read_csv(caminho_dados)
    
    # Treinamento para prever ingressantes e concluintes
    if all(col in df.columns for col in ['numero_cursos', 'vagas', 'inscritos', 'docentes', 'ingressantes', 'concluintes']):
        print("Treinando modelos para ingressantes e concluintes...")

        # Features e targets para previsões de ingressantes e concluintes
        X = df[['numero_cursos', 'vagas', 'inscritos', 'docentes']]
        y_ingressantes = df['ingressantes']
        y_concluintes = df['concluintes']

        # Divisão dos dados para ingressantes
        X_train_ing, X_test_ing, y_train_ing, y_test_ing = train_test_split(X, y_ingressantes, test_size=0.2, random_state=42)

        # Modelo Random Forest para ingressantes
        modelo_ingressantes = RandomForestRegressor(random_state=42)
        modelo_ingressantes.fit(X_train_ing, y_train_ing)
        score_ingressantes = modelo_ingressantes.score(X_test_ing, y_test_ing)
        print(f"Score para ingressantes: {score_ingressantes:.4f}")

        # Divisão dos dados para concluintes
        X_train_conc, X_test_conc, y_train_conc, y_test_conc = train_test_split(X, y_concluintes, test_size=0.2, random_state=42)

        # Modelo Random Forest para concluintes
        modelo_concluintes = RandomForestRegressor(random_state=42)
        modelo_concluintes.fit(X_train_conc, y_train_conc)
        score_concluintes = modelo_concluintes.score(X_test_conc, y_test_conc)
        print(f"Score para concluintes: {score_concluintes:.4f}")

        # Salvar modelos de ingressantes e concluintes
        caminho_modelo = '/Users/eddieferb/informacao/informacao/modelos/modelos_salvos'
        os.makedirs(caminho_modelo, exist_ok=True)
        joblib.dump(modelo_ingressantes, os.path.join(caminho_modelo, 'modelo_ingressantes.pkl'))
        joblib.dump(modelo_concluintes, os.path.join(caminho_modelo, 'modelo_concluintes.pkl'))
    
    # Treinamento para taxas de evasão
    print("Treinando modelos para taxa de evasão...")

    # Filtrar as variáveis relevantes
    colunas_relevantes = ['taxa_ingresso', 'taxa_evasao', 'taxa_conclusao']
    df = df[colunas_relevantes].dropna()

    # Dividir as features e o target
    X = df[['taxa_ingresso', 'taxa_conclusao']]
    y = df['taxa_evasao']

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar dois modelos: Regressão Linear e Random Forest
    # Modelo 1: Regressão Linear
    modelo_linear = LinearRegression()
    modelo_linear.fit(X_train, y_train)
    y_pred_linear = modelo_linear.predict(X_test)
    mse_linear = mean_squared_error(y_test, y_pred_linear)
    r2_linear = r2_score(y_test, y_pred_linear)

    # Modelo 2: Random Forest
    modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo_rf.fit(X_train, y_train)
    y_pred_rf = modelo_rf.predict(X_test)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)

    # Escolher o melhor modelo baseado no R²
    melhor_modelo = modelo_rf if r2_rf > r2_linear else modelo_linear
    nome_melhor_modelo = 'Random Forest' if r2_rf > r2_linear else 'Regressão Linear'

    # Salvar o modelo escolhido
    joblib.dump(melhor_modelo, os.path.join(caminho_modelo, 'modelo_melhor_evasao.pkl'))

    # Salvar as métricas dos modelos
    caminho_metricas = '/Users/eddieferb/informacao/informacao/modelos/resultados_modelos'
    os.makedirs(caminho_metricas, exist_ok=True)
    with open(os.path.join(caminho_metricas, 'metricas_modelos.txt'), 'w') as f:
        f.write(f"Modelo: {nome_melhor_modelo}\n")
        f.write(f"MSE - Regressão Linear: {mse_linear:.4f}, R²: {r2_linear:.4f}\n")
        f.write(f"MSE - Random Forest: {mse_rf:.4f}, R²: {r2_rf:.4f}\n")
        f.write(f"Melhor Modelo Selecionado: {nome_melhor_modelo}\n")

    print(f"Treinamento concluído. Melhor modelo para evasão: {nome_melhor_modelo}")
    print(f"Métricas salvas em: {caminho_metricas}")
    print(f"Modelos salvos em: {caminho_modelo}")

if __name__ == '__main__':
    main()