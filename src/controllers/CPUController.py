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

        binaryFinalArr = []
        for i in range(int(len(asmInstructionData) / 4)):
            binaryFinalArr.append(int.from_bytes(asmInstructionData[i*4:(i*4)+4], "big")) # reads FULL LINE as binary
            print(("{0:0>32b}".format(binaryFinalArr[i]))) # Converts to readable binary, print for debug
            pass

        # The cycle behavior flag essentially will tell the loop to run by stepping on the user's command,
        # or automatically if set to 1 at the beginning

        cycleBehaviorFlag = -1
        while cycleBehaviorFlag != 0 or cycleBehaviorFlag != 1:
            cycleBehaviorFlag = input("Type 0 to step through the program or type 1 to run it all at once.")

        if cycleBehaviorFlag == 1:
            userStep = 1
        else:
            userStep = 0
        # If cycle behavior flag is not 0, it will run the whole program at once

        for i in range(len(binaryFinalArr)):
            if ((cycleBehaviorFlag == 0 and userStep == 1) or (cycleBehaviorFlag == 1)):
                # Manual stepping here, will only run if userStep is set to state 1 or if behavior flag is 1

                userStep = 0 # reset state to stop incrementation

                # construct model object. The init should determine the fields filled out

                pass
            else:
                stepCheck = input("Step? 1 to step, 0 to force stop.")
                if stepCheck == 1:
                    userStep = 1
                else:
                    userStep = 0
                pass
            pass