codeList = {".----": "1", ".-": "a"}
def decodeMorse(morseCode):
    try:
        print(codeList[morseCode])
    except KeyError:
        print("")
decodeMorse(input("please enter string"))
