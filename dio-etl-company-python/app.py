import streamlit as st
import pandas as pd

st.set_page_config(page_title="DIO - ETL Company", layout="wide")

st.title("📊 Processamento de Dados: MySQL Azure + Python")
st.markdown("""
Este projeto replica o desafio de ETL da DIO, utilizando **Python e Streamlit** para transformar dados de uma base corporativa.
""")

# Simulação de conexão (Mock) para o GitHub não dar erro sem o banco ativo
def get_data():
    emp_data = {
        'Fname': ['James', 'Franklin', 'John', 'Jennifer'],
        'Lname': ['Borg', 'Wong', 'Smith', 'Wallace'],
        'Ssn': [888, 333, 123, 987],
        'Salary': [55000.0, 40000.0, 30000.0, 43000.0],
        'Super_ssn': [None, 888, 333, 888],
        'Dno': [1, 2, 3, 2]
    }
    dept_data = {
        'Dnumber': [1, 2, 3],
        'Dname': ['Sede', 'Administração', 'TI'],
        'Mgr_ssn': [888, 333, 987]
    }
    loc_data = {
        'Dnumber': [1, 2, 2, 3],
        'Dlocation': ['São Paulo', 'Rio', 'Niterói', 'Curitiba']
    }
    return pd.DataFrame(emp_data), pd.DataFrame(dept_data), pd.DataFrame(loc_data)

df_emp, df_dept, df_loc = get_data()

# --- ETAPAS DE TRANSFORMAÇÃO (O coração do desafio) ---

# 1. Mesclar Nome e Sobrenome
df_emp['Nome Completo'] = df_emp['Fname'] + " " + df_emp['Lname']

# 2. Mesclar Colaboradores e Departamentos (Inner Join)
df_merged = pd.merge(df_emp, df_dept, left_on='Dno', right_on='Dnumber')

# 3. Mesclar Departamentos e Localização (Combinação Única)
df_dept_loc = pd.merge(df_dept, df_loc, on='Dnumber')

# --- EXIBIÇÃO NO STREAMLIT ---
st.header("1. Dados Transformados (Merge Employee + Dept)")
st.dataframe(df_merged[['Nome Completo', 'Salary', 'Dname']])

st.header("2. Combinação Única: Departamento e Local")
st.write("Abaixo, a mescla que auxilia no futuro Modelo Estrela:")
st.table(df_dept_loc[['Dname', 'Dlocation']])

st.info("**Explicação Técnica:** Utilizamos 'Mesclar' (Merge) em vez de 'Atribuir' porque precisamos relacionar atributos de tabelas diferentes horizontalmente através de uma chave (ID). O 'Atribuir' apenas empilharia linhas, o que não cria o relacionamento necessário.")