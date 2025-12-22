import streamlit as st
from groq import Groq

# 1. Koneksi API Groq via Secrets
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("API Key Groq tidak ditemukan di Secrets!")
    st.stop()

# 2. Header Chatbot Profesional (Nama Diperbarui)
st.title("🤖 Asisten AI Elektronika")
st.caption("MK: Pengajaran Berbantuan Komputer | Dosen: Dr. Yasdinul Huda, S.Pd., MT")
st.markdown("---")

# 3. Pengelolaan Riwayat Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Input & Respon Instan
if prompt := st.chat_input("Tanyakan rumus atau komponen elektronika..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Berpikir..."):
            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "Anda adalah asisten ahli Elektronika Dasar UNP. Jawablah dengan edukatif dan profesional."},
                        {"role": "user", "content": prompt}
                    ]
                )
                
                response = completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                st.error(f"Gagal memproses jawaban: {e}")
