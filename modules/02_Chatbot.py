import streamlit as st
import google.generativeai as genai

# 1. Koneksi API via Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("Secrets 'GEMINI_API_KEY' belum diatur di Streamlit Cloud!")
    st.stop()

# 2. Inisialisasi Model Terbaru (Versi 2.0)
# Model ini jauh lebih pintar dan responsif untuk membantu belajar elektronika
@st.cache_resource
def load_ai_model():
    # Menggunakan salah satu model yang terdeteksi aktif di akun Anda
    return genai.GenerativeModel('gemini-2.0-flash')

model = load_ai_model()

# 3. Header Chatbot Profesional
st.title("🤖 Asisten AI Elektronika v2.0")
st.caption("Didukung oleh Gemini 2.0 Flash | MK: Pengajaran Berbantuan Komputer")
st.markdown("---")

# 4. Wadah Pesan (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya asisten AI versi terbaru. Ada yang bisa saya bantu seputar Elektronika Dasar?"}
    ]

# Tampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Logika Interaksi Dinamis
if prompt := st.chat_input("Tanyakan sesuatu (misal: Bagaimana cara kerja Transistor?)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Sedang memproses jawaban cerdas..."):
            try:
                # Instruksi khusus agar tetap fokus pada materi UNP
                full_prompt = f"Anda adalah asisten cerdas untuk mahasiswa UNP. Jawablah dengan edukatif: {prompt}"
                
                response = model.generate_content(full_prompt)
                
                if response.text:
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                else:
                    st.warning("Maaf, AI sedang tidak memberikan respon. Coba ulangi pertanyaan.")
            except Exception as e:
                st.error(f"Gagal memproses jawaban: {e}")
