import sys
from struct import pack, unpack

class Instruction:
    def __init__(self, binary):
        self.opcode = '{0:032b}'.format(binary)[0:6] # Retrieves first 6 bits of the instruction
        # Now we find the opcode and instruction
        # In each case, initialize registers and immediate fields accordingly.
        # That is to say, in each case, init whatever is needed directly in there. Up to 3 total parameters usually.
        match int(self.opcode):
            case 0:
                # R(egister)-Type. SPECIAL. Only operates with registers, no immediates.
                # add, sub, and, or, slt
                # The opcode starts with 0, but the final 6 bits are the actual instruction
                self.reg1 = '{0:032b}'.format(binary)[6:11]
                self.reg2 = '{0:032b}'.format(binary)[11:16]
                self.storeReg = '{0:032b}'.format(binary)[16:21]
                # [21:26] is always padded with 5 zeroes (00000)
                instruction = '{0:032b}'.format(binary)[26:32]
                pass
            case 2:
                # J(ump)-type. Jump
                instruction = self.opcode
                self.offImmVal = '{0:032b}'.format(binary)[6:32]  # 26-bit offset/immediate value
                pass
            case 3:
                # J(ump)-type. Jump and link. We really should not end up here.
                instruction = self.opcode
                self.offImmVal = '{0:032b}'.format(binary)[6:32]  # 26-bit offset/immediate value
                pass
            case _:
                # I(mmediate)-Type. Everything greater than 3 goes here.
                # Lw, Sw, beq, addi
                # First 6 bits are the actual instruction
                instruction = self.opcode
                self.reg1 = '{0:032b}'.format(binary)[6:11]
                self.reg2 = '{0:032b}'.format(binary)[11:16]
                self.offImmVal = '{0:032b}'.format(binary)[16:32] # 16-bit offset/immediate value
                pass
        self.instruction = instruction

        # Find instruction name. This is just for easier operation later
        match instruction:
            case '100000':
                # add
                self.instrName = 'add'
                pass
            case '100010':
                # sub
                self.instrName = 'sub'
                pass
            case '100100':
                # and
                self.instrName = 'and'
                pass
            case '100101':
                # or
                self.instrName = 'or'
                pass
            case '101010':
                # slt
                self.instrName = 'slt'
                pass
            case '000100':
                # beq
                self.instrName = 'beq'
                pass
            case '100011':
                # lw
                self.instrName = 'lw'
                pass
            case '101011':
                # sw
                self.instrName = 'sw'
                pass
            case '001000':
                # addi
                self.instrName = 'addi'
                pass
            case '000010':
                # jump
                self.instrName = 'jump'
                pass
            case _:
                pass


        pass