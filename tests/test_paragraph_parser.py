"""Implements tests for the ParagraphParser."""

import unittest

import src.exceptions as exceptions
import src.impl.parsers.paragraph_parser as paragraph_parser

ParagraphParser = paragraph_parser.ParagraphParser


class TestParagraphParser(unittest.TestCase):
    """Implements test cases for the ParagraphParser."""

    expected_mask = '<p>{}</p>'.format

    def test_basic_paragraph(self):
        """Tests a simple paragraph case."""
        test_case = 'This is a paragraph.'
        expected = self.expected_mask(test_case)
        output = ParagraphParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_multiline_paragraph(self):
        """Tests a simple multiline paragraph case."""
        test_case = 'This is a paragraph.\nStill the same paragraph'
        expected = self.expected_mask(test_case)
        output = ParagraphParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_paragraph_with_link(self):
        """Tests a paragraph with an inline link."""
        test_case = 'This is a paragraph with a [link](http://google.com).'
        expected = self.expected_mask(test_case)
        output = ParagraphParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_header_start(self):
        """Tests when a block of text is a header match."""
        test_case = '# This is a header, not a paragraph.'
        expected = test_case
        output = ParagraphParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_leading_whitespace(self):
        """Tests when a block of text has a leader whitespace."""
        test_case = ' This is a paragraph.'
        expected = self.expected_mask(test_case)
        output = ParagraphParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_invalid_input(self):
        """Tests invalid input case."""
        test_case = {'Cannot parse': 'This'}
        with self.assertRaises(exceptions.InvalidInputType):
            ParagraphParser.parse(test_case)

    def test_empty_input(self):
        """Tests empty string input."""
        test_case = ''
        expected = test_case
        output = ParagraphParser.parse(test_case)

        self.assertEqual(expected, output)
