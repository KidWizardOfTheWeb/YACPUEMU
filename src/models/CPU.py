import sys
from struct import pack, unpack

class Instruction:
    def __init__(self, binary):
        self.opcode = '{0:032b}'.format(binary)[0:6] # Retrieves first 6 bits of the instruction
        # Now we find the opcode and instruction
        # In each case, initialize registers and immediate fields accordingly.
        # That is to say, in each case, init whatever is needed directly in there. Up to 3 total parameters usually.
        match self.opcode:
            case 0:
                # SPECIAL. Only operates with registers, no immediates.
                # add, sub, and, or, slt
                # The opcode starts with 0, but the final 6 bits are the actual instruction
                reg1 = '{0:032b}'.format(binary)[6:11]
                reg2 = '{0:032b}'.format(binary)[11:16]
                storeReg = '{0:032b}'.format(binary)[16:21]
                # [21:26] is always padded with 5 zeroes (00000)
                instruction = '{0:032b}'.format(binary)[26:32]
                pass
            case 2:
                # Jump
                pass
            case 3:
                # Jump and link. We really should not end up here.
                pass
            case _:
                # Everything greater than 3 goes here.
                # Lw, Sw, beq, addi
                # First 6 bits are the actual instruction
                instruction = self.opcode
                pass
        self.instruction = instruction

        # Find instruction name. This is just for easier operation later
        match instruction:
            case _:
                pass


        pass