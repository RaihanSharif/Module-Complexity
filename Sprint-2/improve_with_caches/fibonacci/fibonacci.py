# fibonacci with caching

from functools import cache

# @cache
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(n, memo={}):
    """With memoization, a memo dict is supplied to the function.
    At each recursive call, the memo is populated the first fibonacci is called
    with a certain value (like fibonacci(n - 2)). For all future calls with the same arguemnt
    it just returns the value from the memo. Does not have to recompute
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]