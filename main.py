#!/usr/bin/python3
import utils
import berlekampMassey
import colorama


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
    print(colorama.Fore.GREEN + "Stream = {}". format(stream) + colorama.Fore.WHITE)
    return stream

def getPolynom(stream):
    print("Berlekamp-Massey Algorithm :")
    span, polynom = berlekampMassey.BerlekampMasseyAlgorithm(stream)
    print(colorama.Fore.GREEN + "Linear Span = {}\nPolynom = {}".format(span, polynom) + colorama.Fore.WHITE)
    return span, polynom

def predictLFSR(stream, nbBits, span, polynom):
    """Predicts next inputs from a stream and nbBits"""
    
    N = len(stream)
    state = (stream[N-span:])[::-1]    #reconstruction of the state of the LFSR
    predictions = []
    end = False
    print("Predictions (press q to stop, enter to continue)\nPrediction : "+ colorama.Fore.GREEN)

    # loop of value prediction
    while(not end):
        # find next bit 
        nextValue = 0
        for j in range(span): 
            nextValue ^= polynom[j+1] & state[j]
        state =  [nextValue] + state
        predictions.append(nextValue)
        state = state[:-1]

        # if a full integer is constructed
        if len(predictions) == nbBits:
            print("{} >> {}  ".format(predictions, utils.bitToInt(predictions)), end ="", flush = True)
            predictions = []
            key = input()
            if key == "q" or key == "Q":
                end = True


if __name__ == "__main__":
    print(colorama.Fore.GREEN + "\nLFSR Predictor\n" + colorama.Fore.WHITE)
    nbBits = getNbBits()
    input(colorama.Style.DIM + "\nPress enter to continue\n" + colorama.Style.NORMAL)
    stream = getStream(nbBits)
    input(colorama.Style.DIM + "\nPress enter to continue\n" + colorama.Style.NORMAL)
    span, polynom = getPolynom(stream)
    input(colorama.Style.DIM + "\nPress enter to continue\n" + colorama.Style.NORMAL)
    predictLFSR(stream, nbBits, span, polynom)