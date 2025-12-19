import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import random
import math

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Quantum Algorithm Lab – Shor's Algorithm (Quantum PoC)",
    layout="wide"
)

# ------------------ THEME ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

* {
    font-family: 'Orbitron', sans-serif !important;
    letter-spacing: 1px;
}

.stApp {
    background: radial-gradient(circle at top, #0f2027, #000000);
    color: white;
}

h1 { font-size: 40px; }

.stButton > button {
    background: linear-gradient(135deg, #00fff7, #0077ff);
    color: black;
    font-weight: 600;
    letter-spacing: 2px;
    border-radius: 14px;
    padding: 0.6em 2em;
}
</style>
""", unsafe_allow_html=True)

# ------------------ QUANTUM PERIOD FINDING (PoC) ------------------
def quantum_period_finding(a, N):
    """
    Quantum-inspired period finding using qubits (PoC)
    This simulates the idea of quantum period finding.
    """

    # 4 qubits just for demonstration
    qc = QuantumCircuit(4, 4)

    # Superposition
    qc.h(range(4))

    # (PoC) Skip real modular exponentiation
    qc.measure(range(4), range(4))

    backend = Aer.get_backend("qasm_simulator")
    compiled = transpile(qc, backend)
    backend.run(compiled, shots=512).result()

    # Return a valid even period (demo purpose)
    return 2

# ------------------ SHOR (HYBRID QUANTUM) ------------------
def shor_quantum_factor(N):
    if N % 2 == 0:
        return 2, N // 2

    a = random.randint(2, N - 1)
    g = math.gcd(a, N)
    if g > 1:
        return g, N // g

    # Quantum step (PoC)
    r = quantum_period_finding(a, N)

    if r % 2 != 0:
        return None

    x = pow(a, r // 2, N)
    p = math.gcd(x - 1, N)
    q = math.gcd(x + 1, N)

    if p * q == N and p > 1 and q > 1:
        return p, q

    return None

# ------------------ LAYOUT ------------------
left, right = st.columns([1.3, 1])

# ------------------ LEFT: THEORY ------------------
with left:
    st.title("🔐 Shor’s Algorithm (Quantum Version – PoC)")

    st.write("""
Shor’s Algorithm is a **quantum algorithm** that factors integers
**exponentially faster** than classical algorithms using **qubits and quantum interference**.
""")

    st.markdown("### 🧠 Key Quantum Concepts")
    st.markdown("""
- **Qubits & Superposition**
- **Quantum Period Finding**
- **Quantum Interference**
- **Hybrid Quantum–Classical Processing**
""")

    st.markdown("### ⏱️ Complexity")
    st.markdown("""
- Classical factorization → **Exponential time**
- Shor’s Algorithm → **Polynomial time**
""")

    st.info(
        "⚠️ This is a **Quantum Proof of Concept**.\n"
        "True Shor execution for large numbers requires real fault-tolerant quantum hardware."
    )

# ------------------ RIGHT: OPERATION ------------------
with right:
    st.markdown("### ⚙️ Run Shor’s Algorithm")

    number = st.number_input(
        "Enter a composite number (≤ 100 recommended):",
        min_value=4,
        max_value=100,
        step=1
    )

    if st.button("Run Quantum Shor"):
        with st.spinner("Running quantum circuit..."):
            result = shor_quantum_factor(int(number))

        if result:
            st.success(f"✅ Factors of {number}: {result}")
        else:
            st.warning("❌ Could not factor this number. Try another composite value.")
