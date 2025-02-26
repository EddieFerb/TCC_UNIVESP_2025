library(dplyr)
library(plotly)

dados_cursos_tratado  <- read.csv2(file = 'informacao/informacao/dados/processado/dados_cursos_tratado.csv')
dados_ies_tratado     <- read.csv2(file = 'informacao/informacao/dados/processado/dados_ies_tratado.csv')

# Prepare Data
all_data <- dados_cursos_tratado |> 
  dplyr::left_join(dados_ies_tratado, by = dplyr::join_by("id_ies")) |> 
  dplyr::mutate(ano = 2023) |> 
  dplyr::filter(numero_cursos > 0)

# Clean Data
all_data <- all_data |>
  dplyr::mutate(
    tipo_rede = dplyr::case_when(
      tipo_rede == "1" ~ "Pública",
      tipo_rede == "2" ~ "Privada",
      TRUE ~ "Outro"),
    cat_adm = dplyr::case_when(
      cat_adm == "1" ~ "Federal",
      cat_adm == "2" ~ "Estadual",
      TRUE ~ "Outro"),
    modalidade_ensino = dplyr::case_when(
      modalidade_ensino == "1" ~ "Presencial",
      modalidade_ensino == "2" ~ "EAD",
      TRUE ~ "Outro"))

# Insights
most_courses <- all_data |> 
  dplyr::group_by(nome_curso) |> 
  dplyr::summarise(ies_ofertantes = n()) |> 
  dplyr::arrange(dplyr::desc(ies_ofertantes))

top10_most_courses <- most_courses |> 
  head(10)

unique_courses_in_one_only_ies <- most_courses |> 
  dplyr::filter(ies_ofertantes == 1) |> 
  nrow()

type_courses <- all_data |> 
  dplyr::group_by(modalidade_ensino) |> 
  dplyr::summarise(ies_ofertantes = n()) |> 
  dplyr::arrange(dplyr::desc(ies_ofertantes))

insights_data <- all_data |> 
  dplyr::mutate(
    pessoas_por_vaga = round(inscritos_totais / ifelse(vagas_totais == 0, 1, vagas_totais), 2)
  ) |> 
  dplyr::select(nome_ies, nome_curso, modalidade_ensino, vagas_totais, inscritos_totais, pessoas_por_vaga, ingressantes, matriculados, concluintes)

