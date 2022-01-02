import argparse

#import warnings
#warnings.filterwarnings("ignore")

def valid_DNA_sequence(DNA):
    # This function takes in a string containing possible DNA sequence and returns True if all nucleotides are valid (A,a,C,c,G,g,T,t) and False if any nucleotide is invalid
    y = True
    for x in DNA:
        if x in ['A','a','C','c','G','g','T','t']:
            y = True
        else:
            y = False
            break
    return y

def print_DNA_sequence(DNA, mode):
    #print("a")
    # This function takes in a string containing valid DNA sequence and a mode that specifies the output format. Prints info to a screen, maximum characters per line
    for i in range(0,3):
        #This loop is used to create the three possible frames on the forward strand
        seq = DNA[i:]
        q = len(seq)//3
        DNA_sequence = seq[0:q*3] # Create DNA sequence for current frame. Ensure it is divisible by 3
        translated_sequence = translate(DNA_sequence, mode)
        # Print out direction (5' to 3') and frame to screen
        print(f"\n5' to 3' Frame: {i}")
        # Print out translated_sequence. If nucleotide sequence mode selected, print nucleotide sequence and amino acid sequence, 60 nucleotides per line until entire sequence is printed out
        if mode == "COMPACT":
            print(translated_sequence,"\n")
        elif mode == "VERBOSE":
            print(translated_sequence,"\n") 
        else:
            if len(DNA_sequence)>60:
                for j in range(0,int(len(DNA_sequence)//60)):
                    print(DNA_sequence[j*60:j*60+60])
                    print(translated_sequence[j*60:j*60+60])
            else:
                print(DNA_sequence)
                print(translated_sequence)

    rev_DNA_sequence = reverse_complement(DNA)
    for i in range(0,3):
        #This loop is used to create the three possible frames on the forward strand
        seq = rev_DNA_sequence[i:]
        q = len(seq)//3
        DNA_sequence = seq[0:q*3] # Create DNA sequence for current frame. Ensure it is divisible by 3
        translated_sequence = translate(DNA_sequence, mode)
        # Print out direction (5' to 3') and frame to screen
        print(f"\n3' to 5' Frame: {i}")
        # Print out translated_sequence. If nucleotide sequence mode selected, print nucleotide sequence and amino acid sequence, 60 nucleotides per line until entire sequence is printed out
        if mode == "COMPACT":
            print(translated_sequence,"\n")
        elif mode == "VERBOSE":
            print(translated_sequence,"\n") 
        else:
            if len(DNA_sequence)>60:
                for j in range(0,int(len(DNA_sequence)//60)):
                    print(DNA_sequence[j*60:j*60+60])
                    print(translated_sequence[j*60:j*60+60])
            else:
                print(DNA_sequence)
                print(translated_sequence)

def translate(DNA_sequence, mode):
    # Create dictionaries that translate codons into amino acids of appropriate format
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'-', 'TAG':'-',
    'TGC':'C', 'TGT':'C', 'TGA':'-', 'TGG':'W',
    }

    # Loop through DNA sequence codons
    out_seq = ''
    for i in range(0, int(len(DNA_sequence)/3)):
        out_seq += codontable[DNA_sequence[i*3:i*3+3]]

    # If VERBOSE, modify the start and stop codons and modify all codons to add space after
    if mode == "VERBOSE":
        out_seq = " ".join(out_seq)
        out_seq = out_seq.replace("M", "Met")
        out_seq = out_seq.replace("-", "Stop") 
    elif mode == "DNA":
        out_seq = " "+"  ".join(out_seq)+" "

    # If DNA, modify all codons to add space before and after
    

    return out_seq

def reverse_complement(DNA_sequence):
    # Returns string containing reverse complement of DNA sequence
    DNA_sequence = DNA_sequence[::-1]
    seq = ""
    for i in DNA_sequence:
        if i == "A":
            seq+="T"
        elif i == "T":
            seq+="A"
        elif i == "G":
            seq+="C"
        else:
            seq+="G"
    return seq
    
# Part I: Determine if the user has entered the appropriate number of argments when they called the script (one). Determine if the user entered one of three valid options for the mode. If there is an error in either of these, print out informative error messages indicating which error was made, what the three valid options are, and then quit the program.

# Part II: Create loop to query user for DNA sequence

# Part III: Determine if user wants to exit program

# Part IV: Determine if user input is valid DNA sequence. If DNA sequence is not valid, print error message and allow user to enter new DNA sequence. 

# Part V: Print out 6 translated frames to the screen in appropriate format
parser = argparse.ArgumentParser(description = 'This is a sample program')
try:
    args = parser.add_argument('mode', type=str, help='Mode can be one of the following options: \n\tCOMPACT \n\tVERBOSE \n\tDNA')
#print(args)
    args = parser.parse_args()
except:
    print("Invalid number of options\n")
    print("Usage: python3 Assignment2_solution.py <mode>\n")
    print("Mode can be one of the following options:\n\tCOMPACT\n\tVERBOSE\n\tDNA")
    quit()
#print(args)

if args.mode is None:
    print("Invalid number of options\n")
    print("Usage: python3 Assignment2_solution.py <mode>\n")
    print("Mode can be one of the following options:\n\tCOMPACT\n\tVERBOSE\n\tDNA")
    quit()
elif args.mode.upper() not in ['COMPACT','VERBOSE','DNA']:
    print(f"{args.mode} not a valid option\n")
    print("Usage: python3 Assignment2_solution.py <mode>\n")
    print("Mode can be one of the following options:\n\tCOMPACT\n\tVERBOSE\n\tDNA")
    quit()
else:
    z = True
    while z:
        DNA = input("Enter DNA sequence (or Exit to quit the program): ")
        if DNA.upper() == "EXIT":
            quit()
        else:
            val = valid_DNA_sequence(DNA)

        if val:
            # do something
            print(DNA)
            print(args.mode.upper())
            print_DNA_sequence(DNA, args.mode.upper())
        else:
            print("Invalid DNA sequence. Characters must be one of A, a, C, c, G, g, T, or t")
        