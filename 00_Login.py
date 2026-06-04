import streamlit as st
import time
from database import login_user, add_user, create_db

create_db()
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

# Centering logo untuk mobile - Logo diupdate ke SMK Bisa Hebat
def show_logo():
    # URL logo SMK Bisa Hebat
    logo_url = "https://smkbisa.kemdikbud.go.id/wp-content/uploads/2021/04/Logo-SMK-Bisa-Hebat.png"
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin-bottom: 10px;">
            <img src="{logo_url}" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )

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
pg_absensi = st.Page("modules/05_Absensi.py", title="Absensi", icon="📅") # Ditambahkan
pg_out = st.Page(logout, title="Logout", icon="🚪")

if not st.session_state["logged_in"]:
    pg = st.navigation([pg_login], position="hidden")
else:
    pg = st.navigation({"Utama": [pg_dash, pg_mat, pg_quiz, pg_absensi], "Fitur": [pg_chat], "Sistem": [pg_out]})
pg.run()
