# Python3
def recursive_match(regex_string, user_string, index=0):
    """Match a regex string to a user string.

    Args:
        regex_string (string): The regex string to match.
        user_string (string): The user string to match.
        index (int, optional): The index of the regex string to match. Defaults to 0.

    Returns:
        bool: True if the regex string matches the user string, False otherwise.
    """
    if index == len(regex_string):
        return True
    if regex_string[index] == ".":
        return recursive_match(regex_string, user_string, index + 1)
    if regex_string[index] == "?":
        return recursive_match(regex_string, user_string, index + 1) or recursive_match(
            regex_string, user_string[1:], index
        )
    if regex_string[index] == "+":
        return recursive_match(regex_string, user_string, index + 1) or recursive_match(
            regex_string, user_string[1:], index
        )
    if regex_string[index] == "*":
        if index == 0:
            return False
        if regex_string[index - 1] == ".":
            return recursive_match(regex_string, user_string, index + 1)
        if regex_string[index - 1] == user_string[index - 1]:
            return recursive_match(regex_string, user_string, index + 1)
        return recursive_match(regex_string, user_string[1:], index)
    if regex_string[index] == user_string[index]:
        return recursive_match(regex_string, user_string, index + 1)
    return False


def regex_check(regex_string, user_string):
    if regex_string[0] == "^" and regex_string[-1] != "$":
        if recursive_match(regex_string, user_string[: len(regex_string)], 1):
            return True
        return False
    if regex_string[-1] == "$" and regex_string[0] != "^":
        regex_string = regex_string[:-1]
        user_string = user_string[-len(regex_string) :]
        if recursive_match(regex_string, user_string):
            return True
        return False
    if regex_string[0] == "^" and regex_string[-1] == "$":
        regex_string = regex_string[1:-1]
        if len(regex_string) != len(user_string):
            return False
        if recursive_match(regex_string, user_string):
            return True
        return False
    for i in range(len(user_string)):
        if recursive_match(regex_string, user_string, i):
            return True


def main():
    regex_string, user_string = input().split("|")
    if regex_string == "":
        print(True)
        return
    if regex_string != "" and user_string == "":
        print(False)
        return
    print(regex_check(regex_string, user_string))


if __name__ == "__main__":
    main()
