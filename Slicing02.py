def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return s[-1: -5 :-1]
s='congratulation'
print(main(s))