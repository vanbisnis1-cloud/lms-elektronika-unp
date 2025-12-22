import streamlit as st
import google.generativeai as genai

st.title("🔍 Diagnosa API Gemini")

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # Mengambil daftar model yang tersedia untuk API Key Anda
    models = genai.list_models()
    
    st.write("### Model yang tersedia untuk kunci Anda:")
    available_models = []
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
            st.code(m.name)
            
    if not available_models:
        st.error("Waduh, kunci Anda tidak punya akses ke model generatif apapun!")
    else:
        st.success(f"Ditemukan {len(available_models)} model aktif.")
        
except Exception as e:
    st.error(f"Error Diagnosa: {e}")
