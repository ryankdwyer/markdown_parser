"""Quick script for generating very large random markdown files."""

import random

if __name__ == '__main__':
    lines = 1000

    samples = [
        '### Title\n\n',
        'This is a paragraph [with an inline link](http://google.com). Neat, eh?\n\n',
        "How are you?\nWhat's going on?\n\n",
        '\n\n\n',
        '# Big Title'
    ]

    with open('./test_file.md', 'w') as f:
        for line in range(lines):
            f.write(random.choice(samples))
