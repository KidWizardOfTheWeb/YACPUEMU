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
		self.registerArr = arr = [("{0:08b}".format(0))] * 32 # all 31 registers, r0-r31. This inits blank values first.
		self.memArr = memArr # Emulate memory, somehow. Check the PDF I suppose?
		self.ALUCount = ALUCount # Count arithimetic operations (note: there are some beyond the obvious, ex. beq)
		self.readWriteCount = readWriteCount # num of reads (load) and writes (store). Might need to count them separately?
		self.instrCount = instrCount # write this value as an array instead with the size of the array as the
		# number of instructions we support for this project. We want to store a count for each instruction's usage. 
    '''