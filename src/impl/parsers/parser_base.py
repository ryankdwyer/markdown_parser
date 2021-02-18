"""Implements the Parser base class."""

import abc


class ParserBase(abc.ABC):
    """Base class that all Parse classes must inherit from."""

    @classmethod
    def parse(cls, md_string):
        """Parses the given md_string and returns a string formatted as html.

        :param str md_string: An unprocessed markdown node

        :return: a string formatted as html
        """
