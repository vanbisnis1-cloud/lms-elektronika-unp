import streamlit as st
import google.generativeai as genai

# 1. Koneksi API
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("Secrets 'GEMINI_API_KEY' belum diatur!")
    st.stop()

# 2. Inisialisasi Model Tanpa Instruksi Rumit (Lebih Stabil)
@st.cache_resource
def load_simple_model():
    # Mencoba model paling standar agar tidak 404
    return genai.GenerativeModel('gemini-1.5-flash')

model = load_simple_model()

st.title("🤖 Asisten AI Elektronika")
st.caption("Mode: Koneksi Langsung (Minimalist)")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Coba sapa AI: 'Halo'"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Tambahkan instruksi langsung di dalam prompt agar tetap pintar
            full_prompt = f"Anda adalah asisten dosen UNP. Jawablah: {prompt}"
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # Menampilkan detail error asli dari Google untuk diagnosa
            st.error(f"Koneksi Gagal: {e}")
