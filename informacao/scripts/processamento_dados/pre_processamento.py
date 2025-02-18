# import os
# import pandas as pd

# def listar_arquivos_relevantes(diretorio):
#     """
#     Lista arquivos CSV relevantes para o projeto nas subpastas.
#     """
#     arquivos_relevantes = []
#     relevancia = ["GRADUACAO_PRESENCIAL.CSV", 
#                   "GRADUACAO_DISTANCIA.CSV", 
#                   "FORME_PRESENCIAL.CSV", 
#                   "FORME_DISTANCIA.CSV", 
#                   "SECOMPLE_PRESENCIAL.CSV", 
#                   "SECOMPLE_DISTANCIA.CSV", 
#                   "INSTITUICAO.CSV"]
#     for raiz, _, arquivos in os.walk(diretorio):
#         for arquivo in arquivos:
#             if arquivo.upper() in relevancia:
#                 arquivos_relevantes.append(os.path.join(raiz, arquivo))
#     return arquivos_relevantes

# def registrar_problemas(arquivo, erro):
#     """
#     Registra problemas de leitura em um log.
#     """
#     with open("log_erros.txt", "a") as log:
#         log.write(f"Arquivo: {arquivo}, Erro: {erro}\n")

# def carregar_arquivo(caminho, delimitador=';', encoding='latin1'):
#     """
#     Carrega o arquivo CSV com tratamento de erros em linhas problemáticas.
#     """
#     try:
#         print(f"Lendo arquivo: {caminho}")
#         return pd.read_csv(caminho, sep=delimitador, encoding=encoding, on_bad_lines='skip', low_memory=False)
#     except pd.errors.ParserError as pe:
#         print(f"Erro de parsing no arquivo {caminho}: {pe}")
#         registrar_problemas(caminho, pe)
#         return pd.DataFrame()
#     except Exception as e:
#         print(f"Erro ao carregar o arquivo {caminho}: {e}")
#         registrar_problemas(caminho, e)
#         return pd.DataFrame()

# def tratar_colunas(df):
#     """
#     Seleciona colunas relevantes e renomeia para padronização.
#     """
#     colunas_relevantes = ['NÚMERO_DE_CURSOS', 'QT_VAGAS', 'QT_INSCRITOS', 'QT_INGRESSANTES', 
#                           'QT_MATRICULADOS', 'QT_CONCLUINTES', 'QT_DOCENTES']
#     mapping_colunas = {
#         'NÚMERO_DE_CURSOS': 'numero_cursos',
#         'QT_VAGAS': 'vagas',
#         'QT_INSCRITOS': 'inscritos',
#         'QT_INGRESSANTES': 'ingressantes',
#         'QT_MATRICULADOS': 'matriculados',
#         'QT_CONCLUINTES': 'concluintes',
#         'QT_DOCENTES': 'docentes'
#     }
#     # Filtrar apenas as colunas relevantes disponíveis
#     colunas_disponiveis = [col for col in colunas_relevantes if col in df.columns]
#     df = df[colunas_disponiveis].rename(columns=mapping_colunas)
#     return df

# def unificar_arquivos_csv(arquivos_csv):
#     """
#     Consolida múltiplos arquivos CSV relevantes em um único DataFrame.
#     """
#     dataframes = []
#     for arquivo in arquivos_csv:
#         try:
#             delimitador = ';'
#             df = carregar_arquivo(arquivo, delimitador=delimitador)
#             if df.empty:
#                 print(f"Aviso: {arquivo} está vazio ou não pôde ser processado.")
#                 continue
#             # Tratar colunas relevantes no arquivo atual
#             df = tratar_colunas(df)
#             df['fonte_arquivo'] = os.path.basename(arquivo)  # Adiciona a fonte
#             dataframes.append(df)
#         except Exception as e:
#             print(f"Erro ao processar o arquivo {arquivo}: {e}")
#             registrar_problemas(arquivo, e)
#     if dataframes:
#         return pd.concat(dataframes, ignore_index=True)
#     else:
#         print("Nenhum dado consolidado.")
#         return pd.DataFrame()

# def salvar_dataframe(df, caminho_saida):
#     """
#     Salva o DataFrame consolidado em um arquivo CSV.
#     """
#     try:
#         os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
#         df.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8')
#         print(f"Dados consolidados salvos em: {caminho_saida}")
#     except Exception as e:
#         print(f"Erro ao salvar os dados: {e}")

