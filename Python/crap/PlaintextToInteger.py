__author__ = 'philstene'


class PlaintextToInteger:

    def ptToInt(self, plaintext):
        output = []

        for i in range(0, len(plaintext)):
            if plaintext[i] == 'a':
                output.append(0)
            elif plaintext[i] == 'b':
                output.append(1)
            elif plaintext[i] == 'c':
                output.append(2)
            elif plaintext[i] == 'd':
                output.append(3)
            elif plaintext[i] == 'e':
                output.append(4)
            elif plaintext[i] == 'f':
                output.append(5)
            elif plaintext[i] == 'g':
                output.append(6)
            elif plaintext[i] == 'h':
                output.append(7)
            elif plaintext[i] == 'i':
                output.append(8)
            elif plaintext[i] == 'j':
                output.append(9)
            elif plaintext[i] == 'k':
                output.append(10)
            elif plaintext[i] == 'l':
                output.append(11)
            elif plaintext[i] == 'm':
                output.append(12)
            elif plaintext[i] == 'n':
                output.append(13)
            elif plaintext[i] == 'o':
                output.append(14)
            elif plaintext[i] == 'p':
                output.append(15)
            elif plaintext[i] == 'q':
                output.append(16)
            elif plaintext[i] == 'r':
                output.append(17)
            elif plaintext[i] == 's':
                output.append(18)
            elif plaintext[i] == 't':
                output.append(19)
            elif plaintext[i] == 'u':
                output.append(20)
            elif plaintext[i] == 'v':
                output.append(21)
            elif plaintext[i] == 'w':
                output.append(22)
            elif plaintext[i] == 'x':
                output.append(23)
            elif plaintext[i] == 'y':
                output.append(24)
            elif plaintext[i] == 'z':
                output.append(25)
        return output

    def intToPt(self, intArr):
        output = ""

        for i in range(0, len(intArr)):
            if intArr[i] == 0:
                output += "a"
            elif intArr[i] == 1:
                output += "b"
            elif intArr[i] == 2:
                output += "c"
            elif intArr[i] == 3:
                output += "d"
            elif intArr[i] == 4:
                output += "e"
            elif intArr[i] == 5:
                output += "f"
            elif intArr[i] == 6:
                output += "g"
            elif intArr[i] == 7:
                output += "h"
            elif intArr[i] == 8:
                output += "i"
            elif intArr[i] == 9:
                output += "j"
            elif intArr[i] == 10:
                output += "k"
            elif intArr[i] == 11:
                output += "l"
            elif intArr[i] == 12:
                output += "m"
            elif intArr[i] == 13:
                output += "n"
            elif intArr[i] == 14:
                output += "o"
            elif intArr[i] == 15:
                output += "p"
            elif intArr[i] == 16:
                output += "q"
            elif intArr[i] == 17:
                output += "r"
            elif intArr[i] == 18:
                output += "s"
            elif intArr[i] == 19:
                output += "t"
            elif intArr[i] == 20:
                output += "u"
            elif intArr[i] == 21:
                output += "v"
            elif intArr[i] == 22:
                output += "w"
            elif intArr[i] == 23:
                output += "x"
            elif intArr[i] == 24:
                output += "y"
            elif intArr[i] == 25:
                output += "z"
        return output