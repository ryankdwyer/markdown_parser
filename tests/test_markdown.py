"""Implements tests for the Markdown class."""

import unittest


class TestMarkdown(unittest.TestCase):
    """Test cases for the Markdown module."""

    def setUp(self):
        """setUp method run before each test case."""
        with open('./samples/simple_sample.md', 'r') as md_file:
            self.simple_file = md_file.read()

    def test_simple_parse(self):
        """Tests a simple parse case."""
