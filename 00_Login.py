import streamlit as st
import time
from database import login_user, add_user, create_db

# Inisialisasi database dan session state untuk navigasi
create_db()
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

st.set_page_config(page_title="LMS Elektronika Dasar", layout="centered")

def show_login():
    st.title("LMS Elektronika Dasar")
    st.subheader("Universitas Negeri Padang")
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
                st.success(f"Selamat datang kembali, {username.capitalize()}!")
                time.sleep(1)
                st.switch_page("pages/01_Dashboard.py")
            else:
                st.error("Username atau Password salah.")

    # Tombol navigasi ke Register (di luar form)
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("Belum punya akun?")
        if st.button("Daftar di sini", use_container_width=True):
            st.session_state["auth_mode"] = "register"
            st.rerun()

def show_register():
    st.title("LMS Elektronika Dasar")
    st.subheader("Pendaftaran Akun Baru")
    st.markdown("---")
    
    with st.form("reg_form"):
        new_user = st.text_input("Buat Username").lower()
        new_pw = st.text_input("Buat Password", type="password")
        confirm_pw = st.text_input("Konfirmasi Password", type="password")
        submit_reg = st.form_submit_button("Daftar Akun", use_container_width=True)

        if submit_reg:
            if new_pw != confirm_pw:
                st.error("Konfirmasi password tidak cocok.")
            elif len(new_pw) < 6:
                st.warning("Password minimal 6 karakter untuk keamanan.")
            else:
                if add_user(new_user, new_pw):
                    st.success("Akun berhasil dibuat!")
                    time.sleep(1.5)
                    st.session_state["auth_mode"] = "login"
                    st.rerun()
                else:
                    st.warning("Username sudah digunakan. Pilih yang lain.")

    # Tombol kembali ke Login
    st.write("")
    if st.button("Sudah punya akun? Masuk di sini"):
        st.session_state["auth_mode"] = "login"
        st.rerun()

# Logika penentuan halaman yang tampil
if st.session_state.get("logged_in"):
    st.switch_page("pages/01_Dashboard.py")
else:
    if st.session_state["auth_mode"] == "login":
        show_login()
    else:
        show_register()