import re
import itertools


# io
def read_lines(filepath):
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(line.strip())

    return lines


def flatten(iterable):
    return list(itertools.chain(*iterable))


# apply func to each elements of an iterable
def lmap(func, *iterable):
    return list(map(func, *iterable))


# return only elements of iterable where predicate from func is true
def lfilter(func, *iterable):
    return list(filter(func, *iterable))


# extract numbers
def get_ints(string):
    return lmap(int, re.findall(r"-?\d+", string))


def get_pos_ints(string):
    return lfilter(lambda x: x > 0, get_ints(string))


def get_neg_ints(string):
    return lfilter(lambda x: x < 0, get_ints(string))


def get_floats(string):
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", string))


def get_pos_floats(string):
    return lfilter(lambda x: x > 0.0, get_floats(string))


def get_neg_floats(string):
    return lfilter(lambda x: x < 0.0, get_floats(string))


def get_words(string):
    return re.findall(r"[aA-zA-Z]+", string)


# stuff
def binary_search(arr, val):
    low, high = 0, len(arr) - 1
    idx_found = None
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    return idx_found
