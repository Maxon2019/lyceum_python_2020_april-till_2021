"""
The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the
two dimensions are different).

https://i.imgur.com/lk5vJ7sm.jpg

Can you translate this drawing into an algorithm?

You will be given two dimensions

1 a positive integer length (parameter named lng)
2 a positive integer width (parameter named wdth)
You will return an array or a string (depending on the language; Shell bash, PowerShell and Fortran return a string)
with the size of each of the squares.
"""


def sqInRect(lng, wdth):
    bill = True
    square_list = []
    if lng == wdth:
        return None
    else:
        while bill:
            if lng > wdth:
                print(f'- width {wdth}')
                square_list.append(wdth)
                lng -= wdth
            elif wdth > lng:
                print(f'- long {lng}')
                square_list.append(lng)
                wdth -= lng
            else:
                square_list.append(1)
                bill = False
    return square_list


if __name__ == '__main__':
    print(sqInRect(4, 5))