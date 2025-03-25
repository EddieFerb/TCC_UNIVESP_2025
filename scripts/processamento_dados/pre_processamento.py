import os
import pandas as pd
import unicodedata
import re

# ==========================================================================
# CONFIGURAÇÕES GERAIS
# ==========================================================================

# Diretórios de entrada e saída (ajuste conforme sua estrutura)
PASTA_BRUTO = "./dados/bruto"
PASTA_PROCESSADO = "./dados/processado"

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


def corrigir_nome_pasta(caminho_base, ano):
    """
    Corrige possíveis problemas com caracteres especiais nos nomes das pastas extraídas.
    """
    caminho_esperado = os.path.join(caminho_base, f"INEP_{ano}-MICRODADOS-CENSO")
    
    if os.path.exists(caminho_esperado):
        for pasta in os.listdir(caminho_esperado):
            pasta_corrigida = unicodedata.normalize("NFKD", pasta).encode("ASCII", "ignore").decode("ASCII")
            pasta_corrigida = re.sub(r'[^a-zA-Z0-9_\- ]', '', pasta_corrigida)  # Remove caracteres especiais
            if "microdados" in pasta_corrigida.lower():
                return os.path.join(caminho_esperado, pasta)

    print(f"Aviso: Nenhuma pasta de microdados encontrada para {ano}")
    return None

def corrigir_nome_arquivo(nome_arquivo):
    """
    Corrige caracteres especiais no nome dos arquivos.
    """
    return re.sub(r'[^a-zA-Z0-9_\-\. ]', '', nome_arquivo)  # Remove caracteres inválidos


# ==========================================================================
# PROCESSAMENTO PRINCIPAL
# ==========================================================================
def main(year: int = 2024):
    # Listando os arquivos disponíveis no diretório
    arquivos_disponiveis = []
    caminho_base_ano = corrigir_nome_pasta(PASTA_BRUTO, year)
    caminho_dados = os.path.join(caminho_base_ano, "dados")

    if os.path.isdir(caminho_dados):
        arquivos_disponiveis = os.listdir(caminho_dados)

    # Normalizando nomes dos arquivos para evitar erros
    ARQUIVO_IES = f"MICRODADOS_ED_SUP_IES_{year}.CSV"
    ARQUIVO_CURSOS = f"MICRODADOS_CADASTRO_CURSOS_{year}.CSV"

    # Tentamos localizar um arquivo que contenha "IES" no nome, caso o padrão esperado não seja encontrado
    caminho_ies = None
    for arquivo in arquivos_disponiveis:
        nome_normalizado = corrigir_nome_arquivo(arquivo)
        if "IES" in nome_normalizado and "ED_SUP" in nome_normalizado:
            caminho_ies = os.path.join(caminho_dados, nome_normalizado)
            break  # Encontramos um nome válido

    # Caso não tenha sido encontrado, usaremos o nome padrão
    if caminho_ies is None:
        caminho_ies = os.path.join(caminho_dados, ARQUIVO_IES)

    # Log para depuração
    print(f"Arquivos encontrados em {caminho_dados}: {arquivos_disponiveis}")
    print(f"Arquivo IES esperado: {ARQUIVO_IES}")
    print(f"Arquivo IES identificado: {caminho_ies if os.path.exists(caminho_ies) else 'NÃO ENCONTRADO'}")

    df_ies_final = pd.DataFrame()
    df_cursos_final = pd.DataFrame()

    # ----------------------------------------------------------------------
    # Carregar e processar MICRODADOS_ED_SUP_IES_{year}.CSV
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
    # Carregar e processar MICRODADOS_CADASTRO_CURSOS_{year}.CSV
    # ----------------------------------------------------------------------
    caminho_cursos = os.path.join(caminho_dados, corrigir_nome_arquivo(ARQUIVO_CURSOS))
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
        saida_ies = os.path.join(PASTA_PROCESSADO, f"dados_ies_{year}.csv")
        os.makedirs(os.path.dirname(saida_ies), exist_ok=True)
        df_ies_final.to_csv(saida_ies, sep=";", index=False, encoding="utf-8")
        print(f"[OK] dados_ies gerado em: {saida_ies}")
    else:
        print("Nenhum dado de IES para salvar.")

    if not df_cursos_final.empty:
        saida_cursos = os.path.join(PASTA_PROCESSADO, f"dados_cursos_{year}.csv")
        os.makedirs(os.path.dirname(saida_cursos), exist_ok=True)
        df_cursos_final.to_csv(saida_cursos, sep=";", index=False, encoding="utf-8")
        print(f"[OK] dados_cursos gerado em: {saida_cursos}")
    else:
        print("Nenhum dado de Cursos para salvar.")


if __name__ == "__main__":
    for year in range(2011, 2024):
        print(f"\tProcessing year {year} ...")
        main(year)
