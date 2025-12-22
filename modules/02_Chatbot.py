import streamlit as st
import google.generativeai as genai

# 1. Mengambil API Key dari "Brankas" Streamlit Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("API Key belum diset di Streamlit Cloud Secrets!")
    st.stop()

# 2. Pengaturan Model & Persona Edukatif
instruction = """
Anda adalah asisten cerdas untuk mata kuliah 'Pengajaran Berbantuan Komputer' di UNP. 
Dosen pengampunya adalah Dr. Yasdinul Huda, S.Pd., MT. 
Jawablah pertanyaan mahasiswa seputar Elektronika Dasar secara mendalam dan edukatif.
"""
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instruction)

st.title("🤖 Asisten AI Elektronika (Secure Mode)")
st.caption("Status: Terhubung via Streamlit Secrets 🔒")
st.markdown("---")

# 3. Riwayat Percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Input & Respon Dinamis
if prompt := st.chat_input("Apa yang ingin Anda tanyakan hari ini?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Berpikir..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
