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
                # Call to view layer here, asks user if they want to step. Only do this call if cycleBehaviorFlag != 1
                userStep = 0 # reset state to stop incrementation, unused if cycleBehaviorFlag == 1

                # construct model object here with instruction info. The init func should determine the fields filled.

                # Check what the instruction does, perform it.
                # This means register values will be adjusted according to instruction behavior.
                # Add these new values to the view object's register array to the right index.
                # If this instruction is arithmetic, increase view object's ALUCount.
                # If this instruction is a read (load) or write (store), increase view object's read/write count
                # Update memory... somehow (the specifications weren't clear)

                # Increment PC when all is said and done and loop for next instruction in binary array.

                pass
            else:
                stepCheck = input("Step? 1 to step, 0 to force stop.")
                if stepCheck == 1:
                    userStep = 1
                else:
                    userStep = 0
                pass
            pass