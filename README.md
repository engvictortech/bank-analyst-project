## 🚀 Análise de Clientes & Propensão a Cross-sell — Banking Edition ##

## Bem-vindo ao projeto de análise de clientes bancários! ## 
Aqui você encontrará um pipeline completo de ETL, EDA, modelagem e dashboard interativo para entender o comportamento do cliente e prever churn ou propensão a produtos. 💳📊

## 📁 Estrutura do Projeto

bank-analyst-project/

│

├─ data/

│   ├─ raw/               # Dados brutos (customers.csv, transactions.csv)

│   └─ processed/         # Agregados e features (monthly_agg.csv, features_table.csv)

│

├─ notebooks/             # Jupyter Notebooks (.ipynb)

│

├─ dashboards/            # Streamlit app

│   └─ streamlit_app.py

│

├─ models/                # Modelos treinados (.pkl, .json)

│

├─ requirements.txt       # Dependências Python

└─ README.md

## 🛠 Etapas do Pipeline

| Passo | Descrição                    | Emoji |
|-------|------------------------------|-------|
| 1     | Data Prep & ETL              | ⚡    |
| 2     | Feature Engineering          | ✨    |
| 3     | Exploração de Dados (EDA)    | 🔍    |
| 4     | Modelagem de Propensão       | 🧠    |
| 5     | Simulação de Campanhas       | 💰    |
| 6     | Dashboard Interativo         | 📈    |
| 7     | Publicação no GitHub         | 🌐    |

## 📊    Principais Resultados

### AUC XGBoost: 
0.85 ✅

### Segmento VIP: 
ARPU médio = R$ 1.200 💎

### Insight: 
Clientes com mais produtos têm menor risco de churn.

## 🛠 Principais Etapas do Pipeline

### Geração de dados sintéticos 🧬
Criação de customers.csv e transactions.csv para simulação do banco de dados.

### Data Prep & ETL ⚡
Limpeza, normalização e agregação mensal (monthly_agg.csv).

### Feature Engineering ✨
Construção de variáveis RFM, produtos ativos, churn 90 dias, idade e outras (features_table.csv).

### Exploração de Dados (EDA) 🔍
Histogramas, boxplots, correlações, cohort analysis e insights de comportamento.

### Modelagem de Propensão 🧠
Treinamento de Logistic Regression e XGBoost. Avaliação via AUC e precision@K.

### Simulação de Campanhas 💰
Seleção dos top-K clientes propensos para campanha e cálculo de receita incremental.

### Dashboard Interativo 📈
Visualização de KPIs, churn, ARPU e segmentação por cidade e coorte usando Streamlit.

## Publicação GitHub 🌐
Notebooks, dashboards, modelos e documentação para fácil reprodução.

## 📊 Resultados Principais

### AUC do XGBoost:   
X.XX

### Insight:
Clientes com mais produtos têm menor risco de churn.

### Segmento VIP:
ARPU médio = R$Y, alta propensão a produtos premium

## ⚡ Como Rodar Localmente

### Clone o repositório:

#### git clone <link-do-repo>
cd bank-analyst-project


#### Instale dependências:

pip install -r requirements.txt


#### Execute notebooks para reproduzir análises:

jupyter notebook


#### Rode o dashboard interativo:

streamlit run dashboards/streamlit_app.py

## 📌 Observações

Arquivos de dados (data/raw/ e data/processed/) não são versionados no GitHub.

Modelos salvos em models/.

Documente suposições, 
#### como janela de churn, ticket médio e parâmetros da campanha no README.

## 🤝 Contato

### LinkedIn: 
[https://www.linkedin.com/in/engvictortech/] 

### E-mail: 
[engvictortech@gmail.com]
