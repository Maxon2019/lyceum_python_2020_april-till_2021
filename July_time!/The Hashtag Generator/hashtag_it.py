"""The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false."""


def generate_hashtag(s):
    if s != '':
        s = s.title()
        s_list = s.split()
        s_list.insert(0, '#')
        if len(s) <= 140:
            return ''.join(s_list)
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(generate_hashtag('CodeWars is nice'))