# def main():
#     # Diretórios
#     pasta_bruto = '/Users/eddieferb/informacao/informacao/dados/bruto'
#     pasta_processado = '/Users/eddieferb/informacao/informacao/dados/processado'
#     nome_arquivo_saida = 'dados_ingresso_evasao_conclusao.csv'
#     caminho_saida = os.path.join(pasta_processado, nome_arquivo_saida)

#     # Listar arquivos CSV relevantes
#     print("Listando arquivos CSV relevantes...")
#     arquivos_csv = listar_arquivos_relevantes(pasta_bruto)

#     # Unificar dados
#     print("Unificando arquivos CSV...")
#     df_consolidado = unificar_arquivos_csv(arquivos_csv)

#     # Salvar arquivo consolidado
#     if not df_consolidado.empty:
#         salvar_dataframe(df_consolidado, caminho_saida)
#     else:
#         print("Nenhum dado disponível para salvar. Verifique os logs para mais informações.")

# if __name__ == '__main__':
#     main()
import os
import pandas as pd

# ==========================================================================
# CONFIGURAÇÕES GERAIS
# ==========================================================================

# Diretórios de entrada e saída (ajuste conforme sua estrutura)
PASTA_BRUTO = "/Users/eddieferb/informacao/informacao/dados/bruto"
PASTA_PROCESSADO = "/Users/eddieferb/informacao/informacao/dados/processado"

# Nomes (ou trechos) que identificam cada arquivo no novo formato
# Ajustados para refletir os arquivos efetivamente presentes no diretório
ARQUIVO_IES = "MICRODADOS_ED_SUP_IES_2023.CSV"
ARQUIVO_CURSOS = "MICRODADOS_CADASTRO_CURSOS_2023.CSV"

# Arquivos de saída
NOME_SAIDA_IES = "dados_ies.csv"
NOME_SAIDA_CURSOS = "dados_cursos.csv"


# ==========================================================================
# COLUNAS DE INTERESSE E MAPEAMENTOS
# ==========================================================================

"""
Exemplo de colunas relevantes para a base de IES,
conforme dicionário do Censo 2023. Ajuste conforme desejar.
"""
COLUNAS_IES_RELEVANTES = [
    "CO_IES",
    "NO_IES",
    "TP_REDE",
    "TP_CATEGORIA_ADMINISTRATIVA",
    "QT_DOC_TOTAL",
    "QT_DOC_EXE",
    "QT_DOC_EX_FEMI",
    "QT_DOC_EX_MASC"
    # Adicione outras colunas se precisar (p. ex. QT_TEC_TOTAL, etc.)
]

MAPPING_IES = {
    "CO_IES": "id_ies",
    "NO_IES": "nome_ies",
    "TP_REDE": "tipo_rede",             # 1 = pública, 2 = privada
    "TP_CATEGORIA_ADMINISTRATIVA": "cat_adm",  # 1 = Fed, 2 = Est, etc.
    "QT_DOC_TOTAL": "docentes_total",
    "QT_DOC_EXE": "docentes_exercicio",
    "QT_DOC_EX_FEMI": "docentes_feminino",
    "QT_DOC_EX_MASC": "docentes_masculino"
}


"""
Exemplo de colunas relevantes para a base de Cursos,
conforme dicionário do Censo 2023. Ajuste conforme desejar.
"""
COLUNAS_CURSOS_RELEVANTES = [
    "CO_IES",
    "CO_CURSO",
    "NO_CURSO",
    "TP_MODALIDADE_ENSINO",
    "QT_CURSO",
    "QT_VG_TOTAL",
    "QT_INSCRITO_TOTAL",
    "QT_ING",
    "QT_MAT",
    "QT_CONC"
    # Adicione outras colunas se quiser (e.g. QT_ING_FEM, QT_MAT_18_24, etc.)
]

MAPPING_CURSOS = {
    "CO_IES": "id_ies",
    "CO_CURSO": "id_curso",
    "NO_CURSO": "nome_curso",
    "TP_MODALIDADE_ENSINO": "modalidade_ensino",  # 1=Presencial, 2=EAD
    "QT_CURSO": "numero_cursos",
    "QT_VG_TOTAL": "vagas_totais",
    "QT_INSCRITO_TOTAL": "inscritos_totais",
    "QT_ING": "ingressantes",
    "QT_MAT": "matriculados",
    "QT_CONC": "concluintes"
}


# ==========================================================================
# FUNÇÕES DE APOIO
# ==========================================================================

def registrar_problemas(arquivo, erro):
    """
    Registra problemas de leitura em um log.
    """
    with open("log_erros.txt", "a", encoding="utf-8") as log:
        log.write(f"Arquivo: {arquivo}, Erro: {erro}\n")


