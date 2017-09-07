def return_one():
    return 1


def return_two():
    rv = return_one() + 1
    return rv


def return_three():
    rv = return_one() + return_two()
    return rv


def return_four():
    rv = return_three() + return_one()
    return rv


def return_five():
    rv = return_three() + return_two()
    return rv


def return_six():
    rv = return_four() + return_two()
    return rv
