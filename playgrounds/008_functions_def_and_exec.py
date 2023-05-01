""" Functions can accepts multiple arguments as an iterable."""
def with_keyword_arguments(**kwargs) -> tuple:
    """ This function accepts 0 or more arguments via *arg:iterable
    Returns:
        tuple: rcvd_args, rcvd_arg_squared
    """
    if not kwargs:
        print("Iterable was empty, returning None.")
        return kwargs, None
    a_dict = dict()
    for k, v in kwargs.items():
        a_dict[k] = v.upper()
    return kwargs, a_dict


# receiving more than one value from a function execution.
# more than 1 arg. args are separated with a comma
sent, rcvd =  with_keyword_arguments(city="Los Angeles", state="California")
print(f"sent: {sent}\t=> received: {rcvd}")

sent, rcvd =  with_keyword_arguments(city="Los Angeles")
print(f"sent: {sent}\t=> received: {rcvd}")

sent, rcvd =  with_keyword_arguments()
print(f"sent: {sent}\t=> received: {rcvd}")
