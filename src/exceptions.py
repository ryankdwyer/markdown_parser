"""Custom Markdown Parser Exceptions."""


class MarkdownParserException(BaseException):
    """The base MarkDown parser exception."""


class InvalidInputType(MarkdownParserException):
    """Raised when an invalid type is passed to a parser."""
