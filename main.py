import streamlit as st

st.set_page_config(
    page_title="ONG Animais",
    page_icon="🐾",
    layout="wide"
)

st.title("🐾 Sistema de Gestão da ONG")

st.write("Bem-vinda ao sistema da ONG.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Animais Abrigados", 0)

with col2:
    st.metric("Adoções", 0)

with col3:
    st.metric("Vacinas Pendentes", 0)

st.divider()

st.write("Selecione uma opção no menu lateral.")