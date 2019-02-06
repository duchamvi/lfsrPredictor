#!/usr/bin/python3
import utils
import berlekampMassey

def stringToInt(str_input):
    try:
        int_input = int(str_input)
    except:
        print("That's not a valid input, please enter an integer next time")
        exit(0)
    return int_input

def getNbBits():
    str_nbBits = input("Enter the number of bits used to code each integer :")
    nbBits = stringToInt(str_nbBits)
    print(nbBits, "bits\n")
    return nbBits

def getInputList(nbBits):
    str_input = input("Enter the list of integer observed (ex: 48 56 94 12):")
    print(str_input)
    str_integerList = str_input.split()
    stream = []
    for i in str_integerList:
        stream+= utils.intToBits(stringToInt(i), nbBits)
    return stream

if __name__ == "__main__":
    nbBits = getNbBits()
    stream = getInputList(nbBits)
    print("Stream : {}". format(stream))