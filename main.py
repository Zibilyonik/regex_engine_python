#Python3
def recursive_match(regex_string, user_string):
    if regex_string == "":
        print(True)
        return
    if regex_string != "" and user_string == "":
        print(False)
        return
    if regex_string[0] == user_string[0] or (
        regex_string[0] == "." and user_string[0] != ""
    ):
        recursive_match(regex_string[1:], user_string[1:])
    else:
        print(False)
        return
def main():
    regex_string, user_string = input().split("|")
    recursive_match(regex_string, user_string)
if __name__ == "__main__":
    main()
