def validate_dna(dna_seq):
    #convert DNA to uppercase
    seqm = dna_seq.upper()
    print(seqm)
    print(len(seqm))

    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + seqm.count("T")

    if valid == len(seqm):
        print("Valid sequences")
        return True
    else:
        print("Invlaid sequences")
        return False

def frequency(seq):
    dic = {}
    for s in seq.upper():
        if s in dic: 
            dic[s] += 1
        else:
            dic[s] = 1
    print(dic)


def frequency_percentage(seq):
    seq = seq.upper()
    total_length = len(seq)
    
    if total_length == 0:
        return
    
    nucleotides = ['A', 'C', 'G', 'T']
    
    for n in nucleotides:
        count = seq.count(n)
        percentage = (count / total_length) * 100.0
        print(f"{n}: {percentage:.2f}%")


#function calling
DNA = "attagagatc"
validate_dna(DNA)
frequency(DNA)
frequency_percentage(DNA)