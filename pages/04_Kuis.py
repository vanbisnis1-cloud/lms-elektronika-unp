import streamlit as st
import time

# --- KONTROL LOGIN ---
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("❌ Anda harus login untuk mengakses halaman ini.")
    time.sleep(1)
    st.switch_page("00_Login.py")

st.set_page_config(page_title="Kuis - LMS Elektronika", layout="centered")

st.title("📝 Kuis Elektronika Dasar")
st.write("Uji pemahaman Anda mengenai Hukum Ohm dan Komponen Aktif.")
st.markdown("---")

# Inisialisasi skor di session state
if "quiz_score" not in st.session_state:
    st.session_state["quiz_score"] = 0

with st.form("quiz_form"):
    st.subheader("Pertanyaan 1")
    q1 = st.radio(
        "Apa rumus Hukum Ohm yang benar untuk mencari Tegangan (V)?",
        ["V = I / R", "V = I * R", "V = R / I", "V = I + R"]
    )

    st.subheader("Pertanyaan 2")
    q2 = st.radio(
        "Komponen semikonduktor yang berfungsi sebagai sakelar atau penguat adalah...",
        ["Resistor", "Kapasitor", "Transistor", "Induktor"]
    )

    st.subheader("Pertanyaan 3")
    q3 = st.radio(
        "Satuan dari Arus Listrik adalah...",
        ["Volt", "Ohm", "Ampere", "Watt"]
    )

    submit = st.form_submit_button("Kirim Jawaban")

    if submit:
        score = 0
        if q1 == "V = I * R": score += 33
        if q2 == "Transistor": score += 33
        if q3 == "Ampere": score += 34
        
        st.session_state["quiz_score"] = score
        
        if score >= 66:
            st.success(f"Luar biasa! Skor Anda: {score}/100")
            st.balloons()
        else:
            st.warning(f"Skor Anda: {score}/100. Silakan pelajari kembali materinya.")

if st.button("⬅️ Kembali ke Dashboard"):
    st.switch_page("pages/01_Dashboard.py")