#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Linear Recursion

Linear recursion is when a recursive function calls itself only once in the body.

This is a basic recursive function with one base case and one recursive call.

"""


def reverse_list(to_reverse: list) -> list:
    """
    Reverses the items from one list into a new list without modifying the original.

    base case:
        empty list          ->   a new empty list
    recursive case:
        non-empty list  ->   ƒ(list without first item) + a list with only first item
    """
    if len(to_reverse) == 0:  # base case
        return []  # turn-around

    #           recursion  |  break-down  |    build-up
    return reverse_list(to_reverse[1:]) + [to_reverse[0]]


# --- --- --- test cases --- --- ---

assert reverse_list([]) == [], "Test 1"
assert reverse_list([1, 2, 3]) == [3, 2, 1], "Test 2"
assert reverse_list([1, 2, 1]) == [1, 2, 1], "Test 3"
assert reverse_list(["", False, None, 0]) == [0, None, False, ""], "Test 4"