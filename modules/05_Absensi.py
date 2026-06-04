import streamlit as st
import datetime

st.title("📅 Form Absensi Siswa")
st.write("Silakan pilih status kehadiran untuk setiap siswa pada simulasi mengajar hari ini.")

# Daftar siswa
daftar_siswa = [
    "Ahmad Alfitra",
    "Fitri Nur Nazmi",
    "Muhammad Ikhsan",
    "Aulia Septri Anisa"
]

# Simpan status kehadiran dalam dictionary di session_state
if "absensi_data" not in st.session_state:
    st.session_state["absensi_data"] = {siswa: "Hadir" for siswa in daftar_siswa}

with st.form("absensi_form"):
    for siswa in daftar_siswa:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write(f"**{siswa}**")
        with col2:
            # Pilihan status secara horizontal
            st.session_state["absensi_data"][siswa] = st.radio(
                f"Status {siswa}", 
                ["Hadir", "Izin", "Sakit"], 
                horizontal=True, 
                label_visibility="collapsed",
                key=f"radio_{siswa}"
            )
    
    if st.form_submit_button("Kirim Rekap Absensi"):
        st.success("Absensi berhasil direkap!")
        st.write(f"**Waktu:** {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        st.table(st.session_state["absensi_data"]) # Menampilkan hasil rekap dalam bentuk tabel
        st.balloons()

if st.button("⬅️ Kembali ke Dashboard"):
    st.switch_page("modules/01_Dashboard.py")
