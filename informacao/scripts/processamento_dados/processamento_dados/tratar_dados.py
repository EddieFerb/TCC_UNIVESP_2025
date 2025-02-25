# # ./informacao/informacao/scripts/processamento_dados/processamento_dados/tratar_dados.py
# # Este script realiza a limpeza e o tratamento de dados.

# import os
# import pandas as pd

# def carregar_dados(caminho_entrada):
#     """
#     Carrega os dados do arquivo CSV.
#     """
#     try:
#         print("Carregando dados...")
#         df = pd.read_csv(caminho_entrada, sep=';', encoding='utf-8', low_memory=False)
#         print("Colunas disponíveis:", df.columns.tolist())
#         return df
#     except Exception as e:
#         raise ValueError(f"Erro ao carregar os dados: {e}")

# def tratar_dados(df):
#     """
#     Realiza a limpeza e o tratamento de dados no DataFrame.
#     """
#     # Colunas numéricas relevantes para o projeto
#     colunas_numericas = ['numero_cursos', 'vagas', 'inscritos', 'ingressantes', 
#                          'matriculados', 'concluintes', 'docentes']
    
#     # Remova duplicatas
#     df = df.drop_duplicates()

#     # Trate valores ausentes
#     df = df.dropna()

#     # Converta para tipos numéricos
#     for col in colunas_numericas:
#         if col in df.columns:
#             df[col] = pd.to_numeric(df[col], errors='coerce')
    
#     # Remova linhas com valores inválidos
#     df = df.dropna()

#     # Filtrar colunas específicas relacionadas ao objetivo do projeto
#     colunas_desejadas = ['taxa_ingresso', 'taxa_evasao', 'taxa_conclusao', 'no_curso', 'no_municipio', 'sg_uf']
#     colunas_disponiveis = [col for col in colunas_desejadas if col in df.columns]

#     if not colunas_disponiveis:
#         raise ValueError(f"Nenhuma das colunas desejadas foi encontrada: {colunas_desejadas}")

#     df = df[colunas_disponiveis]

#     return df

# def salvar_dados_tratados(df, caminho_saida):
#     """
#     Salva o DataFrame tratado em um novo arquivo CSV.
#     """
#     try:
#         os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
#         df.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8')
#         print(f"Dados tratados salvos em: {caminho_saida}")
#     except Exception as e:
#         raise ValueError(f"Erro ao salvar os dados: {e}")

# def main():
#     # Caminhos
#     caminho_entrada = './informacao/informacao/dados/processado/dados_ingresso_evasao_conclusao.csv'
#     caminho_saida_intermediario = './informacao/informacao/dados/intermediario/dados_tratados.csv'
#     caminho_saida_final = './informacao/informacao/dados/processado/dados_tratados.csv'

#     # Carregar os dados
#     try:
#         df = carregar_dados(caminho_entrada)
#     except ValueError as e:
#         print(e)
#         return

#     # Tratar os dados
#     try:
#         df_tratado = tratar_dados(df)
#     except ValueError as e:
#         print(f"Erro ao processar os dados: {e}")
#         return

#     # Salvar os dados intermediários
#     try:
#         salvar_dados_tratados(df_tratado, caminho_saida_intermediario)
#     except ValueError as e:
#         print(f"Erro ao salvar os dados intermediários: {e}")

#     # Salvar os dados tratados finais
#     try:
#         salvar_dados_tratados(df_tratado, caminho_saida_final)
#     except ValueError as e:
#         print(f"Erro ao salvar os dados finais: {e}")

# if __name__ == '__main__':
#     main()

# ./informacao/informacao/scripts/processamento_dados/processamento_dados/tratar_dados.py
# Este script realiza a limpeza e o tratamento de dados para o Censo da Educação Superior 2023,
# considerando apenas os arquivos resultantes do pré-processamento (dados_ies.csv e dados_cursos.csv).

import os
import pandas as pd

