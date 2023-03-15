def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    if len([s1,s2])%2==0:
        return "[]"
    elif len([s2,s3])%2==0:
        return "[]"
    elif len([s1,s3])%2==0:
        return "[]"
print(main("school", "code", "book"))