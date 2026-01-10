"""
Authentication and Authorization Module
Manages user login, credential validation, and session security
"""

import streamlit as st
from typing import Tuple, Dict, Optional
import json
import hashlib


class AuthManager:
    """
    Manages user authentication and session security
    """
    
    # In development, using hardcoded credentials
    # For production, integrate with a proper database or authentication service
    VALID_CREDENTIALS = {
        "admin": "password123"  # Change this in production!
    }
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password for storage"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def validate_credentials(username: str, password: str) -> Tuple[bool, str]:
        """
        Validate user credentials
        
        Args:
            username: User's username
            password: User's password
            
        Returns:
            Tuple of (is_valid: bool, message: str)
        """
        if not username or not password:
            return False, "Username and password required"
        
        if username not in AuthManager.VALID_CREDENTIALS:
            return False, "Invalid username or password"
        
        if AuthManager.VALID_CREDENTIALS[username] != password:
            return False, "Invalid username or password"
        
        return True, "Login successful"
    
    @staticmethod
    def login(username: str, password: str) -> bool:
        """
        Authenticate user and set session state
        
        Args:
            username: User's username
            password: User's password
            
        Returns:
            True if login successful
        """
        is_valid, message = AuthManager.validate_credentials(username, password)
        
        if is_valid:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.login_timestamp = st.session_state.get('login_timestamp', '')
            return True
        else:
            st.session_state.authenticated = False
            st.error(message)
            return False
    
    @staticmethod
    def logout() -> None:
        """Logout current user and clear session"""
        st.session_state.authenticated = False
        st.session_state.username = None
        st.session_state.current_model = None
        st.session_state.model_modified = False
        st.success("Logged out successfully")
    
    @staticmethod
    def is_authenticated() -> bool:
        """Check if user is currently authenticated"""
        return st.session_state.get('authenticated', False)
    
    @staticmethod
    def get_current_user() -> Optional[str]:
        """Get the current authenticated username"""
        if AuthManager.is_authenticated():
            return st.session_state.get('username', None)
        return None


class SessionStateManager:
    """
    Manages session state initialization and reset
    """
    
    @staticmethod
    def initialize_session_state() -> None:
        """Initialize all required session state variables"""
        
        # Authentication state
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        
        if 'username' not in st.session_state:
            st.session_state.username = None
        
        # Model management state
        if 'current_model' not in st.session_state:
            st.session_state.current_model = None
        
        if 'model_path' not in st.session_state:
            st.session_state.model_path = None
        
        if 'model_modified' not in st.session_state:
            st.session_state.model_modified = False
        
        if 'model_last_saved' not in st.session_state:
            st.session_state.model_last_saved = None
        
        # ETABS connection state
        if 'etabs_connected' not in st.session_state:
            st.session_state.etabs_connected = False
        
        if 'analysis_completed' not in st.session_state:
            st.session_state.analysis_completed = False
        
        # Design data cache
        if 'frame_data' not in st.session_state:
            st.session_state.frame_data = {}
        
        if 'column_data' not in st.session_state:
            st.session_state.column_data = {}
        
        # Active page tracking
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "Home"
        
        # Design parameters (user inputs)
        if 'design_parameters' not in st.session_state:
            st.session_state.design_parameters = {
                "concrete_strength": 28,  # MPa
                "steel_grade": 500,  # MPa
                "design_code": "ACI 318-19"
            }
    
    @staticmethod
    def reset_model_session() -> None:
        """Reset model-related session state when opening/creating new model"""
        st.session_state.current_model = None
        st.session_state.model_path = None
        st.session_state.model_modified = False
        st.session_state.model_last_saved = None
        st.session_state.etabs_connected = False
        st.session_state.analysis_completed = False
        st.session_state.frame_data = {}
        st.session_state.column_data = {}
    
    @staticmethod
    def mark_model_modified() -> None:
        """Mark current model as modified"""
        st.session_state.model_modified = True
    
    @staticmethod
    def is_model_loaded() -> bool:
        """Check if a model is currently loaded"""
        return st.session_state.model_path is not None
