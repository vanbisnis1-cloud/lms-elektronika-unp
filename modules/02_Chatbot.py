import streamlit as st
import google.generativeai as genai

# Konfigurasi halaman
st.set_page_config(page_title="Asisten AI Elektronika", layout="wide")

# Masukkan API Key Anda di sini
API_KEY = "PASTE_KODE_API_KEY_ANDA_DI_SINI"
genai.configure(api_key=API_KEY)

# Pengaturan Model (Persona AI)
model = genai.GenerativeModel('gemini-pro')

st.title("🤖 Asisten Pintar Elektronika")
st.write("Tanyakan apa saja seputar komponen, rumus, atau teori elektronika dasar.")
st.markdown("---")

# Inisialisasi riwayat pesan (Chat History) agar tidak statis
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya asisten AI Elektronika Dasar UNP. Ada yang bisa saya bantu?"}
    ]

# Menampilkan pesan dari riwayat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input Chat
if prompt := st.chat_input("Contoh: Apa fungsi kapasitor dalam rangkaian DC?"):
    # Tambahkan pesan user ke riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Proses jawaban AI
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown(" sedang berpikir...")
        
        try:
            # Memberikan instruksi spesifik agar AI fokus pada Elektronika (System Prompt)
            full_prompt = f"Anda adalah asisten dosen ahli Elektronika Dasar di UNP. Jawablah pertanyaan mahasiswa berikut dengan bahasa yang mudah dimengerti dan edukatif: {prompt}"
            
            response = model.generate_content(full_prompt)
            full_response = response.text
            message_placeholder.markdown(full_response)
            
            # Tambahkan jawaban AI ke riwayat
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Gagal terhubung ke otak AI: {e}")
