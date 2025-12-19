import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Quantum Algorithm Lab",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

* {
    font-family: 'Orbitron', sans-serif;
}

.stApp {
    background: radial-gradient(circle at top, #0f2027, #000000);
}

/* Button styling – balanced size */
.stButton > button {
    width: 100%;
    height: 58px;                 /* ✅ balanced */
    font-size: 17px;              /* ✅ readable */
    font-weight: 600;
    letter-spacing: 1.4px;
    border-radius: 16px;
    background: rgba(255,255,255,0.08);
    color: white;
    border: 1.5px solid rgba(255,255,255,0.25);
    transition: all 0.25s ease;
}

/* Hover glow */
.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 22px rgba(0,255,247,0.7);
}

.block-container {
    padding-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown(
    "<h1 style='text-align:center'>⚛️ Quantum Algorithm Lab</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:#9efeff;font-size:18px'>Explore algorithms powered by quantum logic</p>",
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------------ BUTTON GRID ------------------
col1, col2, col3, col4 = st.columns(4, gap="large")

with col1:
    if st.button("🧮  Shor’s Algorithm"):
        st.switch_page("pages/shor_app.py")

with col2:
    if st.button("🔍  Grover’s Algorithm"):
        st.switch_page("pages/grover_app.py")

with col3:
    if st.button("❓  Simon’s Algorithm"):
        st.switch_page("pages/simon_app.py")

with col4:
    if st.button("⚛️  Quantum Counting"):
        st.switch_page("pages/quantum_counting_app.py")
