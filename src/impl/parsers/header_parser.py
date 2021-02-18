"""Implements the HeaderParser."""

import re

import src.exceptions as exceptions
import src.impl.parsers.parser_base as parser_base


class HeaderParser(parser_base.ParserBase):
    """Parses markdown headers and returns html formatted text.

    Handles headers 1 through 6.

    Example Input: # Title
    Example Output: <h1>Title</h1>

    Note: `#Title` is considered invalid markdown and will be skipped.
    """

    # matches 1 to 6 #'s at the beginning of a string
    checker = re.compile('^ *(#{1,6} )(.*)')
    html_mask = '<h{level}>{text}</h{level}>\n'.format

    @classmethod
    def parse(cls, md_string):
        """Parses the given md_string and returns a string formatted as html.

        If the string does not contain markdown header flags, the original
        string is returned for further processing.

        :param str md_string: An unprocessed markdown node

        :return: a string formatted as html
        :rtype: str
        """
        try:
            result = cls.checker.match(md_string)
        except TypeError:
            msg = f'Cannot parse an input of type: {type(md_string)}'
            raise exceptions.InvalidInputType(msg)

        if not result:
            return md_string

        # We are capturing the trailing space and must account for that.
        level = len(result.group(1)) - 1

        return cls.html_mask(level=level, text=result.group(2))
