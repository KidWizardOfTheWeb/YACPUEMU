import sys
from struct import pack, unpack

class CPUController:
    def __init__(self, v):
        pass

    def cycle(self):
        inputFile = open("output.dat", "rb") # The binary we must read, this is a test for now
        asmInstructionData = ""
        with open("output.dat", "rb") as inputFile:
            asmInstructionData = inputFile.read()
            pass
        tempHex = (int.from_bytes(asmInstructionData[0:4], "big"))  # reads first line from the file for now,
        # Include above in loop
        print(("{0:0>32b}".format(tempHex))) # Converts to readable binary, print for debug
        '''
        The cycle behavior flag essentially will tell the loop to run by stepping on the user's command,
        or automatically if set to 1 at the beginning
        '''
        cycleBehaviorFlag = -1
        while cycleBehaviorFlag != 0 or cycleBehaviorFlag != 1:
            cycleBehaviorFlag = input("Type 0 to step through the program or type 1 to run it all at once.")

        if cycleBehaviorFlag == 1:
            userStep = 1
        else:
            userStep = 0
        # If cycle behavior flag is not 0, it will run the whole program at once
        while (cycleBehaviorFlag != 0):
            if (cycleBehaviorFlag == 0 and userStep == 1):
                # Manual stepping here
                pass

            pass
        pass