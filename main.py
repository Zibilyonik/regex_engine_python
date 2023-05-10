regex_string, user_string = input().split("|")
if regex_string == "" or regex_string == user_string or (regex_string == "." and user_string != ""):
    print("True")
else:
    print("False")
    