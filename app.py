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

/* Reduce button size slightly */
.stButton > button {
    width: 100%;
    height: 48px;                 /* ⬅️ reduced from default */
    font-size: 15px;              /* ⬅️ smaller text */
    font-weight: 600;
    letter-spacing: 1.2px;
    border-radius: 14px;
    background: rgba(255,255,255,0.06);
    color: white;
    border: 1px solid rgba(255,255,255,0.25);
    transition: all 0.3s ease;
}

/* Hover glow */
.stButton > button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 18px rgba(0,255,247,0.6);
}

/* Section spacing */
.block-container {
    padding-top: 2.5rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown(
    "<h1 style='text-align:center'>⚛️ Quantum Algorithm Lab</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:#9efeff'>Explore algorithms powered by quantum logic</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------ BUTTON GRID ------------------
col1, col2, col3, col4 = st.columns(4, gap="large")

with col1:
    if st.button("🧮  Shor’s Algorithm"):
        st.switch_page("shor_app.py")

with col2:
    if st.button("🔍  Grover’s Algorithm"):
        st.switch_page("grover_app.py")

with col3:
    if st.button("❓  Simon’s Algorithm"):
        st.switch_page("simon_app.py")

with col4:
    if st.button("⚛️  Quantum Counting"):
        st.switch_page("quantum_counting_app.py")
