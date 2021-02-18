"""Implements the LinkParser class."""

import re

import src.exceptions as exceptions
import src.impl.parsers.parser_base as parser_base


class LinkParser(parser_base.ParserBase):
    """Implements the LinkParser.

    Example Input: [with an inline link](http://google.com)
    Example Output: <a href="http://google.com">with an inline link</a>
    """

    checker = re.compile('(\[(.*)\]\((.*)\))')
    html_mask = '<a href="{link}">{text}</a>'.format

    @classmethod
    def parse(cls, md_string):
        """Parses the given md_string and returns a string formatted as html.

        If the string does not contain markdown link flags, the original
        string is returned for further processing.

        :param str md_string: An unprocessed markdown node

        :return: a string formatted as html
        """
        try:
            return re.sub(cls.checker, cls.replacer, md_string)
        except TypeError:
            msg = f'Cannot parse an input of type: {type(md_string)}'
            raise exceptions.InvalidInputType(msg)

    @classmethod
    def replacer(cls, match):
        """Passed to the re.sub function call to process the match.

        :param re.Match match: The matched occurrence of a link token in the
        markdown string.

        :return: An html formatted string representing a link.
        :rtype: str
        """
        print(match.group(0))
        return cls.html_mask(link=match.group(3), text=match.group(2))
