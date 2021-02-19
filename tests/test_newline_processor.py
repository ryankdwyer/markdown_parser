"""Implements tests for NewlineProcessor class."""

import unittest

import src.exceptions as exceptions
import src.impl.pre_processors.newline_processor as newline_processor

NewlineProcessor = newline_processor.NewlineProcessor


class TestNewlineProcessor(unittest.TestCase):
    """Implements test cases for the NewlineProcessor."""

    def test_basic_case(self):
        """Tests a simple replacement case."""
        test_case = 'This has too many new lines\n\n\n'
        expected = 'This has too many new lines\n\n'
        output = NewlineProcessor.run(test_case)

        self.assertEqual(expected, output)

    def test_paragraph_case(self):
        """Tests a paragraph replacement case."""
        test_case = 'This has too many new lines\n' \
                    'Still part of the block\n\n' \
                    'This is a new paragraph\n\n\n'
        expected = 'This has too many new lines\n' \
                    'Still part of the block\n\n' \
                    'This is a new paragraph\n\n'
        output = NewlineProcessor.run(test_case)

        self.assertEqual(expected, output)

    def test_invalid_input(self):
        """Tests invalid input case."""
        test_case = ['Cannot parse this.']
        with self.assertRaises(exceptions.InvalidInputType):
            NewlineProcessor.run(test_case)
