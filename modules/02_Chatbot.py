import streamlit as st
import google.generativeai as genai

# 1. Ambil API Key dari Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("Kunci API (GEMINI_API_KEY) tidak ditemukan di Streamlit Secrets!")
    st.stop()

# 2. Pengaturan Model dengan Nama yang Lebih Kompatibel
# Kita gunakan 'gemini-1.5-flash' yang merupakan standar terbaru
instruction = "Anda adalah asisten dosen Elektronika di UNP untuk MK Pengajaran Berbantuan Komputer."

try:
    # Gunakan konfigurasi model yang lebih sederhana untuk menghindari error NotFound
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=instruction
    )
except Exception as e:
    st.error(f"Gagal menginisialisasi model: {e}")
    st.stop()

st.title("🤖 Asisten AI Elektronika")
st.caption("Status: Secure Mode Aktif 🔒")
st.markdown("---")

# 3. Riwayat Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Input Chat & Respon
if prompt := st.chat_input("Tanya apa saja seputar elektronika..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Sedang berpikir..."):
            try:
                # Menghasilkan konten
                response = model.generate_content(prompt)
                
                # Cek jika respon valid
                if response and response.text:
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                else:
                    st.warning("AI tidak memberikan respon. Coba pertanyaan lain.")
            except Exception as e:
                # Menampilkan pesan error yang lebih mudah dipahami mahasiswa
                st.error(f"Maaf, terjadi gangguan pada otak AI: {e}")
