import streamlit as st
import time

# --- KONTROL LOGIN ---
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("❌ Anda harus login untuk mengakses halaman ini.")
    time.sleep(1)
    st.switch_page("00_Login.py")

st.set_page_config(page_title="Materi - LMS Elektronika", layout="wide")

# Tombol kembali ke Dashboard di Sidebar
if st.sidebar.button("⬅️ Kembali ke Dashboard"):
    st.switch_page("pages/01_Dashboard.py")

st.title("📚 Modul Pembelajaran Elektronika")
st.write("Silakan pilih tab di bawah ini untuk mempelajari materi secara mendalam.")
st.markdown("---")

# Menggunakan Tab untuk navigasi materi
tab1, tab2, tab3 = st.tabs(["⚡ Hukum Ohm", "🔌 Komponen Aktif", "📑 Rangkaian Dasar"])

with tab1:
    st.header("1. Pengantar Hukum Ohm")
    st.write("""
    Hukum Ohm adalah prinsip dasar elektronika yang menjelaskan hubungan antara **Tegangan (V)**, **Arus (I)**, dan **Hambatan (R)**. 
    Berdasarkan materi video di bawah, kita dapat menggunakan 'Segitiga Hukum Ohm' untuk memudahkan penurunan rumus.
    """)
    
    # Menampilkan Rumus Utama
    st.info("### Rumus Utama Hukum Ohm:")
    st.latex(r"V = I \times R")
    st.write("""
    - **V (Voltage)**: Tegangan, diukur dalam satuan **Volt (V)**.
    - **I (Current)**: Arus listrik, diukur dalam satuan **Ampere (A)**.
    - **R (Resistance)**: Hambatan atau Resistansi, diukur dalam satuan **Ohm (Ω)**.
    """)

    st.markdown("---")
    st.subheader("🎥 Video Penjelasan: Cara Mencari Arus, Tegangan, dan Hambatan")
    
    # UPDATE: Menggunakan video YT yang Anda berikan
    st.video("https://www.youtube.com/watch?v=gfUIa1R39vI")
    
    st.caption("Sumber Video: JAGO LISTRIK - Membahas Segitiga Hukum Ohm dan variabel Daya (P).")

with tab2:
    st.header("2. Komponen Aktif")
    st.write("Berbeda dengan komponen pasif, komponen aktif memerlukan arus listrik eksternal untuk dapat beroperasi.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Transistor")
        st.write("""
        Komponen semikonduktor yang memiliki berbagai fungsi, antara lain:
        - Sebagai penguat sinyal (Amplifier).
        - Sebagai sakelar elektronik (Switching).
        - Sebagai stabilisasi tegangan.
        """)
    with col_b:
        st.subheader("Dioda")
        st.write("""
        Komponen yang berfungsi mengizinkan arus listrik mengalir ke satu arah (bias maju) 
        dan menghambat arus dari arah sebaliknya (bias mundur).
        """)

with tab3:
    st.header("3. Rangkaian Seri & Paralel")
    st.write("Susunan komponen menentukan bagaimana arus dan tegangan terbagi dalam suatu sirkuit.")
    
    st.image("https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc-600.png", 
             caption="Simulasi Rangkaian Listrik", use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Rangkaian Seri**")
        st.write("Komponen disusun berurutan. Arus (I) yang mengalir pada setiap komponen adalah sama.")
    with col2:
        st.markdown("**Rangkaian Paralel**")
        st.write("Komponen disusun sejajar. Tegangan (V) pada setiap cabang rangkaian adalah sama.")

st.markdown("---")
st.write("Sudah selesai membaca materi? Mari uji pemahamanmu di halaman Kuis!")
if st.button("👉 Ambil Kuis Sekarang"):
    st.switch_page("pages/04_Kuis.py")