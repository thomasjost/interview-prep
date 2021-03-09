#!/usr/bin/env python3
def reverse(x):
    """
    The limitations put in place are −2,147,483,648 and 2,147,483,648 for a 32-bit
    integer. Converted to hex, these values are respectively listed below.
    """
    negative_limit = -0x80000000
    positive_limit = 0x7fffffff

    if x > 0:
        rev = int(str(x)[::-1])
        """
        By doing a bitwise AND, if the value of rev is within the limitation,
        it is returned. Otherwise, another value will be returned, breaking this
        condition.
        """
        if rev & positive_limit == rev:
            return rev
        else:
            return 0

    elif x < 0:
        rev = -int(str(abs(x))[::-1])
        if rev & negative_limit == negative_limit:
            return rev
        else:
            return 0

    else:
        return 0


print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))
