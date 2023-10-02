def reverse_complement_dna(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp_seq = ''.join(complement[base] for base in reversed(dna_sequence))
    return reverse_comp_seq

def translate_mrna_to_amino_acids(mrna_sequence):
    # Define the genetic code (codon to amino acid mapping)
    genetic_code = {
        "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine",
        "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine",
        "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine", "AUG": "Methionine",
        "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine",
        "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
        "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
        "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
        "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
        "UAU": "Tyrosine", "UAC": "Tyrosine", "UAA": "Stop", "UAG": "Stop",
        "CAU": "Histidine", "CAC": "Histidine", "CAA": "Glutamine", "CAG": "Glutamine",
        "AAU": "Asparagine", "AAC": "Asparagine", "AAA": "Lysine", "AAG": "Lysine",
        "GAU": "Aspartic acid", "GAC": "Aspartic acid", "GAA": "Glutamic acid", "GAG": "Glutamic acid",
        "UGU": "Cysteine", "UGC": "Cysteine", "UGA": "Stop", "UGG": "Tryptophan",
        "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",
    }
    
    protein_sequence = []
    
    # Split the mRNA sequence into codons (3 bases at a time)
    codons = [mrna_sequence[i:i+3] for i in range(0, len(mrna_sequence), 3)]
    
    # Translate each codon into an amino acid
    for codon in codons:
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            if amino_acid == "Stop":
                break  # Stop translation at a stop codon
            protein_sequence.append(amino_acid)
        else:
            protein_sequence.append("Unknown")  # Unknown codon
    
    return " ".join(protein_sequence)

# Input DNA sequence
dna_sequence = "TTACGA"

# Compute the reverse complement of DNA
reverse_complement_sequence = reverse_complement_dna(dna_sequence)
print("Reverse Complement:", reverse_complement_sequence)

# Convert DNA to mRNA (using 'U' instead of 'T')
mrna_sequence = dna_sequence.replace('T', 'U')
print("mRNA Sequence:", mrna_sequence)

# Translate mRNA to amino acids
amino_acid_sequence = translate_mrna_to_amino_acids(mrna_sequence)
print("Amino Acid Sequence:", amino_acid_sequence)
