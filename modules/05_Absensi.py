import streamlit as st
import datetime

st.title("📅 Form Absensi Siswa")
st.write("Silakan pilih status kehadiran untuk setiap siswa pada simulasi mengajar hari ini.")

# Daftar siswa
daftar_siswa = [
    "Ahmad Alfitra",
    "Fitri Nur Nazmi",
    "Muhammad Ikhsan",
    "Fikhi Khalil Fakhri"
]

# Inisialisasi session state dengan None agar tidak ada yang terpilih otomatis
if "absensi_data" not in st.session_state:
    st.session_state["absensi_data"] = {siswa: None for siswa in daftar_siswa}

with st.form("absensi_form"):
    for siswa in daftar_siswa:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write(f"**{siswa}**")
        with col2:
            # index=None membuat radio button tidak memilih opsi apa pun di awal
            st.session_state["absensi_data"][siswa] = st.radio(
                f"Status {siswa}", 
                ["Hadir", "Izin", "Sakit"], 
                index=None, 
                horizontal=True, 
                label_visibility="collapsed",
                key=f"radio_{siswa}"
            )
    
    if st.form_submit_button("Kirim Rekap Absensi"):
        # Pengecekan sederhana apakah semua sudah diisi
        if None in st.session_state["absensi_data"].values():
            st.warning("Mohon lengkapi status kehadiran untuk semua siswa!")
        else:
            st.success("Absensi berhasil direkap!")
            st.write(f"**Waktu:** {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
            st.table(st.session_state["absensi_data"])
            st.balloons()

if st.button("⬅️ Kembali ke Dashboard"):
    st.switch_page("modules/01_Dashboard.py")
