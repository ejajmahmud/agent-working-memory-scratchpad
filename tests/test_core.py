"""Tests for Scratchpad."""
import unittest
from agent_working_memory_scratchpad.core import WorkingMemoryScratchpad

class TestWorkingMemoryScratchpad(unittest.TestCase):
    def test_scoping_and_shadowing(self):
        sp = WorkingMemoryScratchpad()
        sp.set("x", 10)
        self.assertEqual(sp.get("x"), 10)

        sp.push_scope("local")
        sp.set("x", 20)
        self.assertEqual(sp.get("x"), 20)

        sp.pop_scope()
        self.assertEqual(sp.get("x"), 10)
