from models.state import State
from typing import Dict, Optional, Any
import json
from pathlib import Path

class Memory:
    def __init__(self):
        self.states: Dict[str, State] = {}
        self.storage_path = Path("data/memory")
        self.storage_path.mkdir(parents=True, exist_ok=True)
    
    def get_state(self, session_id: str) -> State:
        if session_id not in self.states:
            # Try to load from storage
            state = self._load_state(session_id)
            if state:
                self.states[session_id] = state
            else:
                # Create new state
                self.states[session_id] = State(session_id=session_id)
        return self.states[session_id]
    
    def update_state(self, session_id: str, message: Dict[str, Any]) -> None:
        state = self.get_state(session_id)
        state.add_message(message)
        self._save_state(state)
    
    def _save_state(self, state: State) -> None:
        file_path = self.storage_path / f"{state.session_id}.json"
        with open(file_path, 'w') as f:
            json.dump(state.dict(), f)
    
    def _load_state(self, session_id: str) -> Optional[State]:
        file_path = self.storage_path / f"{session_id}.json"
        if file_path.exists():
            with open(file_path, 'r') as f:
                data = json.load(f)
                return State(**data)
        return None

# Create a single instance of Memory
memory = Memory()
