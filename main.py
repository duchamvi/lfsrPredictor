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


def predictLFSR(stream, nbBits):
    """Predicts next inputs from a stream and nbBits"""
    L, Creversed = berlekampMassey.BerlekampMasseyAlgorithm(stream)
    C = Creversed[::(-1)]   #reorder the polynom
    print("Linear Span : {}\nPolynom : {}".format(L, C))
    N = len(stream)
    state = stream[N-L:]    #reconstruction of the state of the LFSR
    predictions = []
    end = False
    print("Predictions (press q to stop, enter to continue)\nPrediction : ")

    # loop of value prediction
    while(not end):
        # find next bit 
        nextValue = 0
        for j in range(L): 
            nextValue ^= C[j] & state[j]
        state.append(nextValue)
        predictions.append(nextValue)
        state = state[1:]

        # if a full integer is constructed
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