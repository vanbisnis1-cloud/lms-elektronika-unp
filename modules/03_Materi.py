import streamlit as st

st.title("📚 Materi Pembelajaran")
st.write("Silakan pelajari materi berikut ini:")

# Path ke file PDF lokal
pdf_file = "materi_pembelajaran.pdf" # Sesuaikan dengan nama file Anda

try:
    with open(pdf_file, "rb") as f:
        pdf_data = f.read()
    st.pdf(pdf_data)
except FileNotFoundError:
    st.error(f"File '{pdf_file}' tidak ditemukan. Pastikan nama file sudah benar dan berada di folder yang sama.")
