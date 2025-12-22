import streamlit as st
import time
import os

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="Dashboard - LMS Elektronika",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 1. KONTROL LOGIN ---
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("❌ Anda harus login untuk mengakses halaman ini.")
    time.sleep(1)
    st.switch_page("00_Login.py") 

username = st.session_state.get("username", "Pengguna").capitalize()

# --- FUNGSI NAVIGASI & LOGOUT ---
def logout():
    st.session_state["logged_in"] = False
    st.success("Anda berhasil keluar.")
    time.sleep(1)
    st.switch_page("00_Login.py")

# --- 2. HEADER NAVIGASI ---
col_logo, col_space, col_user = st.columns([1, 4, 1.5])

with col_logo:
    # PERBAIKAN: Menggunakan File Lokal
    # Pastikan file logo_unp.png ada di folder utama 'projek_pbk'
    logo_path = "logo_unp.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=70)
    else:
        # Jika file lokal tidak ditemukan, tampilkan teks sebagai cadangan
        st.write("Logo UNP")

with col_user:
    st.write(f"👤 **{username}**")
    if st.button("Keluar", type="secondary"):
        logout()

st.markdown("---")

# --- 3. BANNER SELAMAT DATANG ---
# Desain ini mengikuti konsep dashboard yang Anda buat sebelumnya
st.markdown(f"""
<div style="background-color:#01579b; padding: 30px; border-radius: 15px; color: white; margin-bottom: 25px;">
    <h1 style="color: white; margin-top:0px;">Selamat Datang, {username}!</h1>
    <p style="font-size: 18px;">Mari jelajahi materi Elektronika Dasar dan uji kemampuanmu hari ini.</p>
</div>
""", unsafe_allow_html=True)

# --- 4. STATISTIK & MODUL ---
col_stats, col_main = st.columns([1, 2.5])

with col_stats:
    st.subheader("📊 Progres Anda")
    st.metric(label="Total Modul", value="3")
    
    # Menampilkan skor kuis jika sudah pernah dikerjakan
    if "quiz_score" in st.session_state:
        st.metric(label="Skor Kuis Terakhir", value=f"{st.session_state['quiz_score']}%")
    else:
        st.metric(label="Skor Kuis", value="Belum Ada")
    
    st.markdown("---")
    st.info("🤖 **Asisten AI** siap membantumu di halaman Chatbot.")
    if st.button("Tanya Chatbot", use_container_width=True):
        st.switch_page("pages/02_Chatbot.py")

with col_main:
    st.subheader("📚 Modul Pembelajaran")
    
    # Fungsi pembantu untuk menggambar kartu modul secara rapi
    def draw_card(title, desc, page_path):
        with st.container():
            st.markdown(f"### {title}")
            st.write(desc)
            # PERBAIKAN: Pastikan argumen tombol ditutup dengan benar untuk menghindari SyntaxError
            if st.button(f"Buka {title}", key=f"btn_{title.replace(' ', '_')}"):
                st.switch_page(page_path)
            st.markdown("---")

    # Integrasi modul sesuai tahapan proyek akhir Anda
    draw_card("Hukum Ohm", "Pelajari hubungan V, I, dan R secara mendalam.", "pages/03_Materi.py")
    draw_card("Komponen Aktif", "Mengenal fungsi Transistor dan Dioda.", "pages/03_Materi.py")
    draw_card("Kuis Evaluasi", "Uji pemahamanmu sekarang untuk evaluasi mandiri.", "pages/04_Kuis.py")
