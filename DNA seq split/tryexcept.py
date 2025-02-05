import sys

DNA = "CTAGCTAGGCGAGCTACGAGAGCTAGCGAGACATCGATCAGTACGATCGACTCGACTAGCTACGACTACGATCAGCTACGATC"
f = open("dna.txt", 'w')
f.write(DNA)

# check for valid filename
try:
    input_file = input('enter filename:\n')
    f = open(input_file)
    contents = f.read()
    print(contents)
except:
    sys.exit('not a valid filename')

# check for valid number
try:
    pieces = input('enter number of pieces:\n')
    pieces = int(pieces)
except:
    sys.exit('not a valid number')

# check that number is not zero or negative
try:
    f = open(input_file)
    dna = f.read().rstrip("\n")
    pieces = int(pieces)
    if pieces <= 0:
        sys.exit('number of pieces must be greater than zero')
    else:
        piece_length = int(len(dna) / pieces)
        print('piece length is ' + str(piece_length))
        for start in range(0, len(dna) - piece_length + 1, piece_length):
            print(dna[start:start + piece_length])

finally:
    f.close()