# markdown_parser

## Description
Provides a utility for converting basic markdown to HTML. The entry point
expects a markdown formatted string and will output HTML to a given filename.

## Notes:
- Expected Python version: `Python 3.7.3`
- No external modules required. 

## Tests:
To run tests:

From the project root - `./test.sh`

Note: You may have to run `chmod +x test.sh` prior to running the script.

## Use:

To Convert markdown to html:

`python3 convert_md_to_html.py {file_to_conver}.md {output_file_name}.html`

## Approach:

- Process the given markdown string to prepare it for parsing by normalizing
 the white space and breaking the string into individual lines.
- Parse each line by applying each registered Parser. Each parser is responsible
for parsing and formatting a specific markdown element. 
- Process each line of the newly HTML formatted string, removing extraneous
 whitespace.
- Finally, concatenate each line into a complete string and output to the
 given filename.
 
## Drawbacks:

- While regex can be efficient, there is a tradeoff for readability and clarity.
- If more Parsers are added, the order in which they are applied is important.
This could potentially be resolved with a priority queue, to assign each
 parser with a relative weight.
 
 
## Improvements:

 
