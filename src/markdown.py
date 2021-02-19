"""Main class for parsing markdown to html."""

import copy
import logging

import src.exceptions as exceptions
import src.impl.parsers.parsers as parsers
import src.impl.pre_processors.processors as pre_processors
import src.impl.post_processors.post_processor_base as post_processor_base

# Aliases

# Parsers
HeaderParser = parsers.HeaderParser
LinkParser = parsers.LinkParser
ParagraphParser = parsers.ParagraphParser

# Processors
NewlineProcessor = pre_processors.NewlineProcessor

# Bases for validation
ParserBase = parsers.ParserBase
PreProcessorBase = pre_processors.PreProcessorBase
PostProcessorBase = post_processor_base.PostProcessorBase

# Constants
SPLIT_TOKEN = '\n\n'

logger = logging.getLogger(__name__)


class MarkdownParser:
    """Parses text formatted as in markdown and outputs html.

    :cvar list[PreProcessors] pre_processors: A list of PreProcessor class
        instances that handle all text munging prior to parsing.
    :cvar list[Parsers] parsers: A list of Parser class instances that handle
        all parsing of markdown elements to html.
    :cvar list[PostProcessors] post_processors: A list of PostProcessor class
        instances that handle all post processing of generated html.
    """

    # We preload these with the defaults
    pre_processors = [NewlineProcessor]
    parsers = [LinkParser, ParagraphParser, HeaderParser]
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
            return

        for instance in instances:
            if not isinstance(instance, base):
                msg = f'{repr(instances)} is not of type {repr(base)}'
                raise exceptions.MarkdownParserException(msg)
            registry.append(instance)

    def preprocess(self, md_copy):
        """Applies each registered preprocessor.

        :param str md_copy: An unprocessed markdown string.

        :return: A list of strings representing the lines of the markdown, ready
        for parsing.
        :rtype: list[str]
        """
        # We will strip leading and trailing white space first.
        md_copy = md_copy.strip()

        for preprocessor in self.pre_processors:
            md_copy = preprocessor.run(md_copy)

        return md_copy.split(SPLIT_TOKEN)

    def apply_parsers(self, md_list):
        """Applies each registered parser.

        :param list[str] md_list: A list of markdown formatted strings.

        :return: A list of html formatted strings
        :rtype: list[str]
        """
        for parser in self.parsers:
            md_list = [parser.parse(line) for line in md_list]

        return md_list

    def postprocess(self, parsed_list):
        """Applies each registered postprocessor.

        :param list[str] parsed_list: A list of html formatted strings.

        :return: A string representing the html output of the original markdown
        :rtype: str
        """
        for postprocessor in self.post_processors:
            parsed_list = [postprocessor.run(line) for line in parsed_list]

        # Stripping each line is not strictly necessary - but makes the output
        # much more readable.
        return SPLIT_TOKEN.join([line.strip() for line  in parsed_list])

    def write_to_html(self, processed, filename):
        """Writes the processed html string to a file.

        :param str processed: The processed markdown->html string.
        :param str filename: The name of the html file to write to.
        """
        with open(filename, 'w') as file_handler:
            file_handler.write(processed)

    def parse(self, markdown, output_name=None):
        """Parses the markdown input and outputs an html file.

        :param str markdown: A markdown formatted string.
        :param str output_name: The name of the html file to output.

        :return
        """
        # We may end up mutating/overwriting some parts, best to keep the
        # original intact.
        md_copy = copy.copy(markdown)

        md_list = self.preprocess(md_copy)
        parsed_list = self.apply_parsers(md_list)
        processed = self.postprocess(parsed_list)

        if output_name:
            self.write_to_html(processed, output_name)
        else:
            return processed
