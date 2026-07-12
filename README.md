# Modelo de projeto de ciência de dados

# 📊 Previsão de Rotatividade de Funcionários (Employee Attrition)

![Capa do projeto](/imagens/Streamlit_Model.png)

## 📖 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de analisar os fatores que influenciam a saída de funcionários de uma empresa (Attrition) utilizando técnicas de Ciência de Dados e Machine Learning.

O trabalho foi dividido em duas etapas principais:

- Análise Exploratória dos Dados (EDA)
- Construção de um modelo de Machine Learning capaz de prever a probabilidade de um funcionário deixar a empresa.

O projeto foi desenvolvido como prática dos conceitos estudados durante minha graduação em Ciência de Dados.

---

# 🎯 Objetivo

A rotatividade de funcionários gera custos elevados para qualquer empresa.

Com este projeto, busquei responder perguntas como:

- Quais características estão mais relacionadas à saída de funcionários?
- Existe algum padrão entre colaboradores que pedem desligamento?
- É possível prever, com Machine Learning, quais funcionários possuem maior risco de sair da empresa?

## Organização do projeto

```

├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto
├── README.md          <- Resumo do projeto destacando pontos chaves.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── modelos            <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
|
├── notebooks          <- Cadernos Jupyter. A convenção de nomenclatura é um número (para ordenação),
│                         as iniciais do criador e uma descrição curta separada por `-`
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── auxiliares.py <- organizar e visualizar o impacto de cada feature no modelo de MachineLearning
|      ├── config.py    <- Configurações básicas do projeto
|      └── graficos.py  <- Scripts para criar visualizações exploratórias e orientadas a resultados
|      └── models_rus.py <- Scripts para ajustar desbalanceamento da base de dados.
|      └── models.py    <- Scripts para criação de pipelines e treinamento de modelos Machine Learning.
|
├── referencias        <- Dicionários de dados, manuais e todos os outros materiais explicativos.
|
```

# 🔍 Etapa 1 — Análise Exploratória dos Dados

![Capa do projeto](imagens/EDA_01.png)

Nesta etapa foram realizadas análises para compreender melhor a base de dados.

Foram investigados:

- valores ausentes
- tipos de dados
- estatísticas descritivas
- distribuição das variáveis
- correlação entre atributos
- comparação entre funcionários que permaneceram e os que deixaram a empresa
- criação de gráficos para identificar padrões

Essa etapa foi fundamental para entender quais variáveis poderiam contribuir para o modelo de Machine Learning.

---

# 🤖 Etapa 2 — Machine Learning

![Capa do projeto](imagens/ML_01.png)

Após o tratamento dos dados foi desenvolvido um pipeline completo contendo:

- tratamento de variáveis categóricas
- normalização das variáveis numéricas
- transformação das features
- treinamento do modelo
- avaliação dos resultados

Todo o pré-processamento foi realizado utilizando Pipeline e ColumnTransformer do Scikit-Learn.

Isso garante que os mesmos tratamentos aplicados durante o treinamento também sejam utilizados quando novos dados forem inseridos no modelo.

---

# 🛠 Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Jupyter Notebook

---

# 📈 Fluxo do Projeto

```text
Base de Dados
       │
       ▼
Análise Exploratória
       │
       ▼
Tratamento dos Dados
       │
       ▼
Engenharia de Atributos
       │
       ▼
Treinamento do Modelo
       │
       ▼
Avaliação
       │
       ▼
Predição
```

---

# 💡 Principais Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Limpeza de dados
- Análise Exploratória
- Visualização de Dados
- Engenharia de Features
- Pré-processamento
- Machine Learning
- Construção de Pipelines
- Avaliação de modelos
- Organização de projetos de Ciência de Dados

---

# 👨‍💻 Autor

**Vitor Chaves**

Graduando em Ciência de Dados.

Sempre buscando desenvolver projetos que unam análise de dados, Machine Learning e resolução de problemas reais.


