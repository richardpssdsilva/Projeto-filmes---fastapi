# pip install streamlit requests

import streamlit as st
import requests

#URL da API Fastapi
API_URL = "http://127.0.0.1:8000/"

st.set_page_config(page_title="Filmes")

st.title("Gerenciador de Filmes",layout="wide")


menu = st.sidebar.radio("Navegação",
    ["Listar Filmes","Adicionar Filmes"]
    )
if menu == "Listar Filmes":
    st.subheader("Filmes em Geral")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        st.write("Sucesso !!")
        filmes = response.json().get("filmes",[])
        if filmes:
            st.dataframe(filmes)
        else:
            st.info("Nemhum filme cadastrado ainda!")
    else:
        st.error("Erro de conexão com a API.")
elif menu == "Cadastrar Filmes":
    st.subheader("➕ Adicionar filmes")