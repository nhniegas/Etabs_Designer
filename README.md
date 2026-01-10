# ETABS Designer
## Structural Design Automation Software Extension

ETABS Designer is an extended software built on top of CSI ETABS that provides an isolated, streamlined design routine interface using Streamlit, comtypes, and Python. This tool enables structural engineers to efficiently perform design calculations and verification for concrete structures directly from a web-based interface while maintaining direct integration with ETABS models.

---

## 📋 Key Features

### A. Security Feature ✅
- User authentication with login/logout functionality
- Session-based access control
- Secure credential management
- Demo credentials for development: `admin` / `password123`

### B. Session State Management ✅
- **New:** Create new design projects
- **Open:** Load previously saved design sessions
- **Save:** Save active design work with metadata
- **Save As:** Export designs to new file locations
- **Auto-save:** Automatic periodic session backups
- **Cache Management:** Session persistence and recovery

### C. Direct Data Extraction from ETABS ✅
- Link ETABS model files (.EDB)
- Automatic analysis trigger if not performed
- Real-time data extraction via comtypes API
- Support for frame elements, loads, and results
- Design-specific data filtering

### D. ETABS Designer Modules ✅

#### 1. Concrete Beam Designer
- **Interactive Editing:** Real-time section modifications
- **Design Input:** Width, depth, reinforcement details
- **Flexure Verification:** Moment capacity calculation (ACI 318)
- **Shear Verification:** Shear strength check
- **Real-time Results:** Instant design updates
- **Capacity Ratios:** Safety assessment
- **Design Summary:** Results export and documentation

#### 2. Concrete Column Designer
- **Section Properties:** Rectangular column design
- **Axial Load:** Compression capacity calculation
- **Biaxial Bending:** Interaction checks (Bresler formula)
- **Steel Ratio Validation:** Min/max reinforcement checks
- **Design Verification:** Comprehensive safety checks
- **Results Export:** CSV export functionality

---

## 🛠️ Technology Stack

- **Frontend:** Streamlit (Web UI)
- **ETABS Integration:** comtypes (COM API)
- **Core Logic:** Python 3.8+
- **Data Processing:** pandas, numpy
- **Storage:** JSON (sessions), Pickle (cache)

---

## 📦 Installation & Setup

### Prerequisites
1. **ETABS:** CSI ETABS 2020 or newer (installed on your machine)
2. **Python:** Version 3.8 or higher
3. **Windows:** This software runs on Windows (ETABS API requirement)

### Step 1: Clone Repository
```bash
git clone https://github.com/nhniegas/Etabs_Designer.git
cd Etabs_Designer
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Application
```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 🚀 Quick Start Guide

### 1. Login
- Use the demo credentials: **admin** / **password123**
- (Change these in `utils/auth.py` for production use)

### 2. Create New Project
- Click "📁 New Project" on the Home dashboard
- Optionally link an ETABS model file

### 3. Design Concrete Beams
- Navigate to "Beam Designer" module
- Enter section dimensions and reinforcement details
- Click "Analyze Section" for instant verification
- Save designs to project

### 4. Design Concrete Columns
- Navigate to "Column Designer" module
- Input column properties and loading conditions
- Verify axial and biaxial bending capacity
- Export results as CSV

### 5. Save & Export
- Save your project using "💾 Save Project"
- Download design summaries as CSV files
- Projects are stored in `cache/sessions/` folder

---

## 📁 Project Structure

```
Etabs_Designer/
├── main.py                      # Main Streamlit application
├── requirements.txt             # Python dependencies
├── README.md                    # This file
│
├── modules/
│   ├── __init__.py
│   └── etabs_api.py            # ETABS API wrapper class
│
├── utils/
│   ├── __init__.py
│   ├── auth.py                 # Authentication & session management
│   └── session.py              # Project save/load functionality
│
├── pages/
│   ├── __init__.py
│   ├── beam_designer.py        # Concrete beam design module
│   └── column_designer.py      # Concrete column design module
│
├── config/                      # Configuration files (future)
│
└── cache/
    └── sessions/               # Saved design projects
```

---

## 🔐 Default Credentials
| Field | Value |
|-------|-------|
| Username | admin |
| Password | password123 |

**⚠️ IMPORTANT:** Change these credentials before deploying to production!

---

## 🎯 Design Specifications Implemented

### Concrete Beam Design (ACI 318-19)
- Rectangular section analysis
- Moment capacity calculation
- Shear strength verification
- Steel ratio validation
- Design code compliance checks

**Parameters:**
- Concrete strength: 20-60 MPa
- Steel grade: 250-500 MPa
- Cover: 20-75 mm

### Concrete Column Design (ACI 318-19)
- Axial load capacity
- Biaxial bending interaction (Bresler formula)
- Steel ratio limits (1%-8%)
- Tied and spiral column support
- Load combination handling

**Parameters:**
- Column width/depth: 150-1000 mm
- Axial loads: 0-50,000 kN
- Bending moments: 0-5,000 kN-m

---

## 🔌 ETABS API Integration

### ETABSConnector Class Methods:

```python
from modules.etabs_api import ETABSConnector

etabs = ETABSConnector()

# Connect to ETABS
etabs.connect()

# Open model
etabs.open_model("path/to/model.EDB")

# Run analysis
etabs.run_analysis()

# Extract frame data
frame_data = etabs.get_frame_data()

# Extract column data
column_data = etabs.get_column_data()

# Disconnect
etabs.disconnect()
```

---

## 💾 Session Management

### Save Session
Sessions are automatically saved with:
- Project name and timestamp
- Design parameters
- ETABS file reference
- Design results

### Auto-save Feature
- Automatic saves every 5 minutes (configurable)
- Located in `cache/sessions/` folder
- JSON format for easy import/export

---

## 📊 Export Capabilities

### CSV Export
- Design summaries (beams and columns)
- Section properties
- Design results
- Load combinations

### JSON Export
- Complete project sessions
- Design parameters
- Model references

---

## 🐛 Troubleshooting

### Issue: "Not connected to ETABS"
- Ensure ETABS is installed and running
- Check ETABS installation path
- Verify comtypes is properly installed: `pip install comtypes`

### Issue: "Model file not found"
- Verify ETABS file path is correct
- Ensure file has .EDB extension
- Check file permissions

### Issue: Streamlit not running
- Activate virtual environment: `venv\Scripts\activate`
- Reinstall streamlit: `pip install --upgrade streamlit`
- Clear cache: `streamlit cache clear`

---

## 🔄 Future Enhancements

- [ ] Slab designer module
- [ ] Footing designer module
- [ ] Wall designer module
- [ ] Connection designer module
- [ ] Database integration for credentials
- [ ] Multi-user support
- [ ] Real-time collaboration
- [ ] Advanced concrete codes (IS 456, Eurocode 2)
- [ ] 3D visualization
- [ ] Report generation (PDF)

---

## 📝 License & Author

**Developer:** Nhel Niegas  
**Repository:** https://github.com/nhniegas/Etabs_Designer

---

## 📞 Support & Contribution

For bugs, feature requests, or contributions:
1. Open an issue on GitHub
2. Submit pull requests
3. Contact the development team

---

## ⚖️ Disclaimer

This software is provided as-is for structural design assistance. Users are responsible for:
- Verifying all calculations
- Checking compliance with local building codes
- Professional engineering judgment
- Final design approval

**Always validate results with independent calculations and professional review before implementation in actual projects.**

---

**Last Updated:** December 2025 
