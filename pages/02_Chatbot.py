import streamlit as st
import time
import random
import re
import string
import sys

# --- 0. KONTROL LOGIN ---
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("❌ Anda harus login untuk mengakses halaman ini.")
    time.sleep(1)
    st.switch_page("00_Login.py") 

# --- 1. LOGIKA CHATBOT DARI PROYEK SEBELUMNYA ---

knowledge_base = {
    "hukum ohm": ["Hukum Ohm menyatakan V = I * R. Tegangan sebanding dengan Arus dan Hambatan.", "Rumus Hukum Ohm adalah V = I * R."],
    "arus listrik": ["Arus listrik (I) adalah aliran muatan elektron. Satuan: Ampere (A)."],
    "tegangan": ["Tegangan (V) adalah beda potensial listrik. Satuan: Volt (V)."],
    "hambatan": ["Hambatan (R) adalah perlawanan material terhadap aliran arus. Satuan: Ohm (Ω)."],
    "transistor": ["Transistor adalah semikonduktor yang digunakan untuk penguat atau sebagai sakelar elektronik."],
    "dioda": ["Dioda adalah semikonduktor yang mengizinkan arus mengalir dalam satu arah (forward bias)."],
    "rangkaian seri": ["Rangkaian seri memiliki komponen tersusun berurutan. Arus sama tapi tegangan berbeda."],
    "rangkaian paralel": ["Rangkaian paralel: komponen sejajar. Tegangan sama tapi arus berbeda."],
    "menu": ["Topik yang tersedia: hukum ohm, arus listrik, tegangan, hambatan, transistor, dioda, rangkaian seri, rangkaian paralel."]
}

synonyms = {
    "ohm": ["hukum ohm", "ohm"],
    "arus": ["arus", "arus listrik", "current", "i", "a"],
    "tegangan": ["tegangan", "voltage", "v"],
    "hambatan": ["hambatan", "resistansi", "r"],
    "seri": ["seri", "rangkaian seri"],
    "paralel": ["paralel", "rangkaian paralel"],
    "transistor": ["transistor", "komponen aktif"],
    "dioda": ["dioda", "diode"]
}

def preprocess_text(text):
    """Membersihkan dan memproses input teks"""
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return ' '.join(text.split())

def find_best_match(processed_input):
    """Mencari kecocokan terbaik untuk input pengguna dari knowledge_base"""
    for keyword, responses in knowledge_base.items():
        if keyword in processed_input:
            return random.choice(responses)

    for keyword, syn_list in synonyms.items():
        for synonym in syn_list:
            if synonym in processed_input and keyword in knowledge_base:
                return random.choice(knowledge_base[keyword])

    return None

def calculate_ohm_law(user_input):
    """Menghitung Hukum Ohm jika terdapat angka dalam pertanyaan"""
    user_input = user_input.lower()
    # Mencari angka (termasuk desimal)
    numbers = re.findall(r'(\d+(?:[.,]\d+)?)', user_input.replace(',', '.'))
    
    if len(numbers) >= 2:
        try:
            val1, val2 = map(float, numbers[:2])
            
            # Mencari R (V dan I diketahui)
            if ("v" in user_input and "i" in user_input and "r" not in user_input):
                r = val1 / val2
                return f"Berdasarkan Hukum Ohm: Nilai Hambatan (R) adalah {r:.2f} Ω (Ohm)."
            
            # Mencari I (V dan R diketahui)
            elif ("v" in user_input and "r" in user_input and "i" not in user_input):
                i = val1 / val2
                return f"Berdasarkan Hukum Ohm: Nilai Arus (I) adalah {i:.2f} A (Ampere)."
            
            # Mencari V (I dan R diketahui)
            elif ("i" in user_input and "r" in user_input and "v" not in user_input):
                v = val1 * val2
                return f"Berdasarkan Hukum Ohm: Nilai Tegangan (V) adalah {v:.2f} V (Volt)."
        except ZeroDivisionError:
            return "ERROR: Pembagian dengan nol tidak diperbolehkan."
        except Exception:
            return "ERROR: Terjadi masalah dalam perhitungan. Coba periksa format angka Anda."
            
    return None

def get_chatbot_response(user_input):
    """Fungsi master yang menghasilkan respons dari chatbot"""
    user_input_lower = user_input.lower()
    processed_input = preprocess_text(user_input)
    
    # Perintah Khusus
    if "menu" in processed_input or "topik" in processed_input:
        return random.choice(knowledge_base['menu'])

    # 1. Prioritas: Perhitungan Hukum Ohm
    calculation_result = calculate_ohm_law(user_input)
    if calculation_result:
        return calculation_result

    # 2. Prioritas: Pencarian Teks (Knowledge Base)
    response = find_best_match(processed_input)
    if response:
        return response
    
    # 3. Respon Default
    return "Maaf, saya tidak mengerti. Saya hanya dapat menjawab topik dasar elektronika. Coba ketik 'menu' atau pertanyaan spesifik seperti 'apa itu dioda?'"


# --- 2. IMPLEMENTASI STREAMLIT (WEB UI) ---

st.set_page_config(
    page_title="Chatbot - LMS Elektronika",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🤖 Asisten AI Elektronika Dasar")
st.markdown("---")

# Inisialisasi riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Pesan Selamat Datang
    st.session_state.messages.append({"role": "assistant", "content": "Halo, saya Chatbot Elektronika UNP. Saya dapat menjawab pertanyaan dasar dan menghitung Hukum Ohm. Silakan bertanya!"})

# Tampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kontrol Input Pengguna
if prompt := st.chat_input("Tanyakan sesuatu tentang elektronika..."):
    # Tambahkan pesan pengguna ke riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Tampilkan pesan pengguna
    with st.chat_message("user"):
        st.markdown(prompt)

    # Dapatkan respons dari Chatbot
    response = get_chatbot_response(prompt)
    
    # Tambahkan respons bot ke riwayat
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Tampilkan respons bot
    with st.chat_message("assistant"):
        st.markdown(response)