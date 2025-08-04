# test_linterstatic.py
"""
Tests for LinterStatic module.
"""

import unittest
from linterstatic import LinterStatic

class TestLinterStatic(unittest.TestCase):
    """Test cases for LinterStatic class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LinterStatic()
        self.assertIsInstance(instance, LinterStatic)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LinterStatic()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
