import streamlit as st
import time
from database import login_user, add_user, create_db

# Inisialisasi database
create_db()

st.set_page_config(page_title="LMS Elektronika Dasar", layout="centered")

def main():
    st.title("LMS Elektronika Dasar")
    st.subheader("Universitas Negeri Padang")
    
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.header("Silakan Masuk")
        with st.form("login_form"):
            username = st.text_input("Username").lower()
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Masuk")

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

    elif choice == "Register":
        st.header("Buat Akun Baru")
        with st.form("reg_form"):
            new_user = st.text_input("Username Baru").lower()
            new_pw = st.text_input("Password Baru", type="password")
            submit_reg = st.form_submit_button("Daftar")

            if submit_reg:
                if add_user(new_user, new_pw):
                    st.success("Akun berhasil dibuat! Silakan pindah ke menu Login.")
                else:
                    st.warning("Username sudah digunakan. Silakan pilih yang lain.")

if __name__ == '__main__':
    main()