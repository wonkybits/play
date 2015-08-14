__author__ = 'philstene'

import PlaintextToInteger


class ShiftCipher:

    input = ""

    def __init__(self, plaintext):
        self.input = plaintext

    def setInput(self, text):
        self.input = text

    def encrypt(self, shift):
        converter = PlaintextToInteger.PlaintextToInteger()
        temp = converter.ptToInt(self.input)

        for i in range(0, len(temp)):
            temp[i] = (temp[i] + shift) % 26
        return converter.intToPt(temp)

    def decrypt(self, shift):
        converter = PlaintextToInteger.PlaintextToInteger()
        temp = converter.ptToInt(self.input)

        for i in range(0, len(temp)):
            temp[i] = (temp[i] - shift) % 26

        return converter.intToPt(temp)

