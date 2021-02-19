"""Utility script for converting markdown to html."""

import argparse

import src.markdown as markdown

MarkdownParser = markdown.MarkdownParser


def parse_args():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('md_file',
                        help='The path to the markdown file to convert.')
    parser.add_argument('-html_filename', help='The html filename to output.')
    return parser.parse_args()


def read_md_file(filename):
    """Reads the md file."""
    with open(filename, 'r') as md_file:
        return md_file.read()


def run_md_parser(md_string, html_filename=None):
    """Parses the md_file."""
    md_parser = MarkdownParser()
    return md_parser.parse(md_string, output_name=html_filename)

def main():
    """Orchestrates parsing."""
    args = parse_args()
    md_string = read_md_file(args.md_file)
    return run_md_parser(md_string, html_filename=args.html_filename)


if __name__ == '__main__':
    main()
