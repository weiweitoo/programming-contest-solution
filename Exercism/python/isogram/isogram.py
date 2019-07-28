import string, re
def is_isogram(string):
    string = re.sub(r'[^A-Za-z]','', string)
    result = set([char for char in string.lower()])
    return True if len(result) == len(string) else False
