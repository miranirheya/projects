def extract_exons(input_file, output_file, exon_positions):
    with open(input_file, 'r') as wt:
        hdr = wt.readlines()
        result = ""
        for line in hdr:
            str = ""
            seq = str.join(line.split())
            result += seq
    extracted_exons = []
    for start, end in exon_positions:
        extracted_exons.append(result[start:end])
    result = "".join(extracted_exons)

    with open(output_file, 'w') as mt:
        mt.write(result)

    print(len(result))
    print(result)


# Example usage
input_filename = "krmod_82.txt"
output_filename = "krmod_test.txt"
exon_positions = [(5545, 5656), (23517, 23696), (25156, 25316), (41018, 41135)]

extract_exons(input_filename, output_filename, exon_positions)