""" Functions can accepts multiple arguments as an iterable."""
def with_one_or_more_args(*args) -> tuple:
    """ This function accepts 0 or more arguments via *arg:iterable
    Returns:
        tuple: rcvd_args, rcvd_arg_squared
    """
    if not args:
        return args, None
    doubled = tuple([x**2 for x in args])
    return args, doubled


# receiving more than one value from a function execution.
# more than 1 arg. args are separated with a comma
sent, rcvd = with_one_or_more_args(4,8)
print(f"sent: {sent}\t=> received: {rcvd}")

sent, rcvd = with_one_or_more_args(1)  # one arg
print(f"sent: {sent}\t=> received: {rcvd}")

sent, rcvd = with_one_or_more_args()  # no arg
print(f"sent: {sent}\t=> received: {rcvd}")
