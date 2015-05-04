__author__ = 'swaribrus'

import itertools

def num2base(num, length, alphabet):
    if num == 0:
        return [x for x in itertools.repeat(alphabet[0], length)]

    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num //= base
        arr.append(alphabet[rem])
    arr.reverse()
    if len(arr) < length:
        buf = [x for x in itertools.repeat(alphabet[0], length - len(arr))]
        buf.extend(arr)
        return buf

    return arr
