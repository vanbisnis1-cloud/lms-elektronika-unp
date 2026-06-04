import streamlit as st
import time
from database import login_user, add_user, create_db

create_db()
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

# Fungsi Logo Lokal (Pastikan file logo_smk.png ada di folder utama)
def show_logo():
    try:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("logo_smk.png", use_container_width=True)
    except:
        st.warning("File logo_smk.png tidak ditemukan.")

def login_page():
    if st.session_state["auth_mode"] == "login":
        show_logo()
        st.markdown("<h1 style='text-align: center; color: #01579b;'>LMS Elektronika Dasar</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Simulasi Mengajar</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        with st.form("login"):
            u = st.text_input("Username").lower()
            p = st.text_input("Password", type="password")
            if st.form_submit_button("Masuk", use_container_width=True):
                if login_user(u, p):
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = u
                    st.rerun()
                else: st.error("Salah password/username.")
        
        if st.button("Daftar Akun Baru", use_container_width=True):
            st.session_state["auth_mode"] = "register"
            st.rerun()
    else: register_page()

def register_page():
    show_logo()
    st.title("Pendaftaran Akun Baru")
    with st.form("reg"):
        u = st.text_input("Username Baru").lower()
        p = st.text_input("Password Baru", type="password")
        if st.form_submit_button("Daftar", use_container_width=True):
            if add_user(u, p):
                st.success("Berhasil! Silakan login.")
                st.session_state["auth_mode"] = "login"
                time.sleep(1)
                st.rerun()
            else: st.warning("Username sudah ada.")
    if st.button("Kembali"):
        st.session_state["auth_mode"] = "login"
        st.rerun()

def logout():
    st.session_state["logged_in"] = False
    st.rerun()

# Definisi Halaman
pg_login = st.Page(login_page, title="Login", icon="🔒")
pg_dash = st.Page("modules/01_Dashboard.py", title="Dashboard", icon="🏠")
pg_chat = st.Page("modules/02_Chatbot.py", title="Asisten AI", icon="🤖")
pg_mat = st.Page("modules/03_Materi.py", title="Materi", icon="📚")
pg_quiz = st.Page("modules/04_Kuis.py", title="Kuis", icon="📝")
pg_absensi = st.Page("modules/05_Absensi.py", title="Absensi", icon="📅")
pg_out = st.Page(logout, title="Logout", icon="🚪")

if not st.session_state["logged_in"]:
    pg = st.navigation([pg_login], position="hidden")
else:
    pg = st.navigation({"Utama": [pg_dash, pg_mat, pg_quiz, pg_absensi], "Fitur": [pg_chat], "Sistem": [pg_out]})
pg.run()
