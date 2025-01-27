import os
import pandas as pd

def listar_arquivos_relevantes(diretorio):
    """
    Lista arquivos CSV relevantes para o projeto nas subpastas.
    """
    arquivos_relevantes = []
    relevancia = ["GRADUACAO_PRESENCIAL.CSV", 
                  "GRADUACAO_DISTANCIA.CSV", 
                  "FORME_PRESENCIAL.CSV", 
                  "FORME_DISTANCIA.CSV", 
                  "SECOMPLE_PRESENCIAL.CSV", 
                  "SECOMPLE_DISTANCIA.CSV", 
                  "INSTITUICAO.CSV"]
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.upper() in relevancia:
                arquivos_relevantes.append(os.path.join(raiz, arquivo))
    return arquivos_relevantes

def registrar_problemas(arquivo, erro):
    """
    Registra problemas de leitura em um log.
    """
    with open("log_erros.txt", "a") as log:
        log.write(f"Arquivo: {arquivo}, Erro: {erro}\n")

def carregar_arquivo(caminho, delimitador=';', encoding='latin1'):
    """
    Carrega o arquivo CSV com tratamento de erros em linhas problemáticas.
    """
    try:
        print(f"Lendo arquivo: {caminho}")
        return pd.read_csv(caminho, sep=delimitador, encoding=encoding, on_bad_lines='skip', low_memory=False)
    except pd.errors.ParserError as pe:
        print(f"Erro de parsing no arquivo {caminho}: {pe}")
        registrar_problemas(caminho, pe)
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro ao carregar o arquivo {caminho}: {e}")
        registrar_problemas(caminho, e)
        return pd.DataFrame()

def tratar_colunas(df):
    """
    Seleciona colunas relevantes e renomeia para padronização.
    """
    colunas_relevantes = ['NÚMERO_DE_CURSOS', 'QT_VAGAS', 'QT_INSCRITOS', 'QT_INGRESSANTES', 
                          'QT_MATRICULADOS', 'QT_CONCLUINTES', 'QT_DOCENTES']
    mapping_colunas = {
        'NÚMERO_DE_CURSOS': 'numero_cursos',
        'QT_VAGAS': 'vagas',
        'QT_INSCRITOS': 'inscritos',
        'QT_INGRESSANTES': 'ingressantes',
        'QT_MATRICULADOS': 'matriculados',
        'QT_CONCLUINTES': 'concluintes',
        'QT_DOCENTES': 'docentes'
    }
    # Filtrar apenas as colunas relevantes disponíveis
    colunas_disponiveis = [col for col in colunas_relevantes if col in df.columns]
    df = df[colunas_disponiveis].rename(columns=mapping_colunas)
    return df

def unificar_arquivos_csv(arquivos_csv):
    """
    Consolida múltiplos arquivos CSV relevantes em um único DataFrame.
    """
    dataframes = []
    for arquivo in arquivos_csv:
        try:
            delimitador = ';'
            df = carregar_arquivo(arquivo, delimitador=delimitador)
            if df.empty:
                print(f"Aviso: {arquivo} está vazio ou não pôde ser processado.")
                continue
            # Tratar colunas relevantes no arquivo atual
            df = tratar_colunas(df)
            df['fonte_arquivo'] = os.path.basename(arquivo)  # Adiciona a fonte
            dataframes.append(df)
        except Exception as e:
            print(f"Erro ao processar o arquivo {arquivo}: {e}")
            registrar_problemas(arquivo, e)
    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    else:
        print("Nenhum dado consolidado.")
        return pd.DataFrame()

def salvar_dataframe(df, caminho_saida):
    """
    Salva o DataFrame consolidado em um arquivo CSV.
    """
    try:
        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
        df.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8')
        print(f"Dados consolidados salvos em: {caminho_saida}")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def main():
    # Diretórios
    pasta_bruto = '/Users/eddieferb/informacao/informacao/dados/bruto'
    pasta_processado = '/Users/eddieferb/informacao/informacao/dados/processado'
    nome_arquivo_saida = 'dados_ingresso_evasao_conclusao.csv'
    caminho_saida = os.path.join(pasta_processado, nome_arquivo_saida)

    # Listar arquivos CSV relevantes
    print("Listando arquivos CSV relevantes...")
    arquivos_csv = listar_arquivos_relevantes(pasta_bruto)

    # Unificar dados
    print("Unificando arquivos CSV...")
    df_consolidado = unificar_arquivos_csv(arquivos_csv)

    # Salvar arquivo consolidado
    if not df_consolidado.empty:
        salvar_dataframe(df_consolidado, caminho_saida)
    else:
        print("Nenhum dado disponível para salvar. Verifique os logs para mais informações.")

if __name__ == '__main__':
    main()