import streamlit as st

st.title("Cadastro de Animal")

foto = st.file_uploader(
    "Foto do animal",
    type=["jpg", "jpeg", "png"]
)

if foto:
    st.image(foto, width=250)

nome = st.text_input("Nome")

especie = st.selectbox(
    "Espécie",
    ["Cão", "Gato", "Coelho"]
)

sexo = st.selectbox(
    "Sexo",
    ["Macho", "Fêmea"]
)

raca = st.text_input("Raça")

idade = st.number_input(
    "Idade",
    min_value=0
)

cor = st.text_input("Cor")

porte = st.selectbox(
    "Porte",
    ["Pequeno", "Médio", "Grande"]
)

castrado = st.checkbox("Castrado")

observacoes = st.text_area(
    "Observações"
)

if st.button("Salvar Animal"):
    st.success("Animal cadastrado com sucesso!")