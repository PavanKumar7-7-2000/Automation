import re

def Find_The_Match(pattern_to_search, given_string):

    match = re.search(pattern_to_search, given_string)

    start = match.start()

    end = match.end()

    return start, end


if __name__ == "__main__" :

    given_string = "day-11"
    
    match = Find_The_Match("day-[0-9]*",given_string)

    print(match)