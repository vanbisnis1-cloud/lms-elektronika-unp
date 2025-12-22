import streamlit as st
import google.generativeai as genai

# 1. Konfigurasi Keamanan API
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("Konfigurasi Secrets 'GEMINI_API_KEY' tidak ditemukan!")
    st.stop()

# 2. Fungsi Inisialisasi Model Pintar (Fallback System)
@st.cache_resource
def get_ai_model():
    # Daftar model dari yang tercanggih ke yang paling stabil
    model_options = ['gemini-1.5-flash', 'gemini-pro']
    
    instruction = "Anda asisten cerdas MK Pengajaran Berbantuan Komputer di UNP."
    
    for m_name in model_options:
        try:
            # Mencoba mengaktifkan model
            test_model = genai.GenerativeModel(model_name=m_name, system_instruction=instruction)
            # Tes singkat untuk memastikan model benar-benar bisa digunakan
            test_model.generate_content("hi") 
            return test_model, m_name
        except Exception:
            continue
    return None, None

model, active_model_name = get_ai_model()

if not model:
    st.error("Maaf, API Key Anda tidak diizinkan mengakses model Gemini saat ini.")
    st.stop()

# 3. Tampilan Header
st.title("🤖 Asisten AI Elektronika")
st.caption(f"Model Aktif: {active_model_name.upper()} | Dosen: Dr. Yasdinul Huda, S.Pd., MT")
st.markdown("---")

# 4. Sistem Riwayat Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Input & Respon Dinamis
if prompt := st.chat_input("Tanyakan sesuatu..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Sedang memproses..."):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Gagal memproses jawaban: {e}")
