__author__ = 'philstene'

import sys
import ShiftCipher



while(True):
    print "\nWhat would you like to do?."
    choice = raw_input("Enter e for Encrypt or d for Decrypt, or x to Exit.\n")

    if choice == 'e':
        temp = ""
        ciphertext = ""
        shift = int(raw_input("\nEnter the shift, 1 to 26.\n"))
        inputPath = raw_input("\nEnter the file path containing the text you would like to encrypt.\n")
        try:
            inputFile = open(inputPath, 'r')
            lines = inputFile.readlines()
            for line in iter(lines):
                temp += line
            temp = temp.lower()
            inputFile.close()
            try:
                outputPath = raw_input("\nEnter the filename for the output.\n")
                plaintext = "".join(c for c in temp if c not in ('!', '.', ':', '?', '/', ',', ' '))
                print "plaintext = " + plaintext
                sc = ShiftCipher.ShiftCipher(plaintext)
                ciphertext = sc.encrypt(shift)
                ciphertext = ciphertext.upper()
                outputFile = open(outputPath, 'w')
                outputFile.write(ciphertext)
                outputFile.close()
                print "ciphertext = " + ciphertext
            except IOError:
                print "Could not open " + inputPath + "\n"
        except IOError:
            print "Could not open " + inputPath + "\n"

    elif choice == 'd':
        ciphertext = ""
        shift = int(raw_input("\nEnter the shift, 1 to 26.\n"))
        inputPath = raw_input("\nEnter the file path containing the text you would like to decrypt.\n")
        try:
            inputFile = open(inputPath, 'r')
            lines = inputFile.readlines()
            for line in iter(lines):
                ciphertext += line
            inputFile.close()
            try:
                outputPath = raw_input("\nEnter the filename for the output.\n")
                print "ciphertext = " + ciphertext
                ciphertext = ciphertext.lower()
                sc = ShiftCipher.ShiftCipher(ciphertext)
                plaintext = sc.decrypt(shift)
                outputFile = open(outputPath, 'w')
                outputFile.write(plaintext)
                outputFile.close()
                print "plaintext = " + plaintext
            except IOError:
                print "Could not open " + outputPath + " for output.\n"
        except IOError:
            print "Could not open " + inputPath + " for input.\n"
    else:
        break

sys.exit()
