import streamlit as st

st.title("🏡 Adoção")

animal = st.text_input("Nome do Animal")

nome_adotante = st.text_input(
    "Nome do Adotante"
)

telefone = st.text_input(
    "Telefone"
)

email = st.text_input(
    "E-mail"
)

endereco = st.text_area(
    "Endereço"
)

data_adocao = st.date_input(
    "Data da Adoção"
)

observacoes = st.text_area(
    "Observações"
)

if st.button("Registrar Adoção"):
    st.success("Adoção registrada!")