import sys
import os
from struct import pack, unpack


class CPUView:
    def __init__(self):
        self.PC = 0  # PC counter. Starts at 0x0.
        self.registerArr = [None] * 32  # all 31 registers, r0-r31. This code inits blank values first.
        self.memArr = []  # Emulate memory, somehow. Check the PDF I suppose?
        self.ALUCount = 0  # Count arithimetic operations (note: there are some beyond the obvious, ex. beq)
        self.readWriteCount = [0] * 2  # num of reads (load) and writes (store). Might need to count them separately?
        self.instrCount = [0] * 10  # write this value as an array instead with the size of the array as the
        # number of instructions we support for this project. We want to store a count for each instruction's usage. 
        self.cycles = 0  # number of cycles

    def incrementPC(self, instructionsMoved):  # increments the pc by however many instructions are moved (usually 1)
        self.PC += (4 * instructionsMoved)
        pass

    def editRegVal(self, regNum,
                   val):  # if a register changes, pass in both which register is changed and what its changed to
        self.registerArr[regNum] = val
        pass

    def incrementALUCount(self):  # done whenever an arthimetic operation is done
        self.ALUCount += 1
        pass

    def incrementReadOrWrite(self,
                             read):  # read should be a boolean, if the instruction reads from memory, then its true, if it writes, then its false
        if read:
            self.readWriteCount[0] += 1
        else:
            self.readWriteCount[1] += 1
        pass

    def incrementCycles(
            self):  # if this is called, it should reprint the scoreboard. should be called at the end of each clock cycle
        self.cycles += 1
        self.printScoreboard()
        pass

    def printScoreboard(self):  # called each clock cycle
        os.system(
            'cls' if os.name == 'nt' else 'clear')  # clears scoreboard so it can be updated, probably needs to be changed in some way

        print("Clock Cycles Completed: " + str(self.cycles))  # prints number of cycles done

        print("PC Value: " + hex(self.PC))  # prints PC value

        print("Register Vals: ")  # prints every register (should be in hex)
        for i in range(32):
            print("$" + str(i) + ": ", end='')
            if self.registerArr[i] is None:
                print("N/A")
            else:
                print(hex(self.registerArr[i]))

        print("ALU Operations: " + str(self.ALUCount))  # displays amount of operations using the ALU

        print("Memory Reads: " + str(self.readWriteCount[0]))  # displays amount of memory reads done

        print("Memory Writes: " + str(self.readWriteCount[1]))  # displays amount of memory writes done

        # memory should go here (not sure what memory entails)
        # logic block statistics should also go here (not sure what that means as well)
        pass

    def incrementInstrCount(self, instruction):  # might be needed in controller instead of view
        if instruction == "lw":  # first thing in array is amount of load words
            self.instrCount[0] += 1

        elif instruction == "sw":  # second thing in array is amount of store words
            self.instrCount[1] += 1

        elif instruction == "add":  # next thing in array is amount of adds
            self.instrCount[2] += 1

        elif instruction == "addi":  # next thing in array is amount of add immediates
            self.instrCount[3] += 1

        elif instruction == "sub":  # next thing in array is amount of subtracts
            self.instrCount[4] += 1

        elif instruction == "and":  # next thing in array is amount of logical ands
            self.instrCount[5] += 1

        elif instruction == "or":  # next thing in array is amount of logical ors
            self.instrCount[6] += 1

        elif instruction == "slt":  # next thing in array is amount of set if less thans
            self.instrCount[7] += 1

        elif instruction == "beq":  # next thing in array is amount of branch if equal tos
            self.instrCount[8] += 1

        else:  # last thing in array is amount jump instructions
            self.instrCount[9] += 1
        pass
