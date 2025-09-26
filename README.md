# Interactive Kernel Lock Simulator for Deadlock Detection and Visualization

This project is a Streamlit-based visual simulator designed to demonstrate how multithreaded systems may encounter deadlocks due to improper lock management. It draws inspiration from recent IEEE research and uses lock graphs, timeline simulations, and runtime analysis to visualize concurrency issues.

## 🔧 Features

- Simulate kernel-style thread and lock behavior
- Visualize lock graphs and detect deadlocks
- Step-through timeline of thread execution
- Analyze static and dynamic lock usage
- Educational and interactive web interface







## 🗃️ Project Structure

kernel_lock_simulator/
│
├── app.py                            # 🚀 Main Streamlit entry point
├── requirements.txt                  # 📦 All required libraries
├── README.md                         # 📖 Project overview & setup
│
├── backend/                          # 🧠 Core logic and concurrency simulation
│   ├── thread_simulator.py           # Simulates threads, events, locks
│   ├── lock_graph.py                 # Builds lock graph, detects deadlocks
│   ├── deadlock_predictor.py         # Runtime prediction logic (Cai et al.)
│   ├── static_analyzer.py            # Static lock graph cycle detection (Zhang et al.)
│   ├── race_checker.py               # Shared access/race check logic (Wang et al.)
│   └── models.py                     # Classes: Thread, Lock, Event, Resource
│
├── ui/                               # 🖥️ Streamlit user interface
│   ├── simulator_page.py             # Main simulation interface
│   ├── lock_graph_page.py            # Visual lock graph + cycle highlight
│   ├── timeline_page.py              # Timeline of thread execution
│   ├── results_page.py               # Detection summary & logs
│   └── utils.py                      # Common UI components (buttons, themes)
│
├── assets/                           # 🗃️ Static files and samples
│   ├── examples/                     # Preloaded thread-lock scenarios (JSON)
│   ├── icons/                        # UI icons/logos (optional)
│   └── styles.css                    # Optional custom Streamlit theming
│
├── data/                             # 📊 Saved simulation logs & graphs
│   ├── graphs/                       # Lock graph images (optional cache)
│   └── execution_logs/               # Logs of timeline steps
│
└── docs/                             # 📚 Project documentation
    ├── report.pdf                    # Final report
    ├── ieee_papers_summary.md        # Literature survey summaries
    └── screenshots/                  # Output visuals (UI, graphs, timeline)


# License


## 📌 To Create a Virtual Environment (step-by-step)

```bash
# Step 1: Navigate to your project folder
cd kernel_lock_simulator

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Step 4: Install requirements
pip install -r requirements.txt

