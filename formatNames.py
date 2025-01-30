import re

def excludeBrackets(string):
    """Remove content within brackets (round, square, or curly)."""
    string = re.sub(r"\(.*?\)", "", string)
    return string


def formatName(s):
    s = excludeBrackets(s)
    n = len(s)
    substrings = set()
    longest = ""

    # Try all substring lengths from longest to shortest
    for length in range(n, 0, -1):
        for i in range(n - length + 1):
            sub = s[i:i + length]
            if sub in substrings:
                sub = re.split(r"[\\/]", sub)[0]
                return sub  # Found the longest repeating substring
            substrings.add(sub)

    return ""  # No repeating substring found

def formatWinning(s):
    result = s.split("-")[0]
    return result

def formatAgain(formatedData):
    for i in range(len(formatedData)):
        formatedData[i][1] = formatName(formatedData[i][1].strip())
        formatedData[i][3] = formatWinning(formatedData[i][3])
    return formatedData