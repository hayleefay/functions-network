def return_one():
    # called by return_two
    return 1


def return_two():
    rv = return_one() + 1
    return rv


def return_three():
    rv = return_one() + return_two()
    return rv
