import sys
from struct import pack, unpack

class CPUController:
    def __init__(self, v):
        pass

    def cycle(self):
        inputFile = open(sys.argv[1], "r") # The binary we must read

        '''
        The cycle behavior flag essentially will tell the loop to run by stepping on the user's command,
        or automatically if set to 1 at the beginning
        '''
        cycleBehaviorFlag = -1
        while cycleBehaviorFlag is not 0 or cycleBehaviorFlag is not 1:
            cycleBehaviorFlag = input("Type 0 to step through the program or type 1 to run it all at once.")

        if cycleBehaviorFlag is 1:
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