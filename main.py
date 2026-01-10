"""
ETABS Designer - Main Application
Extended design routine interface for ETABS with Streamlit
"""

import streamlit as st
from pathlib import Path
import sys

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.auth import AuthManager, SessionStateManager
from utils.session import SessionManager
from modules.etabs_api import ETABSConnector

# Page configuration
st.set_page_config(
    page_title="ETABS Designer",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
SessionStateManager.initialize_session_state()


def render_login_page():
    """Render login/authentication page"""
    st.title("🏗️ ETABS Designer")
    st.subheader("Structural Design Automation")

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.markdown("---")
            st.markdown("### Login")

            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            if st.button("Login", use_container_width=True, key="login_btn"):
                if AuthManager.login(username, password):
                    st.success("Login successful!")
                    st.rerun()

            st.markdown("---")
            st.info("""
                **Demo Credentials:**
                - Username: `admin`
                - Password: `password123`
            """)


def render_home_page():
    """Render home/dashboard page"""
    st.title("🏗️ ETABS Designer Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Status",
            "Connected" if st.session_state.get("etabs_connected") else "Disconnected",
        )

    with col2:
        model_status = "Loaded" if st.session_state.get("model_path") else "No Model"
        st.metric("Current Model", model_status)

    with col3:
        st.metric("User", AuthManager.get_current_user() or "N/A")

    st.markdown("---")

    # Quick actions
    st.subheader("Quick Actions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📁 New Project", use_container_width=True):
            success, msg = SessionManager.new_session()
            if success:
                st.success(msg)
                st.rerun()

    with col2:
        if st.button("📂 Open Project", use_container_width=True):
            st.session_state.show_open_dialog = True

    with col3:
        if st.button("💾 Save Project", use_container_width=True):
            if st.session_state.get("current_model"):
                success, msg = SessionManager.save_session()
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("No project to save")

    with col4:
        if st.button("🔗 Link ETABS Model", use_container_width=True):
            st.session_state.show_link_etabs = True

    # Recent sessions
    st.markdown("---")
    st.subheader("Recent Projects")

    recent = SessionManager.get_recent_sessions(5)
    if recent:
        for session_path in recent:
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.button(
                    Path(session_path).name,
                    use_container_width=True,
                    key=f"recent_{session_path}",
                ):
                    success, msg = SessionManager.open_session(session_path)
                    if success:
                        st.success(msg)
                        st.rerun()
            with col2:
                if st.button("🗑️", key=f"del_{session_path}"):
                    SessionManager.delete_session(session_path)
                    st.rerun()
    else:
        st.info("No recent projects. Create a new project to get started.")

    # Open file dialog
    if st.session_state.get("show_open_dialog"):
        st.session_state.show_open_dialog = False
        st.info("📂 Open feature: Browse and select a saved project file")

    # Link ETABS dialog
    if st.session_state.get("show_link_etabs"):
        st.session_state.show_link_etabs = False
        st.info("🔗 Link ETABS: Select an ETABS model file (.EDB) to load")


def render_sidebar():
    """Render navigation sidebar"""
    with st.sidebar:
        st.title("🏗️ ETABS Designer")

        # User info
        current_user = AuthManager.get_current_user()
        if current_user:
            st.write(f"**Logged in as:** {current_user}")

        st.markdown("---")

        # Navigation
        st.subheader("Navigation")

        page = st.selectbox(
            "Select Module",
            ["Home", "Beam Designer", "Column Designer", "Settings"],
            key="page_selector",
            index=0 if st.session_state.get("current_page") == "Home" else 1,
        )

        st.session_state.current_page = page

        st.markdown("---")

        # Current model info
        if st.session_state.get("current_model"):
            st.subheader("Current Project")
            model = st.session_state.current_model
            st.write(f"**Name:** {model.get('name', 'Untitled')}")
            st.write(f"**Modified:** {st.session_state.get('model_modified', False)}")

        st.markdown("---")

        # Logout button
        if st.button("🚪 Logout", use_container_width=True):
            AuthManager.logout()
            st.rerun()


def main():
    """Main application logic"""

    # Check authentication
    if not AuthManager.is_authenticated():
        render_login_page()
        return

    # Render sidebar for authenticated users
    render_sidebar()

    # Route to appropriate page
    page = st.session_state.get("current_page", "Home")

    if page == "Home":
        render_home_page()
    elif page == "Beam Designer":
        st.header("🏢 Concrete Beam Designer")
        st.info("Beam design module - Coming soon!")
    elif page == "Column Designer":
        st.header("📊 Concrete Column Designer")
        st.info("Column design module - Coming soon!")
    elif page == "Settings":
        st.header("⚙️ Settings")
        st.subheader("Design Parameters")

        with st.form("design_params"):
            col1, col2 = st.columns(2)
            with col1:
                fck = st.number_input(
                    "Concrete Strength (MPa)",
                    min_value=20,
                    max_value=60,
                    value=st.session_state.design_parameters.get(
                        "concrete_strength", 28
                    ),
                )
                design_code = st.selectbox(
                    "Design Code",
                    ["ACI 318-19", "ACI 318-14", "IS 456", "Eurocode 2"],
                    index=0,
                )

            with col2:
                fy = st.number_input(
                    "Steel Grade (MPa)",
                    min_value=250,
                    max_value=500,
                    value=st.session_state.design_parameters.get("steel_grade", 500),
                    step=50,
                )

            if st.form_submit_button("Save Settings", use_container_width=True):
                st.session_state.design_parameters["concrete_strength"] = fck
                st.session_state.design_parameters["steel_grade"] = fy
                st.session_state.design_parameters["design_code"] = design_code
                st.success("Settings saved!")


if __name__ == "__main__":
    main()
