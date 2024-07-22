#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    In a text file, there is 1 char H. Your text editor can execute
    only 2 oprs in this file: Copy All and Paste. Given a # n,
    write a method that calculates the slowest number of opr needed to
    result in exactly n H characters in the file.
    Returns an int
    If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
