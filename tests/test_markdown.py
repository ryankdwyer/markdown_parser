"""Implements tests for the Markdown class."""

import unittest

import src.exceptions as exceptions
import src.markdown as markdown

MarkdownParser = markdown.MarkdownParser


class TestMarkdown(unittest.TestCase):
    """Test cases for the Markdown module."""

    def setUp(self):
        """setUp method run before each test case."""
        with open('./samples/simple_sample.md', 'r') as md_file:
            self.simple_file = md_file.read()

        with open('./samples/simple_output.html', 'r') as md_file:
            self.simple_output = md_file.read()

    def test_simple_parse(self):
       """Tests a simple parse case."""
