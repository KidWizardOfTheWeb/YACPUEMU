import sys
from struct import pack, unpack

class CPUView:
    def __init__(self):
        self.opcode = []
        pass

    def setController(self, c):
        controller = c
        pass

    '''
    class CPUView:
	def __init__(self):
		self.PC = PC # PC counter. Starts at 0x0.
		self.registerArr = [31] # all 31 registers, r0-r31
		self.memArr = memArr # Emulate memory, somehow.
		self.ALUCount = ALUCount # Count arithimetic operations (note: there are some beyond the obvious, ex. beq)
		self.readWriteCount = readWriteCount # num of reads (load byte/half/word) and writes
		self.instrCount = instrCount # write this value as an array instead with the size of the array as the
		# number of instructions we support for this project. We want to store a count for each instruction's usage. 
    '''