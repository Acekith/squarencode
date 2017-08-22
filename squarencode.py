import sys
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
    stringlist = list(string)

    print(stringlist)
    for x in stringlist:
        symbol = ''
        if x in mydict:
            symbol = mydict[x]
            print(x, symbol)
        else:
            symbol = " "
            print(symbol)

encode('test string do not encode')

printalphabet()
