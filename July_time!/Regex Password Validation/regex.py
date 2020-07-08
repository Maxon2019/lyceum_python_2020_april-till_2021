"""You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters."""


def regex_password_validation(regex):
    dig = False
    low = False
    up = False
    lenn = False

    for i in regex:
        if i.isdigit():
            dig = True
        if i.islower():
            low = True
        if i.isupper():
            up = True
        if len(regex) >= 6:
            lenn = True
        if i == ' ':
            return False
    if dig and low and up and lenn:
        return True
    else:
        return False


if __name__ == '__main__':
    print(regex_password_validation('djI38D55'))
