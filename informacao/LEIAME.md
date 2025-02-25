Informacao-UEL/
├── dados/
│   ├── bruto/
│   │   ├── INEP_1995-2022-MICRODADOS-CENSO /
│   │   │    └── DADOS
│   │   │    └── Leia-me
│   │   └── INEP_1995-2022-MICRODADOS-ZIP
│   │   
│   ├── processado/
│   │   ├── ies_dados_limpos.csv
│   │   └── caracteristicas_selecionadas.csv
│   ├── externo/
│   │   └── inep_dados_2020.csv
│   └── intermediario/
│       └── dados_temp.pkl
├── notebooks/
│   ├── exploracao_dados/
│   │   └── exploracao_dados.ipynb
│   ├── pre_processamento/
│   │   └── limpeza_dados.ipynb
│   ├── modelagem/
│   │   ├── treinamento_modelo.ipynb
│   │   └── ajuste_hiperparametros.ipynb
│   └── analise_resultados/
│       └── visualizacao_resultados.ipynb
├── scripts/
│   ├── coleta_dados/
│   │   └── coleta_dados_oficiais.py
│   ├── processamento_dados/
│   │   └── pre_processamento.py
│   ├── modelagem/
│   │   └── treinamento_modelo.py
│   └── visualizacao/
│       └── gerar_graficos.py
├── modelos/
│   ├── modelos_salvos/
│   │   └── modelo_random_forest.pkl
│   └── resultados_modelos/
│       ├── metricas.txt
│       └── matriz_confusao.png
├── relatorios/
│   ├── figuras/
│   │   ├── figura1.png
│   │   └── figura2.png
│   ├── tabelas/
│   │   └── tabela1.csv
│   └── logs/
│       └── log_treinamento.txt
├── artigo/
│   ├── manuscrito/
│   │   ├── artigo.docx
│   │   ├── secoes/
│   │   │   ├── introducao.docx
│   │   │   ├── metodologia.docx
│   │   │   └── resultados.docx
│   │   ├── referencias/
│   │   │   └── referencias.bib
│   │   └── figuras/
│   │       ├── figura1.tif
│   │       └── figura2.tif
│   └── submissao/
│       ├── artigo_final.docx
│       └── checklist_submissao.pdf
├── documentos/
│   └── diagramas/
│       └── fluxo_dados.png
├── ambiente/
│   ├── requisitos.txt
│   └── ambiente.yml
├── LEIAME.md
└── LICENCA

# Análise de Dados Acadêmicos de IES Públicas de SP e PR

Este projeto tem como objetivo desenvolver uma aplicação para análise de dados acadêmicos de Instituições de Ensino Superior (IES) públicas dos estados de São Paulo (SP) e Paraná (PR), utilizando técnicas avançadas de Inteligência Artificial (IA), Aprendizado de Máquina (AM), Aprendizado Profundo (AP) e Redes Neurais Artificiais (RNA).

## Estrutura do Projeto

- `dados/`: Contém os dados utilizados no projeto.
  - `bruto/`: Dados brutos coletados.
  - `processado/`: Dados após limpeza e pré-processamento.
  - `externo/`: Dados provenientes de fontes externas.
  - `intermediario/`: Dados temporários durante o processamento.
- `notebooks/`: Notebooks Jupyter para exploração e desenvolvimento.
- `scripts/`: Scripts Python para automação de tarefas.
- `modelos/`: Modelos treinados e resultados associados.
- `relatorios/`: Recursos para relatórios e apresentações.
- `artigo/`: Manuscrito do artigo científico e documentos para submissão.
- `documentos/`: Documentação adicional e diagramas.
- `ambiente/`: Arquivos relacionados ao ambiente de desenvolvimento.
- `LEIAME.md`: Este arquivo, com informações sobre o projeto.
- `LICENCA`: Informações sobre a licença do projeto.

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Anaconda ou Miniconda para gerenciamento de ambiente (recomendado)

### Configuração do Ambiente

#### Usando Conda

Crie o ambiente a partir do arquivo `ambiente/ambiente.yml`:

