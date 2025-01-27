# /Users/eddieferb/informacao/informacao/scripts/processamento_dados/processamento_dados/tratar_dados.py
# Este script realiza a limpeza e o tratamento de dados.

import os
import pandas as pd

def carregar_dados(caminho_entrada):
    """
    Carrega os dados do arquivo CSV.
    """
    try:
        print("Carregando dados...")
        df = pd.read_csv(caminho_entrada, sep=';', encoding='utf-8', low_memory=False)
        print("Colunas disponíveis:", df.columns.tolist())
        return df
    except Exception as e:
        raise ValueError(f"Erro ao carregar os dados: {e}")

def tratar_dados(df):
    """
    Realiza a limpeza e o tratamento de dados no DataFrame.
    """
    # Colunas numéricas relevantes para o projeto
    colunas_numericas = ['numero_cursos', 'vagas', 'inscritos', 'ingressantes', 
                         'matriculados', 'concluintes', 'docentes']
    
    # Remova duplicatas
    df = df.drop_duplicates()

    # Trate valores ausentes
    df = df.dropna()

    # Converta para tipos numéricos
    for col in colunas_numericas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Remova linhas com valores inválidos
    df = df.dropna()

    # Filtrar colunas específicas relacionadas ao objetivo do projeto
    colunas_desejadas = ['taxa_ingresso', 'taxa_evasao', 'taxa_conclusao', 'no_curso', 'no_municipio', 'sg_uf']
    colunas_disponiveis = [col for col in colunas_desejadas if col in df.columns]

    if not colunas_disponiveis:
        raise ValueError(f"Nenhuma das colunas desejadas foi encontrada: {colunas_desejadas}")

    df = df[colunas_disponiveis]

    return df

def salvar_dados_tratados(df, caminho_saida):
    """
    Salva o DataFrame tratado em um novo arquivo CSV.
    """
    try:
        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
        df.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8')
        print(f"Dados tratados salvos em: {caminho_saida}")
    except Exception as e:
        raise ValueError(f"Erro ao salvar os dados: {e}")

def main():
    # Caminhos
    caminho_entrada = '/Users/eddieferb/informacao/informacao/dados/processado/dados_ingresso_evasao_conclusao.csv'
    caminho_saida_intermediario = '/Users/eddieferb/informacao/informacao/dados/intermediario/dados_tratados.csv'
    caminho_saida_final = '/Users/eddieferb/informacao/informacao/dados/processado/dados_tratados.csv'

    # Carregar os dados
    try:
        df = carregar_dados(caminho_entrada)
    except ValueError as e:
        print(e)
        return

    # Tratar os dados
    try:
        df_tratado = tratar_dados(df)
    except ValueError as e:
        print(f"Erro ao processar os dados: {e}")
        return

    # Salvar os dados intermediários
    try:
        salvar_dados_tratados(df_tratado, caminho_saida_intermediario)
    except ValueError as e:
        print(f"Erro ao salvar os dados intermediários: {e}")

    # Salvar os dados tratados finais
    try:
        salvar_dados_tratados(df_tratado, caminho_saida_final)
    except ValueError as e:
        print(f"Erro ao salvar os dados finais: {e}")

if __name__ == '__main__':
    main()