# pip install streamlit requests

import streamlit as st
import requests

#URL da API Fastapi
API_URL = "http://127.0.0.1:8000/"

st.set_page_config(page_title="Filmes", layout="wide")

st.title("Gerenciador de Filmes")


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

elif menu == "Adicionar Filmes":
    st.subheader("➕ Adicionar filmes")
    titulo = st.text_input("Titulo Filme")
    genero = st.text_input("Genero do Filme")
    ano = st.number_input("Ano de Lançamento",min_value=900,max_value=2100,step=1)
    nota = st.number_input("Nota (0 a 10 )", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Salvar filme"):
        dados = {"titulo ":titulo,"genero":genero,"ano":ano,"nota":nota}
        response = requests.post(f"{API_URL}/filmes",params=dados)
        if response.status_code == 200:
            st.success("filme,e adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o filme")