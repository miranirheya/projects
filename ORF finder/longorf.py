from Bio import SeqIO


def find_longest_orf(seq):
    """
    Finds the longest Open Reading Frame (ORF) in a given DNA sequence.
    """
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    longest_orf = ""

    i = 0
    while i < len(seq) - 2:
        codon = seq[i:i + 3]

        if codon == start_codon:
            current_orf = codon
            i += 3

            while i < len(seq) - 2:
                codon = seq[i:i + 3]
                current_orf += codon

                if codon in stop_codons:
                    if len(current_orf) > len(longest_orf):
                        longest_orf = current_orf
                    break

                i += 3

        else:
            i += 3

    return longest_orf

#Example
seq = "ATGATTAATACCGTACATAACATTGCATGA"
longest_orf = find_longest_orf(seq)
print(longest_orf)