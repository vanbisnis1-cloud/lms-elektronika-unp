import streamlit as st
import streamlit.components.v1 as components

st.title("📝 Kuis Elektronika")
st.write("Uji pemahaman Anda dengan menyelesaikan kuis berikut.")
st.markdown("---")

# Embed code dari Wayground
kuis_embed = """
<div style="width:100%;display:flex;flex-direction:column;gap:8px;min-height:635px;">
    <iframe src="https://wayground.com/embed/quiz/6a1ff178d035b7da125d7301" title="Kuis Elektronika - Wayground" style="flex:1;" frameBorder="0" allowfullscreen></iframe>
    <a href="https://wayground.com/admin?source=embedFrame" target="_blank">Explore more at Wayground.</a>
</div>
"""

# Menampilkan kuis
components.html(kuis_embed, height=700, scrolling=True)

if st.button("⬅️ Kembali ke Dashboard"):
    st.switch_page("modules/01_Dashboard.py")
