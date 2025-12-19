import streamlit as st
import random

st.set_page_config(
    page_title="Quantum Algorithm Lab – Simon's Algorithm",
    layout="wide"
)
st.markdown("""
<style>

/* ------------------ FONT IMPORT ------------------ */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&display=swap');

/* ------------------ GLOBAL TYPOGRAPHY FORCE ------------------ */
html, body, div, span, input, textarea, label, button, p, h1, h2, h3, h4 {
    font-family: 'Orbitron', sans-serif !important;
    letter-spacing: 1px !important;
    font-weight: 400;
}

/* Smooth futuristic rendering */
* {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* ------------------ BACKGROUND ------------------ */
.stApp {
    background: radial-gradient(circle at top, #0f2027, #000000);
    color: #ffffff;
}

/* ------------------ HEADINGS ------------------ */
h1 {
    font-size: 42px !important;
    font-weight: 600 !important;
    letter-spacing: 2.5px !important;
}

h2, h3 {
    font-weight: 500 !important;
    letter-spacing: 2px !important;
}

/* ------------------ PARAGRAPH TEXT ------------------ */
p, label {
    font-size: 15px !important;
    letter-spacing: 1.2px !important;
    color: #bffcff !important;
    line-height: 1.7;
}

/* ------------------ INPUT FIELD ------------------ */
input {
    background-color: #1b1f24 !important;
    color: #ffffff !important;
    border-radius: 14px !important;
    border: 1px solid #00fff7 !important;
    font-size: 15px !important;
    letter-spacing: 1.3px !important;
}

/* Remove Streamlit red invalid border */
input[aria-invalid="true"] {
    border: 1px solid #00fff7 !important;
    box-shadow: 0 0 10px rgba(0,255,247,0.5) !important;
}

/* ------------------ BUTTON ------------------ */
.stButton > button {
    background: linear-gradient(135deg, #00fff7, #0077ff);
    color: #000000 !important;
    font-size: 14px !important;
    letter-spacing: 2px !important;
    font-weight: 600 !important;
    border-radius: 16px;
    padding: 0.6em 2em;
    border: none;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.06);
    box-shadow: 0 0 18px #00fff7;
}

/* ------------------ ALERTS ------------------ */
.stSuccess, .stWarning, .stError {
    font-family: 'Orbitron', sans-serif !important;
    letter-spacing: 1px !important;
}

/* ------------------ DIVIDER ------------------ */
hr {
    border: 1px solid #1f3b3b;
}

</style>
""", unsafe_allow_html=True)
# 🔁 SAME CSS BLOCK AS SHOR APP (COPY-PASTE)

def simon_algorithm(hidden_string):
    n = len(hidden_string)
    equations = []
    for _ in range(n):
        x = [random.randint(0, 1) for _ in range(n)]
        if sum(x[i] * hidden_string[i] for i in range(n)) % 2 == 0:
            equations.append(x)
    return equations

left_col, right_col = st.columns([1.3, 1])

with left_col:
    st.title("❓ Simon’s Algorithm (PoC)")

    st.write(
        "Simon’s Algorithm finds a **hidden binary string** in a black-box "
        "function using quantum interference, offering an **exponential "
        "speedup** over classical methods."
    )

    st.markdown("### 🧠 Key Concepts")
    st.markdown(
        "- Hidden XOR structure\n"
        "- Black-box oracle\n"
        "- Quantum interference\n"
        "- Exponential speedup"
    )

    st.markdown("---")
    st.markdown(
        "**Note:** This PoC simulates the measurement outcomes "
        "used to infer the hidden string."
    )

with right_col:
    st.markdown("### ⚙️ Run the Algorithm")

    n = st.slider("Hidden string length:", 3, 6, 4)
    hidden = [random.randint(0, 1) for _ in range(n)]

    if st.button("Run Simon’s Algorithm"):
        eqs = simon_algorithm(hidden)
        st.success("✅ Measurements collected")
        st.write("Hidden string (demo):", hidden)
        st.write("Measured equations:", eqs)
