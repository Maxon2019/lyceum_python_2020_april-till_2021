def longest(s1, s2):
    s_all = set(s1 + s2)
    s_all = ''.join(sorted((' '.join(s_all)).split(' ')))
    return s_all


if __name__ == "__main__":
    print(longest("aretheyhere", "yestheyarehere"))
    # лучшее : return "".join(sorted(set(a1 + a2)))
