import streamlit as st
import time
from database import login_user, add_user, create_db

# 1. Inisialisasi Database & Session State
create_db()
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

def show_logo():
    logo_url = "https://raw.githubusercontent.com/vanbisnis1-cloud/lms-elektronika-unp/main/logo_unp.png"
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin-bottom: 10px;">
            <img src="{logo_url}" width="120">
        </div>
        """,
        unsafe_allow_html=True
    )

def show_developer_info():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    with st.expander("👤 Tim Pengembang Aplikasi (Developer Team)"):
        st.markdown("### **Proyek Akhir Mata Kuliah Pengajaran Berbantuan Komputer**")
        st.markdown("#### **Dosen Pengampu: Dr. Yasdinul Huda, S.Pd., MT**")
        st.markdown("---")
        # Detail Anggota (Gunakan kode kolom yang sudah Anda miliki di sini)
        st.write("Ivan Bachri Arrizki (23065028)")
        st.write("Lidia Puspita (23065009)")
        st.write("Fitri Nur Nazmi (23065026)")

def login_page():
    if st.session_state["auth_mode"] == "login":
        show_logo()
        st.markdown("<h1 style='text-align: center; color: #01579b; margin-top: -20px;'>LMS Elektronika Dasar</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Universitas Negeri Padang</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.header("Silakan Masuk")
        with st.form("login_form"):
            username = st.text_input("Username").lower()
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Masuk", use_container_width=True)
            if submit:
                if login_user(username, password):
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.rerun()
                else:
                    st.error("Username atau Password salah.")
        
        st.write("Belum punya akun?")
        if st.button("Daftar Akun Baru", use_container_width=True):
            st.session_state["auth_mode"] = "register"
            st.rerun()
        
        show_developer_info()
    else:
        register_page()

# FUNGSI PENDAFTARAN DIPERBARUI
def register_page():
    show_logo()
    st.title("Pendaftaran Akun Baru") # Nama lebih umum
    with st.form("reg_form"):
        u = st.text_input("Username").lower()
        p = st.text_input("Password", type="password")
        if st.form_submit_button("Daftar Akun", use_container_width=True):
            if add_user(u, p):
                st.success("Berhasil! Silakan masuk kembali.")
                st.session_state["auth_mode"] = "login"
                time.sleep(1)
                st.rerun()
            else:
                st.warning("Username sudah terdaftar.")
    if st.button("Kembali ke Login", use_container_width=True):
        st.session_state["auth_mode"] = "login"
        st.rerun()

def logout():
    st.session_state["logged_in"] = False
    st.session_state["auth_mode"] = "login"
    st.rerun()

# --- NAVIGASI ---
l_s = st.Page(login_page, title="Login", icon="🔒")
d_s = st.Page("modules/01_Dashboard.py", title="Dashboard", icon="🏠")
c_s = st.Page("modules/02_Chatbot.py", title="Asisten AI", icon="🤖")
m_s = st.Page("modules/03_Materi.py", title="Materi Pembelajaran", icon="📚")
k_s = st.Page("modules/04_Kuis.py", title="Kuis Evaluasi", icon="📝")
o_s = st.Page(logout, title="Logout", icon="🚪")

if not st.session_state["logged_in"]:
    pg = st.navigation([l_s], position="hidden")
else:
    pg = st.navigation({"Utama": [d_s, m_s, k_s], "Fitur": [c_s], "Sistem": [o_s]})

pg.run()
