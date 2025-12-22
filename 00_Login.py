import streamlit as st
import time
from database import login_user, add_user, create_db

# 1. Inisialisasi Database & Session State
create_db()
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

# --- FUNGSI TAMPILAN LOGO (Stabil di Desktop & Mobile) ---
def show_logo():
    # Menggunakan HTML CSS agar logo tetap di tengah sempurna di HP
    logo_url = "https://raw.githubusercontent.com/vanbisnis1-cloud/lms-elektronika-unp/main/logo_unp.png"
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin-bottom: 10px;">
            <img src="{logo_url}" width="120">
        </div>
        """,
        unsafe_allow_html=True
    )

# --- FUNGSI TAMPILAN DEVELOPER (Data Kelompok) ---
def show_developer_info():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    with st.expander("👤 Tim Pengembang Aplikasi (Developer Team)"):
        st.write("Proyek Akhir Mata Kuliah Pemrograman Dasar")
        st.markdown("---")

        # Anggota 1: Ivan
        c1_f, c1_t = st.columns([1, 2.5])
        with c1_f:
            st.image("foto_ivan.png", use_container_width=True) # Foto 1080x1080
        with c1_t:
            st.markdown("#### **Ivan Bachri Arrizki**")
            st.write("**NIM:** 23065028")
        
        st.divider()

        # Anggota 2: Lidia
        c2_f, c2_t = st.columns([1, 2.5])
        with c2_f:
            st.image("foto_lidia.png", use_container_width=True)
        with c2_t:
            st.markdown("#### **Lidia Puspita**")
            st.write("**NIM:** 23065009")

        st.divider()

        # Anggota 3: Fitri
        c3_f, c3_t = st.columns([1, 2.5])
        with c3_f:
            st.image("foto_fitri.png", use_container_width=True)
        with c3_t:
            st.markdown("#### **Fitri Nur Nazmi**")
            st.write("**NIM:** 23065026")

        st.markdown("---")
        st.caption("© 2024 Pendidikan Teknik Elektronika - UNP")

# --- FUNGSI HALAMAN UTAMA ---

def login_page():
    if st.session_state["auth_mode"] == "login":
        show_logo()
        st.markdown("<h1 style='text-align: center; color: #01579b; margin-top: -20px;'>LMS Elektronika Dasar</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-weight: bold;'>Universitas Negeri Padang</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.header("Silakan Masuk")
        with st.form("login_form"):
            username = st.text_input("Username").lower()
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Masuk Sekarang", use_container_width=True)

            if submit:
                if login_user(username, password):
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.success(f"Selamat datang, {username.capitalize()}!")
                    time.sleep(0.5)
                    st.rerun() 
                else:
                    st.error("Username atau Password salah.")
        
        st.markdown("<p style='text-align: center;'>Belum punya akun?</p>", unsafe_allow_html=True)
        if st.button("Daftar di sini", use_container_width=True):
            st.session_state["auth_mode"] = "register"
            st.rerun()

        # Menampilkan info tim pengembang di bawah halaman login
        show_developer_info()
    else:
        register_page()

def register_page():
    show_logo()
    st.title("Pendaftaran Akun Baru")
    with st.form("reg_form"):
        new_user = st.text_input("Buat Username").lower()
        new_pw = st.text_input("Buat Password", type="password")
        if st.form_submit_button("Daftar Akun", use_container_width=True):
            if add_user(new_user, new_pw):
                st.success("Akun berhasil dibuat! Silakan masuk.")
                st.session_state["auth_mode"] = "login"
                time.sleep(1)
                st.rerun()
            else:
                st.warning("Username sudah digunakan.")
    if st.button("Kembali ke Login", use_container_width=True):
        st.session_state["auth_mode"] = "login"
        st.rerun()

def logout():
    st.session_state["logged_in"] = False
    st.session_state["auth_mode"] = "login"
    st.rerun()

# --- LOGIKA NAVIGASI (MULTI-PAGE) ---

# Definisi halaman dari folder modules
login_screen = st.Page(login_page, title="Masuk", icon="🔒")
dashboard = st.Page("modules/01_Dashboard.py", title="Dashboard", icon="🏠")
chatbot = st.Page("modules/02_Chatbot.py", title="Asisten AI", icon="🤖")
materi = st.Page("modules/03_Materi.py", title="Materi Pembelajaran", icon="📚")
kuis = st.Page("modules/04_Kuis.py", title="Kuis Evaluasi", icon="📝")
logout_screen = st.Page(logout, title="Keluar", icon="🚪")

# Kontrol Sidebar: Sembunyikan jika belum login
if not st.session_state["logged_in"]:
    pg = st.navigation([login_screen], position="hidden")
else:
    pg = st.navigation({
        "Menu Utama": [dashboard, materi, kuis],
        "Bantuan AI": [chatbot],
        "Sistem": [logout_screen]
    })

pg.run()
