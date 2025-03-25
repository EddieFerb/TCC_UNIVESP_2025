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

def main(year: int = 2024):
    """
    Faz a leitura dos arquivos já pré-processados (dados_ies.csv e dados_cursos.csv),
    aplica limpeza mínima e salva em formato 'tratado' em pastas adequadas.
    """
    # Definição de caminhos (ajuste conforme necessário)
    caminho_ies = f'./dados/processado/dados_ies_{year}.csv'
    caminho_cursos = f'./dados/processado/dados_cursos_{year}.csv'

    # Saídas
    caminho_ies_tratado = f'./dados/intermediario/dados_ies_tratado_{year}.csv'
    caminho_cursos_tratado = f'./dados/intermediario/dados_cursos_tratado_{year}.csv'

    caminho_ies_final = f'./dados/processado/dados_ies_tratado_{year}.csv'
    caminho_cursos_final = f'./dados/processado/dados_cursos_tratado_{year}.csv'

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
            print(f"Ano de {year} Erro ao processar dados de Cursos: {e}")
    else:
        print("Nenhum dado de Cursos disponível para tratar.")

if __name__ == '__main__':
    for year in range(2024):
        print(f"\tProcessing year {year} ...")
        main(year)
