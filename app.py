import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Quantum Algorithm Lab",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
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

/* Title */
.title {
    text-align: center;
    font-size: 3rem;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #9efeff;
    margin-bottom: 50px;
}

/* Button styling */
div.stButton > button {
    width: 100%;
    height: 70px;              /* 👈 balanced size */
    font-size: 1.1rem;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.25);
    background: rgba(255,255,255,0.08);
    color: white;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 18px rgba(0,255,255,0.6);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>⚛️ Quantum Algorithm Lab</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explore algorithms powered by quantum logic</div>", unsafe_allow_html=True)

# ---------------- BUTTON GRID ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🧮 Shor’s Algorithm"):
        st.switch_page("shor_app.py")

with col2:
    if st.button("🔍 Grover’s Algorithm"):
        st.switch_page("grover_app.py")

with col3:
    if st.button("❓ Simon’s Algorithm"):
        st.switch_page("simon_app.py")

with col4:
    if st.button("⚛️ Quantum Counting"):
        st.switch_page("quantum_counting_app.py")
