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

def printPolynom(polynom):
    chaine =""
    indice = len(polynom)
    for i in polynom:
        indice -=1
        if i:
            if chaine != "":
                chaine += " + "

            if indice == 0:
                chaine+= "1"
            else:
                chaine+= "X^{}".format(indice)
    print(colorama.Fore.GREEN + chaine + colorama.Fore.WHITE)
    print("Use this polynom to find the next output of the LFSR.")



def getPolynom(stream):
    print("Berlekamp-Massey Algorithm :")
    span, polynom = berlekampMassey.BerlekampMasseyAlgorithm(stream)
    return span, polynom


def tuto():
    print(colorama.Fore.GREEN + "\nLFSR Predictor\n" + colorama.Fore.WHITE)
    nbBits = getNbBits()
    input(colorama.Style.DIM + "\nPress enter to continue\n" + colorama.Style.NORMAL)
    stream = getStream(nbBits)
    input(colorama.Style.DIM + "\nPress enter to continue\n" + colorama.Style.NORMAL)
    span, polynom = getPolynom(stream)
    printPolynom(polynom)

tuto()