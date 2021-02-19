"""Implements tests for the Markdown class."""

import unittest
import unittest.mock as mock

import src.exceptions as exceptions
import src.markdown as markdown

MarkdownParser = markdown.MarkdownParser


class TestMarkdown(unittest.TestCase):
    """Test cases for the Markdown module."""

    def setUp(self):
        """setUp method run before each test case."""
        self.simple_file = \
            "# Sample Document\n\n" \
            "Hello!\n\n" \
            "This is sample markdown for the [Mailchimp](" \
            "https://www.mailchimp.com) homework assignment."

        self.simple_output = \
            '<h1>Sample Document</h1>\n\n' \
            '<p>Hello!</p>\n\n' \
            '<p>This is sample markdown for the <a ' \
            'href="https://www.mailchimp.com">Mailchimp</a> homework ' \
            'assignment.</p>'

    def test_simple_parse(self):
        """Tests a simple parse case."""
        parser = MarkdownParser()
        output = parser.parse(self.simple_file)
        self.assertEqual(output, self.simple_output)

    def test_passing_bad_post_processor(self):
        """Test passing bad inputs on __init__."""
        with self.assertRaises(exceptions.MarkdownParserException):
            MarkdownParser(post_processors=['TEST'])

    @mock.patch.object(MarkdownParser, 'write_to_html')
    def test_write_to_html_is_called(self, mock_writer):
        """Test the write to html method is called."""
        parser = MarkdownParser()
        filename = 'test.html'
        parser.parse(self.simple_file, filename)
        mock_writer.assert_called_once()
