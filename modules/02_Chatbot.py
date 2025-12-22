import streamlit as st
import google.generativeai as genai

# 1. Ambil API Key dari Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("Kunci API tidak ditemukan di Secrets!")
    st.stop()

# 2. Inisialisasi Model
# Gunakan nama model standar 'gemini-1.5-flash'
instruction = "Anda adalah asisten cerdas MK Pengajaran Berbantuan Komputer di UNP."

@st.cache_resource
def load_model():
    return genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=instruction
    )

model = load_model()

st.title("🤖 Asisten AI Elektronika")
st.caption("Mode: Gemini 1.5 Flash Aktif 🚀")
st.markdown("---")

# 3. Riwayat Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Input Chat & Respon
if prompt := st.chat_input("Apa yang ingin Anda tanyakan?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Gunakan response streaming agar terasa lebih dinamis
            response = model.generate_content(prompt)
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.warning("Respon kosong, coba pertanyaan lain.")
        except Exception as e:
            # Jika 'gemini-1.5-flash' masih 404, coba fallback ke 'gemini-pro'
            st.error(f"Error: {e}")
            st.info("Sistem sedang mencoba memulihkan koneksi...")
