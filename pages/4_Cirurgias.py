import streamlit as st

st.title("🏥 Cirurgias")

animal = st.text_input("Nome do Animal")

procedimento = st.selectbox(
    "Procedimento",
    [
        "Castração",
        "Enucleação",
        "Mastectomia",
        "Ortopedia",
        "Hérnia",
        "Outro"
    ]
)

data_cirurgia = st.date_input(
    "Data da Cirurgia"
)

veterinario = st.text_input(
    "Veterinário Responsável"
)

resultado = st.text_area(
    "Descrição da Cirurgia"
)

pos_operatorio = st.text_area(
    "Pós-operatório"
)

if st.button("Salvar Cirurgia"):
    st.success("Cirurgia registrada!")