# phone-num-parser

ASSUMPTIONS:
1. Phone nums will be in the format '(###) ###-####'
2. Each num will be on its own new line
3. Input file format is .txt

HOW TO RUN:
1. Clone the repo
2. Navigate to directory where repo was saved
3. Run the following command: python phoneNumParse.py </path/to/file/file.txt> (NOTE: PATH/FILE is a required arg. Script will not work without it)


EDGE CASES NOT HANDLED:
1. Different file types
2. Nums missing area code
3. Different num formats (ie ###-###-####, ###.###.#####, ### ### ####, etc)
