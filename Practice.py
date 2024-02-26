# explaining re.compile
import re

def comp():
    # .compile() is used to compile a regular expression pattern into a regular expression object
    # object can now be used to find matches in strings
    pattern = re.compile(r'\d+') # matches one or more digits

    # .match() is used to determine if the RE matches at the beginning of a string. if it does match() returns a match object.
    # if it does not match() returns None
    match = pattern.match('123 world')
    if match:
        print(match.group())
    else:
        print('No match')
    # Output: ['123', '456']
        
    # slicing: 0 based index
    s = 'hello world'
    print(s[6:]) # skips 6 char from left 'hello ' and prints the rest.. 
    print(s[:5]) # leaves out the remaining 5



def main():
    print("Hello World!")
comp()