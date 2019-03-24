def speedParser(speed = '0k'):
    speed = speed.replace(',','.')
    x = 0
    num = str()
    for val in  speed:
        if val == 'k' or val == 'K':
            x *= 1
        elif val == 'm' or val == 'M':
            x *= 1024
        elif val == 'g' or val == 'G':
            x *= 1048576
        else:
            num += str(val)
            x = float(num)
    return int(x)


if __name__ == '__main__':
    print speedParser('1,5M')
