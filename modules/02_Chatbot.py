import streamlit as st
import google.generativeai as genai

# Setup API
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# Gunakan model yang terdeteksi aktif di akun Anda
model = genai.GenerativeModel('gemini-2.0-flash')

st.title("🤖 Asisten AI Elektronika v2.0")
st.caption("Status: Monitoring Kuota 📊")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tanya sesuatu..."):
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
                # Menangani Error Quota (429) agar tetap terlihat profesional
                if "429" in str(e):
                    st.warning("⚠️ **Server Sibuk (Limit Kuota Gratis)**")
                    st.info("Mohon tunggu sekitar 60 detik sebelum mengirim pertanyaan berikutnya. Ini adalah batasan versi gratis dari Google API.")
                else:
                    st.error(f"Terjadi gangguan teknis: {e}")
