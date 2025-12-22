import streamlit as st

# 1. Konfigurasi Halaman Dasar
st.title("🏠 Dashboard Pembelajaran")
st.write(f"Selamat Datang kembali, **{st.session_state.get('username', 'Mahasiswa')}**!")
st.markdown("---")

# 2. Statistik Pembelajaran (Berdasarkan tampilan Anda)
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.subheader("Total Modul")
    st.title("3") # Menyesuaikan dengan data di dashboard Anda

with col_info2:
    st.subheader("Skor Kuis")
    # Menampilkan skor kuis jika ada, jika tidak tampilkan default
    skor = st.session_state.get('quiz_score', 'Belum Ada')
    st.title(skor)

st.markdown("---")

# 3. Kotak Promosi Asisten AI
st.info("🤖 **Asisten AI** siap membantumu di halaman Chatbot jika kamu menemui kesulitan memahami materi.")

# 4. Tombol Navigasi Cepat (SOLUSI ERROR JALUR FILE)
# Perbaikan: Mengarahkan ke folder 'modules/' bukan 'pages/'
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    if st.button("📚 Buka Materi", use_container_width=True):
        st.switch_page("modules/03_Materi.py") # Jalur diperbaiki

with col_btn2:
    if st.button("📝 Mulai Kuis", use_container_width=True):
        st.switch_page("modules/04_Kuis.py") # Jalur diperbaiki

with col_btn3:
    # Tombol yang sebelumnya error di gambar Anda
    if st.button("💬 Tanya Chatbot", use_container_width=True):
        st.switch_page("modules/02_Chatbot.py") # Jalur diperbaiki

# 5. Informasi Tambahan (Opsional)
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2024 LMS Elektronika Dasar - Universitas Negeri Padang")
