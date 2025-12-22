import streamlit as st

# 1. Konfigurasi Halaman
st.title("📚 Materi Pembelajaran Elektronika Dasar")
st.write("Silakan pelajari materi di bawah ini untuk persiapan kuis.")
st.markdown("---")

# 2. Daftar Materi menggunakan Tabs agar Rapi
tab1, tab2, tab3 = st.tabs(["Resistor", "Kapasitor", "Dioda"])

with tab1:
    st.header("1. Resistor (Hambatan)")
    st.write("""
    Resistor adalah komponen elektronik pasif yang berfungsi untuk menghambat dan mengatur arus listrik dalam suatu rangkaian.
    
    **Fungsi Utama:**
    * Membatasi arus listrik.
    * Pembagi tegangan.
    * Penurun tegangan.
    """)
    st.info("Rumus Hukum Ohm: **V = I x R**")

with tab2:
    st.header("2. Kapasitor (Kondensator)")
    st.write("""
    Kapasitor adalah komponen yang mampu menyimpan energi dalam bentuk medan listrik.
    
    **Fungsi Utama:**
    * Menyimpan muatan listrik.
    * Sebagai penyaring (filter) dalam rangkaian power supply.
    * Memblokir arus DC dan melewatkan arus AC.
    """)
    st.warning("Satuan Kapasitansi adalah **Farad (F)**.")

with tab3:
    st.header("3. Dioda")
    st.write("""
    Dioda adalah komponen semikonduktor yang hanya mengalirkan arus listrik ke satu arah saja (penyearah).
    
    **Komponen Dioda:**
    * **Anoda**: Kutub Positif.
    * **Katoda**: Kutub Negatif.
    """)
    st.success("Dioda sering digunakan sebagai penyearah arus (Rectifier).")

# --- TOMBOL KEMBALI DIHAPUS SESUAI PERMINTAAN ---
# (Navigasi kini sepenuhnya menggunakan sidebar agar lebih stabil)

st.markdown("---")
st.caption("Gunakan bilah sisi (sidebar) di sebelah kiri untuk berpindah ke halaman lain.")
