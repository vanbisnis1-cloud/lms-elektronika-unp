import streamlit as st
import datetime

# Judul Halaman
st.title("📅 Form Absensi Siswa")
st.write("Silakan pilih nama Anda dan status kehadiran untuk simulasi mengajar hari ini.")

# Daftar siswa sesuai permintaan Anda
daftar_siswa = [
    "Ahmad Alfitra",
    "Fitri Nur Nazmi",
    "Muhammad Ikhsan",
    "Aulia Septri Anisa"
]

# Form Absensi
with st.form("absensi_form"):
    nama_siswa = st.selectbox("Pilih Nama Anda", daftar_siswa)
    status_kehadiran = st.radio("Status Kehadiran", ["Hadir", "Izin", "Sakit"])
    catatan = st.text_area("Catatan Tambahan (Opsional)")
    
    # Tombol submit
    submit = st.form_submit_button("Kirim Absensi")

    if submit:
        # Menampilkan konfirmasi (Untuk saat ini data tampil di layar)
        st.success(f"Absensi berhasil dikirim!")
        st.write(f"**Nama:** {nama_siswa}")
        st.write(f"**Status:** {status_kehadiran}")
        st.write(f"**Waktu:** {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        
        # Anda bisa menambahkan logika penyimpanan ke database atau file CSV di sini
        st.balloons()

# Tombol navigasi kembali
if st.button("⬅️ Kembali ke Dashboard"):
    st.switch_page("modules/01_Dashboard.py")
