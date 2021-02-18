"""Implements tests for the HeaderParser class"""

import unittest

import src.exceptions as exceptions
import src.impl.parsers.header_parser as header_parser

HeaderParser = header_parser.HeaderParser


class TestHeaderParser(unittest.TestCase):
    """Implements tests for the HeaderParser class."""

    def test_single_header(self):
        """Tests the `# Title` case."""
        test_case = '# Title'
        expected = '<h1>Title</h1>\n'
        output = HeaderParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_max_header(self):
        """Tests the `###### Title` case."""
        test_case = '###### Title'
        expected = '<h6>Title</h6>\n'
        output = HeaderParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_seven_header(self):
        """Tests the `####### Title` case."""
        test_case = '####### Title'
        expected = test_case
        output = HeaderParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_missing_space(self):
        """Tests the `####### Title` case."""
        test_case = '#Title'
        expected = test_case
        output = HeaderParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_no_match(self):
        """Tests a no match case."""
        test_case = 'This is not a title!'
        expected = test_case
        output = HeaderParser.parse(test_case)

        self.assertEqual(expected, output)

    def test_invalid_input(self):
        """Tests an invalid test_case case."""
        test_case = ['1', 2, None]

        with self.assertRaises(exceptions.InvalidInputType):
            HeaderParser.parse(test_case)

    def test_hanging_newline(self):
        """Tests hanging newlines."""
        test_case = '# Title\n'
        expected = '<h1>Title</h1>\n'
        output = HeaderParser.parse(test_case)

        self.assertEqual(expected, output)
