"""Implements the PreProcessor base class."""

import abc

class PreProcessorBase(abc.ABC):
    """Base class that all PreProcessor classes must inherit from."""

    @classmethod
    def run(self, md_string):
        """Processes the initial markdown string.

        Any implementation of this method must return a string.

        :param str md_string: An unprocessed markdown string.

        :return: A string that has been processed.
        :rtype: str
        """
