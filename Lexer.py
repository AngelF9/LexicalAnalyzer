import re   # importing the regular expression module. allows us to work with regular expressions. 
            # regular expressions are used to match patterns in strings.

def lexicalAnalyzer(input_string):
    # storing the keywords in a list
    keywords = ['int', 'float', 'char', 'string', 'bool', 'if', 'else', 
                'while', 'for', 'return', 'break', 'continue', 'switch', 
                'case', 'default', 'void', 'main', 'print', 'input', 'true', 
                'false', 'null']

    # Defining The Token Types For The Lexems
    # \b is used to make sure that the keyword is not a part of another word: while and NOT awhile.
    # join is used to join all keywords with a | which means OR
    # () allows \b to be applied to all keywords

    # r is used to make the string a raw string. 
    # In a string when using \ would need to be escaped with another \. r makes it a raw string and \ is not needed to be escaped.
    token_types = {
        'keyword': r"\b(" + "|".join(keywords) + r")\b",

        # regular expression for the following:
        'seperator': r"[();]",  # matches any single char that is () or ;
        'identifier': r"\b[a-zA-Z][a-zA-Z0-9]*\b", 
        'operator': r"[<>=]", 
        'int': r"(-)?(0-9)+",

        # one or more digits: \d+
        # followed by a decimal point: \.
        # followed by one or more digits: \d+
        'real': r"\b\d+\.\d+\b" 
    }

    # Create a list of tuples to store the tokens
    tokens = []

    # Loop through the input string
    while input_string:
        match = None # will hold the result of the RE match if one is found

        for token_type, token_Re in token_types.items():
            regex = re.compile(token_Re) # compile the regular expression pattern into a regular expression object
            
            # do not need to loop through the input_string. instead use the RE to match patterns.
            match = regex.match(input_string) # match the regular expression pattern to the input string
            if match:
                # TODO: store the token and lexeme in tokens. 
                break

        if not match: # if no token matched, there is an error in the input
            print("Error: Invalid input")
            return
    return tokens
