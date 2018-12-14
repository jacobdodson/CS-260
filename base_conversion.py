def re_convert(b10, base):
    ans = ""
    if b10 // base == 0:
        ans = str(b10)
    else:
        ans = re_convert(b10 // base, base) + str(b10 % base)
    return ans

def convert_10_to_base(b10, base):
    quo = b10
    out = ""

    while quo > 0:
        rem = quo % base
        quo = quo // base
        out = str(rem) + out

    return out


print(re_convert(6, 2))
