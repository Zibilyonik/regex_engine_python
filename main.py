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
    if regex_string[0] == "^":
        regex_string = regex_string[1:]
        while regex_string[index + 1: index + 2] not in ["*","?","+"]:
            if regex_string[index] != user_string[index]:
                return False
            index += 1
    if regex_string[-1] == "$":
        regex_string = regex_string[:-1]
        while regex_string[-1] not in ["*","?","+"]:
            if regex_string[index] != user_string[index] and regex_string[index] != ".":
                return False
            regex_string = regex_string[:-1]
            user_string = user_string[:-1]
    if index + 1 != len(regex_string):
        if regex_string[index + 1:index + 2] == "*":
            star_letter = regex_string[index]
            regex_string = regex_string[:index] + regex_string[index+2:]
            if star_letter == ".":
                return True
            while user_string[index] == star_letter:
                user_string = user_string[:index] + user_string[index+1:]
                if index == len(user_string):
                    return True
            return recursive_match(regex_string, user_string, index + 1)
        if regex_string[index + 1:index + 2] == "+":
            plus_letter = regex_string[index]
            regex_string = regex_string[:index] + regex_string[index+2:]
            if plus_letter != user_string[index] and plus_letter != ".":
                return False
            if plus_letter == "." and index != len(user_string) - 1:
                return True
            while user_string[index] == plus_letter:
                user_string = user_string[:index] + user_string[index+1:]
                if index == len(user_string):
                    return True
            return recursive_match(regex_string, user_string, index + 1)
        if regex_string[index + 1: index + 2] == "?":
            if regex_string[index] == user_string[index]:
                regex_string = regex_string[:index+1] + regex_string[index+2:]
                return recursive_match(regex_string, user_string, index + 1)
            regex_string = regex_string[:index] + regex_string[index+2:]
            return recursive_match(regex_string, user_string, index)
    if regex_string[index] == user_string[index] or regex_string[index] == ".":
        return recursive_match(regex_string, user_string, index + 1)
    return False


def regex_check(regex_string, user_string):
    if len(regex_string) != len(user_string):
        for i in range(len(user_string)):
            if recursive_match(regex_string, user_string[i:]):
                return True
        return False
    else:
        return recursive_match(regex_string, user_string)


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
