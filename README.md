# 📊 Desafio de ETL: Integrando MySQL Azure com Python & Streamlit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dio-powerbi-etl-python.streamlit.app/)

Este repositório contém a resolução do desafio de projeto **"Processamento de Dados Simplificado com Power BI"**, parte da formação Power BI Analyst da [DIO](https://www.dio.me/). 

> **Diferencial Técnico:** Como alternativa ao Power BI, utilizei a stack **Python + Pandas + Streamlit** para realizar todo o processo de ETL (Extração, Transformação e Carregamento), demonstrando habilidades de engenharia de dados e criação de Data Apps.

## 🔗 Link para Visualização
Acesse o projeto publicado aqui: [https://dio-powerbi-etl-python.streamlit.app/](https://dio-powerbi-etl-python.streamlit.app/)

---

## 🛠️ Etapas do Projeto

### 1. Configuração na Nuvem (Azure)
- Instância de banco de dados **MySQL** criada na plataforma **Azure**.
- Configuração de regras de Firewall para permitir conexões externas.
- Criação e população do banco de dados "Company" através de scripts SQL.

### 2. Processo de ETL (Transformação de Dados)
Utilizando a biblioteca **Pandas**, realizei as seguintes limpezas solicitadas no desafio:
- **Tratamento de Nulos:** Identificação de colaboradores sem gerente (CEOs/Diretores).
- **Padronização Monetária:** Conversão de salários para tipos decimais precisos.
- **Mesclagem de Colunas:** Criação da coluna `Nome Completo` (Nome + Sobrenome).
- **Joins (Mesclas):** - Junção de colaboradores e departamentos para identificar onde cada um trabalha.
    - Associação de colaboradores aos seus respectivos gerentes.
    - Criação de uma tabela única para **Departamento-Localização** para facilitar o modelo estrela.

### 3. Respondendo ao Desafio Teórico
**Pergunta:** Por que, no caso de Departamentos e Localização, usamos "Mesclar" (Merge) e não "Atribuir/Acrescentar" (Append)?

**Resposta:** No processamento de dados, o **Merge (Mesclar)** funciona como um `JOIN` do SQL; ele combina colunas de tabelas diferentes baseando-se em uma chave comum (como o ID do departamento). Isso é necessário porque as informações de "Nome do Departamento" e "Cidade" são atributos complementares de uma mesma entidade. Já o **Append (Acrescentar)** empilha linhas verticalmente, o que só faria sentido se tivéssemos duas listas de departamentos diferentes para unir em uma só.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.10+**
- **Pandas** (Manipulação de dados)
- **Streamlit** (Interface e visualização)
- **MySQL / Azure** (Armazenamento de dados)

## 📂 Como executar localmente
1. Clone o repositório: `git clone https://github.com/SEU_USUARIO/dio-etl-company-python.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o app: `streamlit run app.py`

---
Desenvolvido como parte da Formação Power BI Analyst da DIO.
