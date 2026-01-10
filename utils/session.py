"""
Session Management Module
Handles New, Open, Save operations with caching and persistence
"""

import os
import json
import pickle
import shutil
from pathlib import Path
from typing import Tuple, Dict, Any, Optional
from datetime import datetime
import streamlit as st


class SessionManager:
    """
    Manages session lifecycle: New, Open, Save, Save As operations
    """
    
    CACHE_DIR = Path("cache")
    SESSIONS_DIR = CACHE_DIR / "sessions"
    AUTOSAVE_INTERVAL = 5  # minutes
    
    def __init__(self):
        self._ensure_cache_directories()
    
    @staticmethod
    def _ensure_cache_directories() -> None:
        """Create cache directories if they don't exist"""
        SessionManager.CACHE_DIR.mkdir(exist_ok=True)
        SessionManager.SESSIONS_DIR.mkdir(exist_ok=True)
    
    @staticmethod
    def new_session() -> Tuple[bool, str]:
        """
        Create a new session
        
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            st.session_state.current_model = {
                "name": "Untitled Model",
                "created_date": datetime.now().isoformat(),
                "last_modified": datetime.now().isoformat(),
                "etabs_file": None,
                "design_data": {},
                "design_parameters": {}
            }
            st.session_state.model_path = None
            st.session_state.model_modified = True
            
            return True, "New session created successfully"
        except Exception as e:
            return False, f"Error creating new session: {e}"
    
    @staticmethod
    def open_session(session_path: str) -> Tuple[bool, str]:
        """
        Open an existing session from disk
        
        Args:
            session_path: Path to saved session file (.json)
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if not os.path.exists(session_path):
            return False, f"Session file not found: {session_path}"
        
        try:
            with open(session_path, 'r') as f:
                session_data = json.load(f)
            
            st.session_state.current_model = session_data
            st.session_state.model_path = session_path
            st.session_state.model_modified = False
            
            return True, f"Session opened: {session_path}"
        except Exception as e:
            return False, f"Error opening session: {e}"
    
    @staticmethod
    def save_session(session_path: Optional[str] = None) -> Tuple[bool, str]:
        """
        Save current session to disk
        
        Args:
            session_path: Path where session should be saved. If None, updates current path.
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if not st.session_state.get('current_model'):
            return False, "No active session to save"
        
        try:
            # Determine save path
            if session_path is None:
                if st.session_state.model_path is None:
                    return False, "No save location specified. Use Save As first."
                session_path = st.session_state.model_path
            
            # Update metadata
            st.session_state.current_model['last_modified'] = datetime.now().isoformat()
            
            # Ensure directory exists
            Path(session_path).parent.mkdir(parents=True, exist_ok=True)
            
            # Save to file
            with open(session_path, 'w') as f:
                json.dump(st.session_state.current_model, f, indent=4)
            
            st.session_state.model_path = session_path
            st.session_state.model_modified = False
            
            return True, f"Session saved: {session_path}"
        except Exception as e:
            return False, f"Error saving session: {e}"
    
    @staticmethod
    def save_as(new_path: str) -> Tuple[bool, str]:
        """
        Save current session with a new filename
        
        Args:
            new_path: New file path for the session
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if not new_path.endswith('.json'):
            new_path += '.json'
        
        return SessionManager.save_session(new_path)
    
    @staticmethod
    def get_recent_sessions(max_count: int = 10) -> list:
        """
        Get list of recently saved sessions
        
        Args:
            max_count: Maximum number of recent sessions to return
            
        Returns:
            List of session file paths
        """
        try:
            session_files = list(SessionManager.SESSIONS_DIR.glob("*.json"))
            # Sort by modification time, most recent first
            session_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            return [str(f) for f in session_files[:max_count]]
        except Exception as e:
            print(f"Error getting recent sessions: {e}")
            return []
    
    @staticmethod
    def autosave_session() -> bool:
        """
        Auto-save current session if it has been modified
        
        Returns:
            True if saved successfully or no save needed
        """
        if not st.session_state.get('model_modified'):
            return True
        
        # Create autosave filename
        autosave_name = "autosave.json"
        autosave_path = SessionManager.SESSIONS_DIR / autosave_name
        
        success, message = SessionManager.save_session(str(autosave_path))
        return success
    
    @staticmethod
    def list_all_sessions() -> list:
        """
        Get list of all saved sessions
        
        Returns:
            List of (filename, filepath, last_modified) tuples
        """
        try:
            sessions = []
            for session_file in SessionManager.SESSIONS_DIR.glob("*.json"):
                if session_file.name != "autosave.json":  # Exclude autosave
                    stat = session_file.stat()
                    sessions.append({
                        "name": session_file.name,
                        "path": str(session_file),
                        "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
                    })
            
            # Sort by modification time
            sessions.sort(key=lambda x: x['last_modified'], reverse=True)
            return sessions
        except Exception as e:
            print(f"Error listing sessions: {e}")
            return []
    
    @staticmethod
    def delete_session(session_path: str) -> Tuple[bool, str]:
        """
        Delete a saved session
        
        Args:
            session_path: Path to session file to delete
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            if os.path.exists(session_path):
                os.remove(session_path)
                return True, f"Session deleted: {session_path}"
            else:
                return False, "Session file not found"
        except Exception as e:
            return False, f"Error deleting session: {e}"
    
    @staticmethod
    def cache_frame_data(frame_data: Dict[str, Any]) -> bool:
        """Cache frame design data"""
        try:
            cache_path = SessionManager.CACHE_DIR / "frame_data.pkl"
            with open(cache_path, 'wb') as f:
                pickle.dump(frame_data, f)
            return True
        except Exception as e:
            print(f"Error caching frame data: {e}")
            return False
    
    @staticmethod
    def load_cached_frame_data() -> Optional[Dict[str, Any]]:
        """Load cached frame design data"""
        try:
            cache_path = SessionManager.CACHE_DIR / "frame_data.pkl"
            if cache_path.exists():
                with open(cache_path, 'rb') as f:
                    return pickle.load(f)
        except Exception as e:
            print(f"Error loading cached frame data: {e}")
        return None
