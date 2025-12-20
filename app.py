import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Quantum Algorithm Lab",
    layout="wide"
)

# ------------------ CUSTOM UI ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

* {
    font-family: 'Orbitron', sans-serif;
}

.stApp {
    background: radial-gradient(circle at top, #0f2027, #000000);
    color: white;
}

.title {
    font-size: 2.5rem;
    letter-spacing: 2px;
}

.subtitle {
    font-size: 1rem;
    color: #9efeff;
    margin-bottom: 40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-top:60px;">
    <h1 class="title">Quantum Algorithm Lab</h1>
    <p class="subtitle">Explore algorithms powered by quantum logic</p>
</div>
""", unsafe_allow_html=True)

# ------------------ BUTTON GRID ------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🧮 Shor’s Algorithm", use_container_width=True):
        st.switch_page("pages/shor_app.py")

with col2:
    if st.button("🔍 Grover’s Algorithm", use_container_width=True):
        st.switch_page("pages/grover_app.py")

with col3:
    if st.button("❓ Simon’s Algorithm", use_container_width=True):
        st.switch_page("pages/simon_app.py")

with col4:
    if st.button("⚛️ Quantum Counting", use_container_width=True):
        st.switch_page("pages/quantum_counting_app.py")