```bash
conda env create -f ambiente/ambiente.yml
conda activate informacao_env


Utilização da Estrutura de Pastas

	•	Armazenamento de Dados:
	•	Armazene os dados brutos em dados/bruto/ e utilize-os como base para gerar os dados processados em dados/processado/.
	•	Notebooks:
	•	Use os notebooks localizados em notebooks/ para experimentação e desenvolvimento iterativo.
	•	Após estabilizar o código nos notebooks, converta-o para scripts e organize-os na pasta scripts/.
	•	Modelos:
	•	Salve os modelos treinados em modelos/modelos_salvos/ para reutilização.
	•	Registre os resultados de desempenho dos modelos na pasta modelos/resultados_modelos/.

Para o Artigo:

	•	Centralização:
	•	Centralize todo o trabalho relacionado ao manuscrito na pasta artigo/.
	•	Versões Separadas:
	•	Mantenha arquivos separados para rascunho e versão final do artigo, organizados dentro de artigo/manuscrito/.
	•	Figuras e Tabelas:
	•	Armazene figuras e tabelas no formato exigido pela revista em artigo/manuscrito/figuras/.
	•	Documentos para Submissão:
	•	Utilize artigo/submissao/ para guardar os documentos necessários para a submissão, como a versão final do artigo e a checklist de submissão.



    Benefícios desta Estrutura

	•	Organização: Facilita a localização de arquivos e mantém o projeto estruturado.
	•	Reprodutibilidade: Com uma estrutura clara e arquivos de ambiente bem definidos, outras pessoas podem reproduzir seus resultados.
	•	Colaboração: Se estiver trabalhando com outras pessoas, uma estrutura padrão ajuda na colaboração e evita conflitos.
	•	Preparação para o Mestrado: Esta estrutura pode ser facilmente expandida e adaptada para o desenvolvimento futuro do projeto durante o mestrado.


    Dicas Finais

	•	Backup Regular: Faça backups regulares, especialmente dos dados e do artigo.
	•	Controle de Versão: Utilize o Git e considere hospedar o repositório em plataformas como GitHub ou GitLab (lembrando de não tornar público dados sensíveis).
	•	Automatização: Considere criar scripts de automação para tarefas repetitivas, como atualização de dados ou treinamento de modelos.
	•	Conformidade com a Revista: Verifique sempre as diretrizes da revista Informação & Informação para garantir que o formato dos arquivos (especialmente figuras e tabelas) está conforme as especificações.

# **Análise de Dados Acadêmicos do INEP/MEC – MVP 2023**  

Este projeto tem como objetivo desenvolver uma aplicação para análise de dados acadêmicos de Instituições de Ensino Superior (IES) **com base nos microdados do Censo da Educação Superior do INEP/MEC**. A primeira fase do projeto (MVP) foca exclusivamente nos **dados do ano de 2023**, permitindo uma implementação controlada e iterativa antes de expandir para séries históricas.

## **Alteração de Escopo**  
**ANTES:** O projeto analisaria dados de **1995 a 2023**.  
**AGORA:** O escopo foi reduzido para **APENAS O ANO DE 2023**, conforme decisão da equipe para viabilizar um MVP funcional. A expansão para anos anteriores será feita **gradualmente**, após validação dos resultados do MVP.  

---

## **Execução do MVP**
1. **Coleta de Dados**
   - **O projeto não usa mais raspagem de dados (web scraping).**
   - **Os microdados do INEP 2023 são baixados diretamente da fonte oficial e armazenados em `dados/bruto/`**.
   - **Arquivos principais:**
     - `MICRODADOS_ED_SUP_IES_2023.CSV`
     - `MICRODADOS_CADASTRO_CURSOS_2023.CSV`
   - Executar os scripts para tratamento dos dados:
     ```bash
	 python ./informacao/scripts/coleta_dados/coletar_links_inep.py
     python ./informacao/scripts/coleta_dados/coleta_dados_oficiais.py
     ```

2. **Pré-processamento e Análise Exploratória**
   - Executar os scripts para tratamento dos dados:
     ```bash
     python ./informacao/scripts/processamento_dados/pre_processamento.py
     python ./informacao/scripts/processamento_dados/processamento_dados/tratar_dados.py
     ```
   - **O tratamento de dados foi ajustado para lidar apenas com 2023**.  

# TODO: Fazer a modelagem e análises exploratórias
3. **Modelagem e Treinamento do Modelo**
	**Principais Arquivos a serem utilizados**
	- dados_cursos_tratado.csv
	- dados_ies_tratado.csv

   - **Agora o modelo é treinado somente com os dados de 2023**:
     ```bash
     python scripts/modelagem/treinamento_modelo.py
     ```
   - A avaliação é feita com:
     ```bash
     python scripts/visualizacao/gerar_graficos.py
     ```

---

## **Dados Utilizados no MVP**  
**ANTES:** O projeto processaria **dados de 1995 a 2023**.  
**AGORA:** O projeto foca **APENAS NO ANO DE 2023**, incluindo os seguintes arquivos:
  - `MICRODADOS_ED_SUP_IES_2023.CSV`
  - `MICRODADOS_CADASTRO_CURSOS_2023.CSV`
  - `dados_ies_tratado.csv`
  - `dados_cursos_tratado.csv`
  - `taxas_ingresso_evasao_conclusao.csv`

Esses arquivos foram ajustados para conter apenas informações de **ingresso, evasão e conclusão**.

---

## **Scripts Atualizados**
### **1. Coleta de Dados**  
   **ANTES:** Raspagem de dados via `raspagem_web.py`.  
   **AGORA:** Os dados são baixados diretamente das fontes oficiais e processados com:
   ```bash
   python scripts/coleta_dados/coletar_links_inep.py
   python scripts/coleta_dados/coleta_dados_oficiais.py
   ```
   **Web scraping foi removido.**

### **2. Pré-processamento e Tratamento**
   - **ANTES:** Unificação de dados de múltiplos anos.  
   - **AGORA:** Apenas os dados de **2023** são processados:
     ```bash
     python scripts/processamento_dados/pre_processamento.py
     python scripts/processamento_dados/tratar_dados.py
     ```

### **3. Modelagem e Avaliação**
   - **ANTES:** Modelos baseados em séries históricas.  
   - **AGORA:** Modelo treinado **exclusivamente com dados de 2023**.  
   ```bash
   python scripts/modelagem/treinamento_modelo.py
   python scripts/visualizacao/gerar_graficos.py
   ```

---

## **Próximos Passos**
1. **Validar resultados do MVP**: Garantir que o pipeline está funcional e coerente.  
2. **Aprimorar visualizações e métricas**: Refinar análises e gráficos no `visualizacao_resultados.ipynb`.  
3. **Expansão gradual**: Após validar os dados de 2023, expandir para séries históricas (anos anteriores).  

---

## **Benefícios da Mudança de Escopo**
✅ **Maior viabilidade:** Processo mais enxuto e testável.  
✅ **Melhor organização:** Dados de um único ano garantem mais controle e menos ruído.  
✅ **Facilidade de expansão:** Depois de validado, será mais simples incluir novos anos.  

---

### **Conclusão**
O projeto agora se concentra na análise **dos microdados do Censo da Educação Superior 2023**, permitindo um MVP funcional. Após rodar satisfatoriamente, podemos escalar para incluir múltiplos anos gradualmente.  

---


___________________________________________________________________________

# Execução do Projeto
# 1.	Coleta de Dados
# Execute os scripts para coletar os dados:
# python scripts/coleta_dados/coletar_links_inep.py
# python scripts/coleta_dados/coleta_dados_oficiais

# 2.	Pré-processamento, Limpeza e EDA
# Execute os scripts de pré-processamento:
# python scripts/processamento_dados/pre_processamento.py
# python scripts/tratar_dados/pre_processamento.py
# 	2.1	Análise Exploratória (EDA – Exploratory Data Analysis)
# 	•	No notebook exploracao_dados.ipynb, rodamos algumas análises estatísticas básicas, histogramas (para taxa de evasão, por exemplo), e correlações.
# 	•	Verificável possíveis outliers e valores ausentes, ajustando conforme preciso.
# 	2.2 Modelagem Inicial
# 	•	No notebook ajuste_hiperparametros.ipynb, teste hiperparâmetros de um modelo (Random Forest).
# 	•	No notebook treinamento_modelo.ipynb, treinamos a versão final do Random Forest e salvamos o modelo (via joblib).
# 	2.3 Análise dos Resultados
# 	•	No notebook visualizacao_resultados

# 3.	Treinamento do Modelo
# Treine o modelo de aprendizado de máquina:
# python scripts/modelagem/treinamento_modelo.py

# 4.	Geração de Gráficos
# Gere visualizações dos resultados:
# python scripts/visualizacao/gerar_graficos.py


# 5. Dados

# 5.1. Estrutura dos Dados

# Os arquivos CSV em dados/bruto/ contêm os dados brutos coletados das IES. As colunas incluem:
# 	•	nome: Nome da instituição.
# 	•	endereco: Endereço da instituição.
# 	•	cidade: Cidade onde a instituição está localizada.
# 	•	estado: Estado onde a instituição está localizada.
# 	•	telefone: Telefone de contato.
# 	•	numero_alunos: Número total de alunos matriculados.
# 	•	taxa_evasao: Taxa de evasão dos cursos.
# 	•	Outras colunas relevantes conforme a disponibilidade dos dados.

# 6. Scripts

# 6.1. coleta_dados_oficiais.py

# Caminho: informacao/scripts/coleta_dados_oficiais.py

# Descrição: Para coletar dados sobre taxas de ingresso, evasão e conclusão de universitários, é mais eficiente utilizar fontes de dados abertos fornecidas por instituições oficiais, como o Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) e o Ministério da Educação (MEC). Essas instituições disponibilizam microdados detalhados que podem ser acessados diretamente, eliminando a necessidade de web scraping.
# Script para coletar dados das IES utilizando web scraping.


# 6.2. pre_processamento.py

# Caminho: informacao/scripts/processamento_dados/pre_processamento.py

# Descrição: Script para limpar e preparar os dados para modelagem.

# 6.3. treinamento_modelo.py

# Caminho: informacao/scripts/modelagem/treinamento_modelo.py

# Descrição: Script para treinar o modelo de aprendizado de máquina.

# 6.4. gerar_graficos.py

# Caminho: informacao/scripts/visualizacao/gerar_graficos.py

# Descrição: Script para gerar gráficos e visualizações dos resultados.

# Notebooks

# 6.5. exploracao_dados.ipynb

# Caminho: informacao/notebooks/exploracao_dados/exploracao_dados.ipynb

# Descrição: Notebook para análise exploratória dos dados (EDA).

# 6.6. limpeza_dados.ipynb

# Caminho: informacao/notebooks/pre_processamento/limpeza_dados.ipynb

# Descrição: Notebook para limpeza e pré-processamento dos dados.

# 6.7. treinamento_modelo.ipynb

# Caminho: informacao/notebooks/modelagem/treinamento_modelo.ipynb

# Descrição: Notebook para treinamento do modelo de aprendizado de máquina.

# 6.8. ajuste_hiperparametros.ipynb

# Caminho: informacao/notebooks/modelagem/ajuste_hiperparametros.ipynb

# Descrição: Notebook para ajuste de hiperparâmetros do modelo.

# 6.9. visualizacao_resultados.ipynb

# Caminho: informacao/notebooks/analise_resultados/visualizacao_resultados.ipynb

# Descrição: Notebook para análise e visualização dos resultados obtidos.


# 7. Modelos

# 7.1. modelo_random_forest.pkl

# Caminho: informacao/modelos/modelos_salvos/modelo_random_forest.pkl

# Descrição: Arquivo contendo o modelo Random Forest treinado. Este arquivo é gerado pelo script treinamento_modelo.py ou pelo notebook correspondente.


# 8. Relatórios

# 8.1. metricas.txt

# Caminho: informacao/modelos/resultados_modelos/metricas.txt

# Descrição: Arquivo de texto com as métricas de desempenho do modelo.

# 8.2. log_treinamento.txt

# Caminho: informacao/relatorios/logs/log_treinamento.txt

# Descrição: Arquivo de log do processo de treinamento do modelo.

# 9. Documentos

# 9.1. fluxo_dados.png

# Caminho: informacao/documentos/diagramas/fluxo_dados.png

# Descrição: Diagrama do fluxo de dados do projeto, desde a coleta até a visualização.

# Nota: Como não é possível inserir imagens aqui, sugiro que crie um diagrama representando as etapas:
# 	1.	Coleta de Dados
# 	2.	Pré-processamento
# 	3.	Modelagem
# 	4.	Avaliação
# 	5.	Visualização de Resultados

# Observações Finais

# 	•	Integração da Aplicação: Os scripts e notebooks fornecidos estão interligados conforme o fluxo de trabalho do projeto. Certifique-se de que os caminhos relativos nos scripts correspondam à estrutura de pastas.
# 	•	Dados Sensíveis: Ao trabalhar com dados reais, assegure-se de estar em conformidade com as leis de proteção de dados, como a LGPD.
# 	•	Atualizações Necessárias: Alguns códigos utilizam URLs de exemplo ou estruturas genéricas. Você precisará ajustá-los de acordo com as fontes de dados reais e a estrutura dos sites ou APIs que irá utilizar.
# 	•	Dependências Adicionais: Se utilizar bibliotecas ou ferramentas adicionais, lembre-se de adicioná-las aos arquivos de requisitos (requisitos.txt ou ambiente.yml).
# 	•	Testes e Validações: Recomendo executar cada script individualmente para verificar se funcionam conforme esperado e realizar testes unitários onde possível.


# Com base na sua estrutura e no foco do projeto (ingresso, evasão e conclusão de cursos pelos alunos), aqui está uma recomendação sobre os dados e tabelas mais importantes a serem utilizadas nas etapas de pré-processamento, treinamento e visualização dos resultados:

# Tabelas mais relevantes

# 	1.	GRADUACAO_PRESENCIAL.CSV / GRADUACAO_DISTANCIA.CSV:
# 	•	Informações detalhadas sobre os alunos matriculados, concluídos e evadidos em cursos presenciais ou a distância.
# 	•	Dados importantes:
# 	•	Matrículas por curso e ano.
# 	•	Taxas de evasão e conclusão por curso.
# 	•	Distribuição de alunos por modalidade (presencial e a distância).
# 	2.	FORME_PRESENCIAL.CSV / FORME_DISTANCIA.CSV:
# 	•	Dados sobre os ingressantes nos cursos superiores.
# 	•	Dados importantes:
# 	•	Número de ingressantes por curso e ano.
# 	•	Comparação entre modalidades (presencial e a distância).
# 	3.	SECOMPLE_PRESENCIAL.CSV / SECOMPLE_DISTANCIA.CSV:
# 	•	Informações sobre os alunos que concluíram os cursos.
# 	•	Dados importantes:
# 	•	Taxas de conclusão por curso e modalidade.
# 	•	Comparação temporal (1995-2022).
# 	4.	INSTITUICAO.CSV:
# 	•	Dados sobre as instituições de ensino.
# 	•	Dados importantes:
# 	•	Localização geográfica (estado, cidade).
# 	•	Tipo de instituição (pública/privada).
# 	•	Número total de alunos por instituição.
# 	5.	MICRODADOS_CADASTRO_CURSOS_XXXX.CSV (Anos mais recentes):
# 	•	Informações mais detalhadas sobre cursos.
# 	•	Dados importantes:
# 	•	Número de cursos ativos por instituição.
# 	•	Distribuição de alunos por tipo de curso (bacharelado, licenciatura, tecnólogo).
# 	6.	MICRODADOS_CADASTRO_IES_XXXX.CSV (Anos mais recentes):
# 	•	Informações gerais das instituições de ensino superior.
# 	•	Dados importantes:
# 	•	Tamanho da instituição.
# 	•	Tipos de cursos oferecidos.

# 	Etapas do projeto

# 	1.	Pré-processamento:
# 	•	Unificar dados:
# 	•	Combine tabelas de diferentes anos para gerar séries temporais (e.g., número de ingressantes por ano).
# 	•	Lidar com dados ausentes:
# 	•	Substituir valores ausentes ou criar categorias “desconhecidas”.
# 	•	Gerar métricas:
# 	•	Criar colunas com taxas (e.g., taxa de evasão = número de evadidos / total de matrículas).
# 	•	Filtrar dados relevantes:
# 	•	Focar apenas em cursos de graduação.
# 	•	Considerar apenas instituições e cursos com dados completos.
# 	2.	Treinamento:
# 	•	Variáveis independentes (features):
# 	•	Ano.
# 	•	Tipo de curso (presencial, distância).
# 	•	Tipo de instituição (pública, privada).
# 	•	Localização geográfica.
# 	•	Variável dependente (target):
# 	•	Taxa de evasão.
# 	•	Taxa de conclusão.
# 	3.	Visualização de resultados:
# 	•	Gráficos de linha:
# 	•	Evolução temporal do número de ingressantes, concluintes e evadidos.
# 	•	Mapas geográficos:
# 	•	Distribuição de instituições e suas taxas de evasão/conclusão por estado.
# 	•	Gráficos de barras:
# 	•	Comparação entre modalidades (presencial x distância).

# 	Estratégia para organizar os dados

# 	1.	Pasta de dados processados:
# 	•	Criar arquivos consolidados para cada métrica:
# 	•	taxas_ingresso_evasao_conclusao.csv: Contendo séries temporais para cada curso e instituição.
# 	•	instituicoes_resumo.csv: Resumo de instituições (localização, tipo, número de cursos).
# 	•	Gerar indicadores normalizados (e.g., taxas de evasão e conclusão como porcentagens).
# 	2.	Scripts recomendados:
# 	•	Unificação:
# 	•	Script para consolidar dados de múltiplos arquivos CSV em um único DataFrame.
# 	•	Análise temporal:
# 	•	Script para calcular métricas anuais (e.g., médias, medianas).
# 	•	Visualização:
# 	•	Scripts para gerar gráficos diretamente a partir dos dados processados.

# Esta abordagem maximiza a utilização dos microdados, atendendo ao foco do projeto em ingresso, evasão e conclusão dos cursos.