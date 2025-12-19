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

.title {
    text-align: center;
    font-size: 2.6rem;
    margin-bottom: 8px;
    letter-spacing: 2px;
}

.subtitle {
    text-align: center;
    color: #9efeff;
    margin-bottom: 40px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 30px;
}

.card {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 35px 25px;
    text-align: center;
    transition: all 0.4s ease;
    cursor: pointer;
    position: relative;
}

.card:hover {
    transform: translateY(-10px) scale(1.03);
}

/* Individual glow colors */
.shor {
    border: 2px solid #00ff55;
    box-shadow: 0 0 30px rgba(0, 255, 85, 0.35);
}
.grover {
    border: 2px solid #ff00ff;
    box-shadow: 0 0 30px rgba(255, 0, 255, 0.35);
}
.simon {
    border: 2px solid #ffaa00;
    box-shadow: 0 0 30px rgba(255, 170, 0, 0.35);
}
.counting {
    border: 2px solid #00fff7;
    box-shadow: 0 0 30px rgba(0, 255, 247, 0.35);
}

.icon {
    font-size: 2.6rem;
    margin-bottom: 15px;
}

.card h2 {
    margin-bottom: 10px;
}

.card p {
    font-size: 0.85rem;
    color: #d0ffff;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 class='title'>⚛️ Quantum Algorithm Lab</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Explore algorithms powered by quantum logic</p>", unsafe_allow_html=True)

# ---------------- GRID ----------------
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

# ---------------- CARD LOOK (FAKE DIVS) ----------------
st.markdown("""
<div class="grid">

<div class="card shor">
    <div class="icon">🧮</div>
    <h2>Shor’s Algorithm</h2>
    <p>Integer factorization using quantum period finding.</p>
</div>

<div class="card grover">
    <div class="icon">🔍</div>
    <h2>Grover’s Algorithm</h2>
    <p>Fast database search with amplitude amplification.</p>
</div>

<div class="card simon">
    <div class="icon">❓</div>
    <h2>Simon’s Algorithm</h2>
    <p>Find hidden patterns in black-box functions.</p>
</div>

<div class="card counting">
    <div class="icon">⚛️</div>
    <h2>Quantum Counting</h2>
    <p>Count solutions using Grover + phase estimation.</p>
</div>

</div>
""", unsafe_allow_html=True)
