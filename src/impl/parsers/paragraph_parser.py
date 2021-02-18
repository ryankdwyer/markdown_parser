"""Implements the ParagraphParser."""

import re

import src.exceptions as exceptions
import src.impl.parsers.parser_base as parser_base


class ParagraphParser(parser_base.ParserBase):
    """Parses blocks of text and formats as html.

    This parser is essentially a 'negative' check of the other parsers. We want
    to ignore blocks of text that start with other known Markdown modifiers.
    Considering the simple case we are solving for here, we will only check for
    the header token '#'. If we were to expand functionality we would need to
    account for other markdown tokens ('>', 1-9, '-', etc.)

    Example Input: 'This is a paragraph'
    Example Output: '<p>This is a paragraph</p>'
    """

    checker = re.compile('^([#])')
    html_mask = '<p>{text}</p>'.format

    @classmethod
    def parse(cls, md_string):
        """Parses a markdown string and returns an html formatted string.

        :param str md_string: A markdown formatted string.

        :return: a string formatted as html
        :rtype: str
        """
        if not md_string:
            return md_string

        try:
            result = cls.checker.match(md_string)
        except TypeError:
            msg = f'Cannot parse an input of type: {type(md_string)}'
            raise exceptions.InvalidInputType(msg)

        # This indicates that we matched a beginning character that signifies
        # a different markdown element, so we skip.
        if result and result.group(0):
            return md_string

        return cls.html_mask(text=md_string)
