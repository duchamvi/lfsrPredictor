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
    print("First, the number of bits used to code each integer is required. Enter 1 for a bitstream")
    str_nbBits = input("Number of bits : ")
    nbBits = stringToInt(str_nbBits)
    return nbBits

def getStream(nbBits):
    print("Then, enter the list integers produced by the LFSR (ex: 10 14 3 8)")
    str_input = input("List of integers : ")
    str_integerList = str_input.split()
    stream = []
    for i in str_integerList:
        stream+= utils.intToBits(stringToInt(i), nbBits)
    print("Stream : {}". format(stream))
    return stream

def predictLFSR(stream, nbBits):
    L, Creversed = berlekampMassey.BerlekampMasseyAlgorithm(stream)
    C = Creversed[::(-1)]
    print("Linear Span : {}\nPolynom : {}".format(L, C))
    N = len(stream)
    state = stream[N-L:]
    predictions = []
    end = False
    print("Predictions (press q to stop, enter to continue)\nPrediction : ")

    while(not end):
        nextValue = 0
        for j in range(L): 
            nextValue ^= C[j] & state[j]
        state.append(nextValue)
        predictions.append(nextValue)
        state = state[1:]

        if len(predictions) == nbBits:
            print(" >> {}  ".format(utils.bitToInt(predictions)), end ="", flush = True)
            predictions = []
            key = input()
            if key == "q" or key == "Q":
                end = True


if __name__ == "__main__":
    print("LFSR Predictor - Berlekamp-Massey Algorithm\n")
    nbBits = getNbBits()
    stream = getStream(nbBits)
    predictLFSR(stream, nbBits)