import streamlit as st

st.title("🪱 Controle de Vermífugos")

animal = st.text_input("Nome do Animal")

produto = st.text_input(
    "Produto Utilizado"
)

data_aplicacao = st.date_input(
    "Data da Aplicação"
)

proxima_dose = st.date_input(
    "Próxima Dose"
)

dose = st.text_input(
    "Dose"
)

observacoes = st.text_area(
    "Observações"
)

if st.button("Salvar Vermífugo"):
    st.success("Vermífugo registrado!")