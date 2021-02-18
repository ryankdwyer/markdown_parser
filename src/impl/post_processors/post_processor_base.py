"""Implements the PostProcessor base class."""

import abc


class PostProcessorBase(abc.ABC):
    """Base class that all PostProcessor classes must inherit from."""

    @classmethod
    def run(self, parsed_list):
        """Processes a list of parsed strings.

        Any implementation of this method must return a list of strings.

        :param list[str] parsed_list: An parsed list of html strings.

        :return: A string that has been processed.
        :rtype: str
        """
