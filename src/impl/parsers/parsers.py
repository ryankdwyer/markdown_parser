"""Single entry point for all parsers."""

import src.impl.parsers.header_parser as header_parser
import src.impl.parsers.link_parser as link_parser
import src.impl.parsers.paragraph_parser as paragraph_parser
import src.impl.parsers.parser_base as parser_base

HeaderParser = header_parser.HeaderParser
LinkParser = link_parser.LinkParser
ParagraphParser = paragraph_parser.ParagraphParser
ParserBase = parser_base.ParserBase
