import streamlit as st
from ui.simulator_page import show_simulator
from ui.lock_graph_page import show_lock_graph
from ui.timeline_page import show_timeline
from ui.results_page import show_results
from backend.utils import create_required_folders

# 🧩 Initialize session state
if "simulation_complete" not in st.session_state:
    st.session_state.simulation_complete = False
if "timeline" not in st.session_state:
    st.session_state.timeline = []

# 🛠️ App Setup
st.set_page_config(page_title="Kernel Lock Simulator", layout="wide")
create_required_folders()

st.sidebar.subheader("🧪 Analysis Mode")
mode = st.sidebar.radio("Choose Detection Type", ["Deadlock Detection", "Race Condition Detection"])
st.session_state["mode"] = mode

# 📚 Sidebar Navigation
st.sidebar.title("🔧 Navigation")
page = st.sidebar.radio("Go to", ("Simulator", "Lock Graph", "Timeline", "Results"))

# 📦 Page Routing (IMPORTANT: only one is called based on `page`)
if page == "Simulator":
    show_simulator()
elif page == "Lock Graph":
    show_lock_graph()
elif page == "Timeline":
    show_timeline()
elif page == "Results":
    show_results()