def carregar_csv(caminho_arquivo, sep=";", encoding="latin1"):
    """
    Carrega um CSV, tratando parsing e erros.
    """
    try:
        print(f"Lendo arquivo: {caminho_arquivo}")
        df = pd.read_csv(
            caminho_arquivo,
            sep=sep,
            encoding=encoding,
            on_bad_lines='skip',  # descarta linhas problemáticas
            low_memory=False
        )
        return df
    except pd.errors.ParserError as pe:
        print(f"Erro de parsing em {caminho_arquivo}: {pe}")
        registrar_problemas(caminho_arquivo, pe)
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro ao carregar {caminho_arquivo}: {e}")
        registrar_problemas(caminho_arquivo, e)
        return pd.DataFrame()


def filtrar_renomear(df, colunas_relevantes, mapping):
    """
    Seleciona apenas colunas relevantes e as renomeia conforme dicionário de mapeamento.
    """
    # Identifica somente colunas que existam no df
    existentes = [c for c in colunas_relevantes if c in df.columns]
    df_filtrado = df[existentes].copy()
    # Renomeia
    df_filtrado = df_filtrado.rename(columns=mapping)
    return df_filtrado


# ==========================================================================
# PROCESSAMENTO PRINCIPAL
# ==========================================================================
def main():
    # ----------------------------------------------------------------------
    # Verificar se os arquivos com nomes ajustados estão presentes
    # ----------------------------------------------------------------------
    caminho_ies = os.path.join(PASTA_BRUTO, "INEP_2023-MICRODADOS-CENSO",
                               "microdados_censo_da_educacao_superior_2023", "dados",
                               ARQUIVO_IES)
    caminho_cursos = os.path.join(PASTA_BRUTO, "INEP_2023-MICRODADOS-CENSO",
                                  "microdados_censo_da_educacao_superior_2023", "dados",
                                  ARQUIVO_CURSOS)

    df_ies_final = pd.DataFrame()
    df_cursos_final = pd.DataFrame()

    # ----------------------------------------------------------------------
    # Carregar e processar MICRODADOS_ED_SUP_IES_2023.CSV
    # ----------------------------------------------------------------------
    if os.path.isfile(caminho_ies):
        df_ies = carregar_csv(caminho_ies)
        if not df_ies.empty:
            df_ies_final = filtrar_renomear(df_ies, COLUNAS_IES_RELEVANTES, MAPPING_IES)
        else:
            print(f"Aviso: {ARQUIVO_IES} está vazio ou não pôde ser processado.")
    else:
        print(f"Aviso: Arquivo {ARQUIVO_IES} não encontrado em {caminho_ies}.")

    # ----------------------------------------------------------------------
    # Carregar e processar MICRODADOS_CADASTRO_CURSOS_2023.CSV
    # ----------------------------------------------------------------------
    if os.path.isfile(caminho_cursos):
        df_cursos = carregar_csv(caminho_cursos)
        if not df_cursos.empty:
            df_cursos_final = filtrar_renomear(df_cursos, COLUNAS_CURSOS_RELEVANTES, MAPPING_CURSOS)
        else:
            print(f"Aviso: {ARQUIVO_CURSOS} está vazio ou não pôde ser processado.")
    else:
        print(f"Aviso: Arquivo {ARQUIVO_CURSOS} não encontrado em {caminho_cursos}.")

    # ----------------------------------------------------------------------
    # Salvando resultados (IES e Cursos) na pasta "processado"
    # ----------------------------------------------------------------------
    if not df_ies_final.empty:
        saida_ies = os.path.join(PASTA_PROCESSADO, NOME_SAIDA_IES)
        os.makedirs(os.path.dirname(saida_ies), exist_ok=True)
        df_ies_final.to_csv(saida_ies, sep=";", index=False, encoding="utf-8")
        print(f"[OK] dados_ies gerado em: {saida_ies}")
    else:
        print("Nenhum dado de IES para salvar.")

    if not df_cursos_final.empty:
        saida_cursos = os.path.join(PASTA_PROCESSADO, NOME_SAIDA_CURSOS)
        os.makedirs(os.path.dirname(saida_cursos), exist_ok=True)
        df_cursos_final.to_csv(saida_cursos, sep=";", index=False, encoding="utf-8")
        print(f"[OK] dados_cursos gerado em: {saida_cursos}")
    else:
        print("Nenhum dado de Cursos para salvar.")


if __name__ == "__main__":
    main()