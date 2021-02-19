"""Implements a NewlineProcessor."""

import re

import src.exceptions as exceptions
import src.impl.pre_processors.pre_processor_base as base


class NewlineProcessor(base.PreProcessorBase):
    """Normalizes newline characters separating lines.

    For markdown -> html we can convert instances of multiple newline
    characters. Anything more than 2 newline characters we can reduce to 2 new
    line characters. This will allow us to split the markdown text on the
    double new line character. As a result, we will preserve multiline
    paragraphs.

    Some consideration must be made for markdown files generated on non-unix
    like machines. Windows based machines may generate files where \r\n is used
    to signify a new line. To simplify this exercise we will assume all files
    are generated in a Unix environment.

    Example:
         'This has too many new line characters\n\n\n'
    Output:
        'This has too many new line characters\n\n'
    """

    # We check for cases where 3 or more newlines are used.
    checker = re.compile('(\n{3,})$')
    replacement = '\n\n'

    @classmethod
    def run(cls, md_string):
        """Processes a markdown string, normalizing whitespace.

        :param str md_string: A markdown formatted string

        :return: A str with normalized newline characters.
        """
        try:
            # Removes and normalizes whitespace in the middle of the string.
            result = re.sub(cls.checker, cls.replacement, md_string)
        except TypeError:
            msg = f'Cannot parse an input of type: {type(md_string)}'
            raise exceptions.InvalidInputType(msg)

        return result
