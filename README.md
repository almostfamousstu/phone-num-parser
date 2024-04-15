# phone-num-parser

ASSUMPTIONS:
1. Phone nums will be in the format '(###) ###-####'
2. Each num will be on its own new line
3. Input file format is .txt
4. File path/name is hardcoded (will only work with phonenumbers.txt)
     --can be modified by updating path/name in line 28

HOW TO RUN:
1. Clone the repo
2. Navigate to directory where repo was saved
3. Run the following command: python phoneNumParse.py


EDGE CASES NOT HANDLED:
1. Different file types
2. Nums missing area code
3. Different num formats (ie ###-###-####, ###.###.#####, ### ### ####, etc)
