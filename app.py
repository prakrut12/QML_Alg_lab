import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Quantum Algorithm Lab",
    layout="wide"
)

# ------------------ STYLES ------------------
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
    font-size: 46px;
    margin-top: 40px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #7ffcff;
    margin-bottom: 50px;
}

/* Buttons */
.card button {
    width: 100%;
    height: 95px;
    font-size: 18px;
    border-radius: 18px;
    background: rgba(255,255,255,0.06);
    color: white;
    border: 2px solid rgba(255,255,255,0.25);
    transition: all 0.3s ease;
}

.card button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 18px rgba(0,255,255,0.7);
}

/* Color Borders */
.shor button { border-color: #00ff55; }
.grover button { border-color: #ff00ff; }
.simon button { border-color: #ffaa00; }
.counting button { border-color: #00fff7; }
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="title">⚛️ Quantum Algorithm Lab</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Explore algorithms powered by quantum logic</div>', unsafe_allow_html=True)

# ------------------ BUTTON GRID ------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card shor">', unsafe_allow_html=True)
    if st.button("🧮  Shor’s Algorithm"):
        st.switch_page("shor_app")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card grover">', unsafe_allow_html=True)
    if st.button("🔍  Grover’s Algorithm"):
        st.switch_page("grover_app")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card simon">', unsafe_allow_html=True)
    if st.button("❓  Simon’s Algorithm"):
        st.switch_page("simon_app")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card counting">', unsafe_allow_html=True)
    if st.button("⚛️  Quantum Counting"):
        st.switch_page("quantum_counting_app")
    st.markdown('</div>', unsafe_allow_html=True)
