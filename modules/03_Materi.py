import streamlit as st
import os

st.title("📚 Materi Pembelajaran")
st.write("Silakan pelajari materi berikut ini:")

# Pastikan nama file ini SAMA PERSIS dengan file di folder Anda
pdf_file = "materi_pembelajaran.pdf" 

# Mengecek apakah file ada di folder
if os.path.exists(pdf_file):
    with open(pdf_file, "rb") as f:
        # Membaca file sebagai data biner
        st.pdf(f.read())
else:
    st.error(f"File '{pdf_file}' tidak ditemukan di folder!")
    st.write("Pastikan file tersebut berada di direktori yang sama dengan skrip ini.")
