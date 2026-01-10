# ETABS Designer 🏗️

**ETABS Designer** is a Python-based automation tool developed to interface with **CSI ETABS**. It streamlines the structural design workflow by providing a custom Graphical User Interface (GUI) for specific design tasks, starting with Beam Design.

## 🚀 Features

* **🔌 ETABS API Integration:** Directly connects to an open instance of ETABS to read model data and write results.
* **🖥️ User Interface:** A clean GUI (`main_gui.py`) to manage design parameters easily.
* **📐 Beam Design Module:** Automated beam reinforcement calculation and checking (`beam_designer.py`).
* **Modular Architecture:** Organized codebase allowing for easy addition of future modules (e.g., Column Design, Wall Design).

## 📂 Project Structure

```text
ETABS_DESIGNER/
├── modules/
│   ├── etabs_api.py       # Handles the connection and commands to CSI ETABS
│   └── main_gui.py        # The main dashboard of the application
├── pages/
│   └── beam_designer.py   # Specific logic for Beam Design calculations
├── utils/                 # Helper functions and common utilities
├── main.py                # The entry point to run the application
└── requirements.txt       # List of required Python libraries