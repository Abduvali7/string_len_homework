def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    if len(a)%2==0 and len(b)%2==0:
        return True
    elif len(a)%2==1 and len(b)%2==1:
        return False