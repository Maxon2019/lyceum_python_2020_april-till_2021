def filter_list(l):
    """return a new list with the strings filtered out"""

    return [i for i in l if not isinstance(i, str)]


if __name__ == "__main__":
    print(filter_list([1, 'w', 123, '1234', 44562]))
