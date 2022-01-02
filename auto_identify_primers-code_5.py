"""
Assignment 5: Automatic Primer Identification

In this assignment, you will practice using python's subprocess library, the pyfasta library, and the primer3
command-line-interface to automatically identify primers. This template provides a potential route to a completed
script, but the implementation details are entirely up to you. The checker script, as you will see, does little more
than confirm that your script prints the correct primers to the console for a handful of argument combinations.
"""

import argparse
import subprocess
from pyfasta import Fasta

"""
If you have not already, install pyfasta and primer3 into the current environment using the following commands:
conda install -c bioconda primer3
conda install -c bioconda pyfasta
"""

"""
Create your parser and arguments. Your script should expect three positional arguments: First, the name of a
fasta file, second, the chromosome you want to amplify, and third, the position you want amplified. Enforce that
the first two arguments are of type str, and the third is of type int.
"""

# your code here
parser = argparse.ArgumentParser(description = 'This is assignment 5')
args = parser.add_argument('--fasta_file', type=str,help='Enter a genome file containing DNA sequence')
args = parser.add_argument('--chromosome', type=str, help='Enter the chromosome you want amplified')
args = parser.add_argument('--position', type=int, help='Enter the position you want amplified')   
args = parser.parse_args()

"""
Open the fasta file and read in the entirety of the sequence. You can use whatever data structure you prefer.
"""

# your code here
file = open(f"{args.fasta_file}","r+")
data = file.read()
"""
Identify the sequence 500 bp upstream and downstream of the requested position and store it as a string.
"""

# your code here
for x in range(len(data)):
    if data[x:x+len(args.chromosome)] == args.chromosome:
        for y in range(len(data[x+1:])):
            if data[x+y+1] == '>':
                break
        # something
        break

dat = "".join(data[x+len(args.chromosome):x+len(args.chromosome)+y].split())
value = dat[args.position-500:args.position+500]
"""
Add braces to the DNA sequence 100 bp upstream and downstream of the requested position. Alternatively, you can use 
an argument in the input file to specify this
"""

# your code here
# NOTE :- skipping this part as not required

"""
Create an input file containing the DNA sequence and specify a product length of 600 - 800 base pairs
"""

# your code here
file_data = f'SEQUENCE_ID=example\nSEQUENCE_TEMPLATE={value}\nPRIMER_PRODUCT_SIZE_RANGE=600-800\n='
file2 = open(r"primer_data.txt","w+")
file2.write(f"{file_data}")
file2.close()
"""   
Execute the primer3_core command on the input file you created.
"""

# your code here
output = subprocess.run(['primer3_core','primer_data.txt'], capture_output = True, encoding = 'utf-8')
file3 = open(r"primer_output.txt","w+")
file3.write(f"{output.stdout}")
file3.close()

""" 
Read in and parse the output to identify the sequence of best two primers. Print these out to the user
"""

# your code here
p1 = subprocess.Popen(['cat','primer_output.txt'], stdout = subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'PRIMER_LEFT_0_SEQUENCE'], stdin = p1.stdout, stdout = subprocess.PIPE)
p1 = subprocess.Popen(['cat','primer_output.txt'], stdout = subprocess.PIPE)
p3 = subprocess.Popen(['grep', 'PRIMER_RIGHT_0_SEQUENCE'], stdin = p1.stdout, stdout = subprocess.PIPE)
output2 = p2.communicate()
output3 = p3.communicate()
val1 = str(output2[0]).split('=')[1].split('\\')[0] 
#print(output3)
val2 = str(output3[0]).split('=')[1].split('\\')[0] 
print(val1+'\n'+val2)