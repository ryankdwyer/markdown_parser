"""Main class for parsing markdown to html."""

import exceptions
import src.impl.parsers.parser_base as parser_base
import src.impl.pre_processors.pre_processor_base as pre_processor_base
import src.impl.post_processors.post_processor_base as post_processor_base


ParserBase = parser_base.ParserBase
PreProcessorBase = pre_processor_base.PreProcessorBase
PostProcessorBase = post_processor_base.PostProcessorBase


class MarkdownParse:
    """Parses text formatted as in markdown and outputs html.

    :cvar list[PreProcessors] pre_processors: A list of PreProcessor class
    instances that handle all text munging prior to parsing.
    :cvar list[Parsers] parsers: A list of Parser class instances that handle
    all parsing of markdown elements to html.
    :cvar list[PostProcessors] post_processors: A list of PostProcessor class
    instances that handle all post processing of generated html.
    """

    pre_processors = []
    parsers = []
    post_processors = []

    def __init__(self, pre_processors=None, parsers=None, post_processors=None):
        """Initializer method.

        :param list[PreProcessors] pre_processors: A list of PreProcessor class
            instances that handle all text munging prior to parsing.
        :param list[Parsers] parsers: A list of Parser class instances that
            handle all parsing of markdown elements to html.
        :param list[PostProcessors] post_processors: A list of PostProcessor
            class instances that handle all post processing of generated html.
        """
        self.register(pre_processors, parsers, post_processors)

    def register(self, pre_processors, parsers, post_processors):
        """Registers the variables

        :param list[PreProcessors] pre_processors: A list of PreProcessor class
            instances that handle all text munging prior to parsing.
        :param list[Parsers] parsers: A list of Parser class instances that
            handle all parsing of markdown elements to html.
        :param list[PostProcessors] post_processors: A list of PostProcessor
            class instances that handle all post processing of generated html.
        """
        self._register(pre_processors, PreProcessorBase, self.pre_processors)
        self._register(post_processors, PostProcessorBase, self.post_processors)
        self._register(parsers, ParserBase, self.parsers)

    def _register(self, instances, base, registry):
        """Validates and registers each instance against the base.

        :param list instances: A list of class instances
        :param Class base: A base class to compare each instance against
        :param list registry: A list to store the instances.

        :raises: InvalidClass
        """
        if not instances:
            msg = f'You must provide at least one instance of {repr(base)}.'
            raise exceptions.MarkdownParserException(msg)
