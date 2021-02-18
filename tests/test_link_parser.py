"""Implements tests for the LinkParser class"""

import unittest

import src.exceptions as exceptions
import src.impl.parsers.link_parser as link_parser

LinkParser = link_parser.LinkParser


class TestLinkParser(unittest.TestCase):
    """Implements tests for the LinkParser."""

    def test_single_link(self):
        """Tests a single valid link."""
        test_case = '[with an inline link](http://google.com)'
        expected = '<a href="http://google.com">with an inline link</a>'
        result = LinkParser.parse(test_case)

        self.assertEqual(expected, result)

    def test_single_link_in_text(self):
        """Tests a single valid link in text."""
        test_case = 'There is a link here ' \
                    '[with an inline link](http://google.com)'
        expected = 'There is a link here ' \
                   '<a href="http://google.com">with an inline link</a>'
        result = LinkParser.parse(test_case)

        self.assertEqual(expected, result)

    def test_multiple_links(self):
        """Tests multiple links."""
        test_case = 'Link 1: [here](http://google.com) ' \
                    'Link 2: [there](http://google.com)'
        expected = 'Link 1: <a href="http://google.com">here</a> ' \
                   'Link 2: <a href="http://google.com">there</a>'
        result = LinkParser.parse(test_case)

        self.assertEqual(expected, result)
