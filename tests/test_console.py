#!/usr/bin/python3
"""
Tests fpor console
"""
import unittest
from console import HBNBCommand

class testConsole(unittest.TestCase):
    """Unittests for console """

    def test_prompt(self):
        """test if prompt is correct"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)