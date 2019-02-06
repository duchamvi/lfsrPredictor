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

def getStream(nbBits):
    str_input = input("Enter the list of integer observed (ex: 48 56 94 12):")
    print(str_input)
    str_integerList = str_input.split()
    stream = []
    for i in str_integerList:
        stream+= utils.intToBits(stringToInt(i), nbBits)
    print("Stream : {}". format(stream))
    return stream

def predictLFSR(stream, nbBits):
    L, C = berlekampMassey.BerlekampMasseyAlgorithm(stream)
    N = len(stream)
    state = stream[N-L:]
    predictions = []
    end = False
    print("Predictions (press q to stop, enter to continue)\n")

    while(not end):
        nextValue = 0
        for j in range(L): 
            nextValue ^= C[j] & state[j]
        state.append(nextValue)
        predictions.append(nextValue)
        state = state[1:]

        if len(predictions) == nbBits:
            print("Prediction : {}".format(utils.bitToInt(predictions)))
            predictions = []
            key = input()
            if key == "q" or key == "Q":
                end = True


if __name__ == "__main__":
    nbBits = getNbBits()
    stream = getStream(nbBits)
    predictLFSR(stream, nbBits)