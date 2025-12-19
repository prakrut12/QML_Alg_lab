import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Quantum Algorithm Lab",
    layout="wide"
)

# ------------------ CUSTOM UI (FROM index.html) ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

* {
    font-family: 'Orbitron', sans-serif;
    box-sizing: border-box;
}

.stApp {
    min-height: 100vh;
    background: radial-gradient(circle at top, #0f2027, #000000);
    color: white;
}

.container {
    width: 90%;
    max-width: 1100px;
    margin: auto;
    padding-top: 80px;
    text-align: center;
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

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 25px;
}

.card {
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 35px 25px;
    cursor: pointer;
    transition: all 0.4s ease;
    backdrop-filter: blur(15px);
    position: relative;
}

.card:hover {
    transform: translateY(-10px) scale(1.03);
}

.card h2 {
    margin: 10px 0;
    font-size: 1.2rem;
}

.card p {
    font-size: 0.85rem;
    color: #d0ffff;
}

.icon {
    font-size: 2.5rem;
    margin-bottom: 15px;
}

/* Accent borders */
.shor {
    border: 2px solid #00ff55;
    box-shadow: 0 0 35px rgba(0,255,85,0.35);
}

.grover {
    border: 2px solid #ff00ff;
    box-shadow: 0 0 35px rgba(255,0,255,0.35);
}

.simon {
    border: 2px solid #ffaa00;
    box-shadow: 0 0 35px rgba(255,170,0,0.35);
}

.quantum {
    border: 2px solid #00fff7;
    box-shadow: 0 0 35px rgba(0,255,247,0.35);
}
</style>
""", unsafe_allow_html=True)

# ------------------ UI CONTENT ------------------
st.markdown("""
<div class="container">
    <h1 class="title">Quantum Algorithm Lab</h1>
    <p class="subtitle">Explore algorithms powered by quantum logic</p>
</div>
""", unsafe_allow_html=True)

# ------------------ CARDS (BUTTONS) ------------------
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

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
