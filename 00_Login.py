import streamlit as st
import time
from database import login_user, add_user, create_db

# 1. Inisialisasi Database & Session State
create_db()
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

# --- FUNGSI TAMPILAN LOGO ---
def show_logo():
    # Menggunakan kolom untuk memposisikan logo di tengah
    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        # Langsung memanggil file dari root repositori GitHub Anda
        st.image("logo_unp.png", width=120)

# --- FUNGSI HALAMAN LOGIN ---
def login_page():
    if st.session_state["auth_mode"] == "login":
        show_logo() # Memanggil logo di bagian paling atas
        
        st.markdown("<h1 style='text-align: center; color: #01579b;'>LMS Elektronika Dasar</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-weight: bold;'>Universitas Negeri Padang</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.header("Silakan Masuk")
        with st.form("login_form"):
            username = st.text_input("Username").lower()
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Masuk", use_container_width=True)

            if submit:
                result = login_user(username, password)
                if result:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.success(f"Selamat datang, {username.capitalize()}!")
                    time.sleep(0.5)
                    st.rerun() 
                else:
                    st.error("Username atau Password salah.")
        
        # Link navigasi ke halaman pendaftaran
        st.markdown("<p style='text-align: center;'>Belum punya akun?</p>", unsafe_allow_html=True)
        if st.button("Daftar di sini", use_container_width=True):
            st.session_state["auth_mode"] = "register"
            st.rerun()
    else:
        register_page()

# --- FUNGSI HALAMAN REGISTER ---
def register_page():
    show_logo()
    st.title("Pendaftaran Akun Baru")
    st.write("Silakan isi data di bawah untuk membuat akun siswa.")
    
    with st.form("reg_form"):
        new_user = st.text_input("Buat Username").lower()
        new_pw = st.text_input("Buat Password", type="password")
        confirm_pw = st.text_input("Konfirmasi Password", type="password")
        submit_reg = st.form_submit_button("Daftar Akun Sekarang", use_container_width=True)

        if submit_reg:
            if new_pw != confirm_pw:
                st.error("Konfirmasi password tidak cocok.")
            elif len(new_pw) < 6:
                st.warning("Password minimal 6 karakter.")
            else:
                if add_user(new_user, new_pw):
                    st.success("Akun berhasil dibuat! Silakan masuk.")
                    st.session_state["auth_mode"] = "login"
                    time.sleep(1.5)
                    st.rerun()
                else:
                    st.warning("Username sudah digunakan. Silakan pilih yang lain.")
    
    if st.button("Kembali ke Halaman Login", use_container_width=True):
        st.session_state["auth_mode"] = "login"
        st.rerun()

# --- FUNGSI LOGOUT ---
def logout():
    st.session_state["logged_in"] = False
    st.session_state["auth_mode"] = "login"
    st.rerun()

# --- SISTEM NAVIGASI MULTI-HALAMAN ---

# Pastikan path mengarah ke folder 'modules' yang sudah Anda buat
login_screen = st.Page(login_page, title="Masuk Ke Sistem", icon="🔒")
dashboard = st.Page("modules/01_Dashboard.py", title="Dashboard", icon="🏠")
chatbot = st.Page("modules/02_Chatbot.py", title="Asisten AI", icon="🤖")
materi = st.Page("modules/03_Materi.py", title="Materi Pembelajaran", icon="📚")
kuis = st.Page("modules/04_Kuis.py", title="Kuis Evaluasi", icon="📝")
logout_screen = st.Page(logout, title="Keluar dari Sistem", icon="🚪")

# Pengaturan visibilitas menu sidebar
if not st.session_state["logged_in"]:
    # Jika belum login, sidebar disembunyikan (Akses Terkunci)
    pg = st.navigation([login_screen], position="hidden")
else:
    # Jika sudah login, tampilkan menu berdasarkan kategori
    pg = st.navigation({
        "Menu Utama": [dashboard, materi, kuis],
        "Fitur Cerdas": [chatbot],
        "Akun": [logout_screen]
    })

pg.run()
