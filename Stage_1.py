#Function to translate DNA to Protein 
def translate_dna(dna):
    codon_table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_', 'TGA': '_'
    }
    protein = "" #Create empty 
    for i in range(0, len(dna) - 2, 3): #index 0, step 3, -2 to ensure that the sequence is iterated correctly
        codon = dna[i:i+3] #codon is defined here 
        if codon in codon_table:
            if codon_table[codon] == "_":
                break
            protein += codon_table[codon]
    return protein

#Function to Simulate Logistic Growth Simulation
def logistic_growth(t, K, P0, r):
    return K / (1 + ((K - P0) / P0) * (2.71828 ** (-r * t)))

#Generating Growth Curves
def generate_growth_curves(n, time_range):
    data = []
    for i in range(n):
        K = 1000 + i * 10  # Simple variation instead of random values
        P0 = 10 + i  # Different starting populations
        r = 0.1 + (i * 0.001)  # Different growth rates
        times = list(range(time_range))
        populations = [logistic_growth(t, K, P0, r) for t in times]
        data.append((times, populations, i))
    return data

#Calculating time to reach 80% of Maximum Growth
def time_to_80_percent(K, P0, r):
    target = 0.8 * K
    time = 0
    while logistic_growth(time, K, P0, r) < target:
        time += 1
    return time

#Hamming Distance
def hamming_distance(str1, str2):
    length = max(len(str1), len(str2))
    str1 = str1.ljust(length) #ljust adds padding
    str2 = str2.ljust(length)
    distance = 0
    for i in range(length):
        if str1[i] != str2[i]:
            distance += 1
    return distance

# Examples
dna_seq = "ATGCGTACGTTAG"
print("Protein:", translate_dna(dna_seq))

growth_data = generate_growth_curves(5, 10)  # Generate 5 curves for simplicity
print("Sample Growth Data:")
for row in growth_data[:2]:
    print("Time:", row[0])
    print("Population:", row[1])

print("Time to 80% capacity:", time_to_80_percent(1000, 10, 0.1))

print("Hamming Distance:", hamming_distance("Oluwatobiloba", "@penemeritus"))
