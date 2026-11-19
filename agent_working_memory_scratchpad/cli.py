"""CLI for Scratchpad."""
import argparse
from .core import WorkingMemoryScratchpad

def main():
    parser = argparse.ArgumentParser(description="Agent Working Memory Scratchpad CLI")
    parser.add_argument("--demo", action="store_true", help="Run scratchpad demo")
    args = parser.parse_args()

    sp = WorkingMemoryScratchpad()
    sp.set("total_users", 100)
    sp.push_scope("subtask_filter")
    sp.set("active_users", 42)
    print(f"Inside subtask: active={sp.get('active_users')}, total={sp.get('total_users')}")
    sp.pop_scope()
    print(f"After pop: active={sp.get('active_users')}, total={sp.get('total_users')}")

if __name__ == "__main__":
    main()
