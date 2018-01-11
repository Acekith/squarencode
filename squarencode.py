import sys
import argparse
from itertools import zip_longest


#alphabet defined
mydict = {
        "a" : ["|", "\\", "\\"],
        "b" : ["|", "\\", "|"],
        "c" : ["-", "|", "|"],
        "d" : ["|", "/", "|"],
        "e" : ["|", "/", "/"],
        "f" : ["-", "|", "\\"],
        "g" : [u"\u2022", "|", "\\"],
        "h" : [u"\u2022", "|", "-"],
        "i" : [u"\u2022", "|", "/"],
        "j" : ["-", "|", "/"],
        "k" : ["|", "-", "-"],
        "l" : [u"\u2022", "-", "\\"],
        "m" : [u"\u2022", u"\u2022", u"\u2022"],
        "n" : [u"\u2022", "-", "/"],
        "o" : ["-", "-", "|"],
        "p" : ["-", "/", "|"],
        "q" : [u"\u2022", "/", "|"],
        "r" : [u"\u2022", "-", "|"],
        "s" : [u"\u2022", "\\", "|"],
        "t" : ["-", "\\", "|"],
        "u" : ["/", "/", "|"],
        "v" : ["/", "|", "|"],
        "w" : ["|", "|", "-"],
        "x" : ["\\", "|", "|"],
        "y" : ["\\", "\\", "|"],
        "z" : ["\\", "\\", "\\"]
        }

#functions

def printalphabet():
    teststring = ''
    print("\n" + "***************************")
    print("*    PRINTING ALPHABET    *")
    print("***************************" + "\n")
    for key, value in sorted(mydict.items()):
        symbol = ''
        pair = ''
        for x in value:
            symbol += x
        pair = key + symbol
        teststring += pair + " "
    for x in zip_longest(*teststring.split(), fillvalue=' '):
        print(' '.join(x))


def encode(string):
    finalstring = ''
    stringlist = list(string.lower())

    print(stringlist)
    for x in stringlist:
        symbol = ''
        if x in mydict:
            #currentlist = mydict[x]
            for item in mydict[x]:
                symbol += item
            print(symbol)
            finalstring += symbol
        else:
            symbol = " "
            print(symbol)
            finalstring += symbol
    print("Final String Assembled")
    print("-----------------------")
    print(finalstring)
    return(finalstring)

def printformatted(string):
    toPrint = encode(string)
    print("\n" + "***************************")
    print("*    Formatted Output    *")
    print("***************************" + "\n")
    for x in zip_longest(*toPrint.split(), fillvalue=' '):
        print(' '.join(x))
        return(' '.join(x))
printformatted('Texas A&M Cyber SEcurity Club')
