#!/usr/bin/python3
import utils
import berlekampMassey


def getNbBits():
    """Asks the user to enter nbBits"""
    print("First, the number of bits used to code each integer is required. Enter 1 for a bitstream")
    str_nbBits = input("Number of bits : ")
    nbBits = utils.stringToInt(str_nbBits)
    return nbBits


def getStream(nbBits):
    """Asks the user to enter the stream"""
    print("Then, enter the list integers produced by the LFSR (ex: 10 14 3 8)")
    
    # get the list of integers
    str_input = input("List of integers : ")
    str_integerList = str_input.split()
    
    # conversion into a bitstream
    stream = []     
    for i in str_integerList:
        stream+= utils.intToBits(utils.stringToInt(i), nbBits)
    print("Stream : {}". format(stream))
    return stream

def getPolynom(stream):
    print("Berlekamp-Massey Algorithm :")
    span, Preversed = berlekampMassey.BerlekampMasseyAlgorithm(stream)
    polynom = Preversed[::(-1)]   #reorder the polynom
    print("\tLinear Span = {}\n\tPolynom = {}".format(span, polynom))
    return span, polynom

def predictLFSR(stream, nbBits, span, polynom):
    """Predicts next inputs from a stream and nbBits"""
    
    N = len(stream)
    state = stream[N-span:]    #reconstruction of the state of the LFSR
    predictions = []
    end = False
    print("Predictions (press q to stop, enter to continue)\nPrediction : ")

    # loop of value prediction
    while(not end):
        # find next bit 
        nextValue = 0
        for j in range(span): 
            nextValue ^= polynom[j] & state[j]
        state.append(nextValue)
        predictions.append(nextValue)
        state = state[1:]

        # if a full integer is constructed
        if len(predictions) == nbBits:
            print("{} >> {}  ".format(predictions, utils.bitToInt(predictions)), end ="", flush = True)
            predictions = []
            key = input()
            if key == "q" or key == "Q":
                end = True


if __name__ == "__main__":
    print("LFSR Predictor - Berlekamp-Massey Algorithm\n")
    nbBits = getNbBits()
    input("\nPress enter to continue\n")
    stream = getStream(nbBits)
    input("\nPress enter to continue\n")
    span, polynom = getPolynom(stream)
    input("\nPress enter to continue\n")
    predictLFSR(stream, nbBits, span, polynom)