def carregar_dados(caminho_entrada):
    """
    Carrega os dados de um arquivo CSV.
    """
    try:
        print(f"Carregando dados de: {caminho_entrada}")
        df = pd.read_csv(caminho_entrada, sep=';', encoding='utf-8', low_memory=False)
        print("Colunas disponíveis:", df.columns.tolist())
        return df
    except Exception as e:
        raise ValueError(f"Erro ao carregar os dados: {e}")

def tratar_dados(df, colunas_numericas=None):
    """
    Realiza a limpeza e o tratamento de dados no DataFrame.
      - Remove duplicatas
      - Descarta valores ausentes
      - Converte colunas numéricas (se fornecidas) para tipo numérico
      - Novamente remove eventuais linhas que fiquem inválidas
      - (Nesta versão, não faz filtragem por colunas específicas, pois os dados já foram pré-processados)
    """
    # Remove duplicatas
    df = df.drop_duplicates()

    # Descartar valores ausentes
    df = df.dropna()

    # Se houver colunas numéricas definidas, converter para tipo numérico
    if colunas_numericas:
        for col in colunas_numericas:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        # E descartar possíveis NaNs novamente
        df = df.dropna()

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
    """
    Faz a leitura dos arquivos já pré-processados (dados_ies.csv e dados_cursos.csv),
    aplica limpeza mínima e salva em formato 'tratado' em pastas adequadas.
    """
    # Definição de caminhos (ajuste conforme necessário)
    caminho_ies = './informacao/informacao/dados/processado/dados_ies.csv'
    caminho_cursos = './informacao/informacao/dados/processado/dados_cursos.csv'

    # Saídas
    caminho_ies_tratado = './informacao/informacao/dados/intermediario/dados_ies_tratado.csv'
    caminho_cursos_tratado = './informacao/informacao/dados/intermediario/dados_cursos_tratado.csv'

    caminho_ies_final = './informacao/informacao/dados/processado/dados_ies_tratado.csv'
    caminho_cursos_final = './informacao/informacao/dados/processado/dados_cursos_tratado.csv'

    # Exemplo de colunas numéricas, se quiser converter:
    # Para IES (docentes)
    colunas_numericas_ies = [
        'docentes_total',
        'docentes_exercicio',
        'docentes_feminino',
        'docentes_masculino'
    ]
    # Para Cursos (ingressantes, matriculados etc.)
    colunas_numericas_cursos = [
        'numero_cursos',
        'vagas_totais',
        'inscritos_totais',
        'ingressantes',
        'matriculados',
        'concluintes'
    ]

    # 1) Processar e tratar IES
    try:
        df_ies = carregar_dados(caminho_ies)
    except ValueError as e:
        print(e)
        df_ies = pd.DataFrame()

    if not df_ies.empty:
        try:
            df_ies_tratado = tratar_dados(df_ies, colunas_numericas=colunas_numericas_ies)
            # Salvar intermediário
            salvar_dados_tratados(df_ies_tratado, caminho_ies_tratado)
            # Salvar final
            salvar_dados_tratados(df_ies_tratado, caminho_ies_final)
        except ValueError as e:
            print(f"Erro ao processar dados de IES: {e}")
    else:
        print("Nenhum dado de IES disponível para tratar.")

    # 2) Processar e tratar Cursos
    try:
        df_cursos = carregar_dados(caminho_cursos)
    except ValueError as e:
        print(e)
        df_cursos = pd.DataFrame()

    if not df_cursos.empty:
        try:
            df_cursos_tratado = tratar_dados(df_cursos, colunas_numericas=colunas_numericas_cursos)
            # Salvar intermediário
            salvar_dados_tratados(df_cursos_tratado, caminho_cursos_tratado)
            # Salvar final
            salvar_dados_tratados(df_cursos_tratado, caminho_cursos_final)
        except ValueError as e:
            print(f"Erro ao processar dados de Cursos: {e}")
    else:
        print("Nenhum dado de Cursos disponível para tratar.")

if __name__ == '__main__':
    main()