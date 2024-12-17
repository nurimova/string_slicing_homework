def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return s[-4:len(s):1]
s="It_Markaz"
n=4
print(main(s,n))
