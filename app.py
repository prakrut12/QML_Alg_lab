import streamlit as st

st.set_page_config(
    page_title="Quantum Algorithm Lab",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

* { font-family: 'Orbitron', sans-serif; }

.stApp {
    background: radial-gradient(circle at top, #0f2027, #000000);
    color: white;
}

.title {
    text-align: center;
    font-size: 3rem;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #9efeff;
    margin-bottom: 60px;
}

div.stButton > button {
    width: 100%;
    height: 68px;        /* balanced size */
    font-size: 1.1rem;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.25);
    background: rgba(255,255,255,0.08);
    color: white;
    transition: 0.25s;
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
c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("🧮 Shor’s Algorithm"):
        st.switch_page("shor_app")

with c2:
    if st.button("🔍 Grover’s Algorithm"):
        st.switch_page("grover_app")

with c3:
    if st.button("❓ Simon’s Algorithm"):
        st.switch_page("simon_app")

with c4:
    if st.button("⚛️ Quantum Counting"):
        st.switch_page("quantum_counting_app")
