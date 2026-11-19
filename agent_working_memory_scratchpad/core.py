"""Core Working Memory Scratchpad with Stack Scoping."""
from typing import Dict, List, Any, Optional

class ScopeFrame:
    def __init__(self, name: str):
        self.name = name
        self.variables: Dict[str, Any] = {}

class WorkingMemoryScratchpad:
    def __init__(self):
        self._stack: List[ScopeFrame] = [ScopeFrame("global")]

    def push_scope(self, scope_name: str):
        self._stack.append(ScopeFrame(scope_name))

    def pop_scope(self) -> ScopeFrame:
        if len(self._stack) <= 1:
            raise IndexError("Cannot pop root global scope")
        return self._stack.pop()

    def set(self, var_name: str, value: Any):
        self._stack[-1].variables[var_name] = value

    def get(self, var_name: str) -> Optional[Any]:
        # Search from top of stack down to global
        for frame in reversed(self._stack):
            if var_name in frame.variables:
                return frame.variables[var_name]
        return None

    def dump_active_bindings(self) -> Dict[str, Any]:
        combined = {}
        for frame in self._stack:
            combined.update(frame.variables)
        return combined
