# test_relaystream.py
"""
Tests for RelayStream module.
"""

import unittest
from relaystream import RelayStream

class TestRelayStream(unittest.TestCase):
    """Test cases for RelayStream class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RelayStream()
        self.assertIsInstance(instance, RelayStream)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RelayStream()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
