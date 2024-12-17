def main(s):
    """
    The s string variable is given. return the characters in the even position.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return s[1:len(s):2]
s='python'
print(main(s))