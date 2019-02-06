def bitToInt(bits):
    """Converts a list of bits into an integer"""
    n = 0
    for i in range (len(bits)):
        n+= bits[i]*(2**i)
    return n


def intToBits(n, length):
    """Converts an integer into a list of bits"""
    bits = []
    for i in range(length):
        bits.append(n%2)
        n = n//2
    return bits


def stringToInt(str_input):
    """Checks that the input string is an integer then converts it"""
    try:
        int_input = int(str_input)
    except:
        print("That's not a valid input, please enter an integer next time")
        exit(0)
    return int_input