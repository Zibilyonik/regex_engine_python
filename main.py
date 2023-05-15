#Python3
def recursive_match(regex_string, user_string):
    """Match a regex string to a user string.

    Args:
        regex_string (string): The regex string to match.
        user_string (string): The user string to match.

    Returns:
        bool: True if the regex string matches the user string, False otherwise.
    """
    if regex_string == "":
        return True
    if regex_string != "" and user_string == "":
        return False
    if regex_string[0] == user_string[0] or (
        regex_string[0] == "." and user_string[0] != ""
    ):
        if recursive_match(regex_string[1:], user_string[1:]):
            return True
    else:
        return False

def main():
    regex_string, user_string = input().split("|")
    if regex_string == "":
        print(True)
        return
    if regex_string != "" and user_string == "":
        print(False)
        return
    if regex_string[0] == "^" and regex_string[-1] != "$":
        regex_string = regex_string[1:]
        if recursive_match(regex_string, user_string[:len(regex_string)]):
            print(True)
            return
        print(False)
        return
    if regex_string[-1] == "$" and regex_string[0] != "^":
        regex_string = regex_string[:-1]
        user_string = user_string[-len(regex_string):]
        if recursive_match(regex_string, user_string):
            print(True)
            return
        print(False)
        return
    if regex_string[0] == "^" and regex_string[-1] == "$":
        regex_string = regex_string[1:-1]
        if len(regex_string) != len(user_string):
            print(False)
            return
        if recursive_match(regex_string, user_string):
            print(True)
            return
        print(False)
        return
    for i in range(len(user_string)):
        if recursive_match(regex_string, user_string):
            print(True)
            return
        user_string = user_string[i:]
    print(False)

if __name__ == "__main__":
    main()
