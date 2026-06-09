import streamlit as st

st.title("💉 Controle de Vacinas")

animal = st.text_input("Nome do Animal")

vacina = st.selectbox(
    "Vacina",
    [
        "V8",
        "V10",
        "Antirrábica",
        "Giárdia",
        "Leucemia Felina",
        "Outra"
    ]
)

data_aplicacao = st.date_input(
    "Data da Aplicação"
)

proximo_reforco = st.date_input(
    "Próximo Reforço"
)

veterinario = st.text_input(
    "Veterinário Responsável"
)

observacoes = st.text_area(
    "Observações"
)

if st.button("Salvar Vacina"):
    st.success("Vacina registrada com sucesso!")