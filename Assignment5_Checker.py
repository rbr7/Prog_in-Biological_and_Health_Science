"""
This script is meant to help you check your final output against the expected output. You may need to tweak the
script_path variable, depending on the name of your solution script, but should otherwise be able to run this checker
without modification.
"""

import subprocess

script_path = './Assignment5_Solution.py'
fasta_file = 'c_elegans.WS220.genomic.fa'
chromosomes = ['CHROMOSOME_I', 'CHROMOSOME_V', 'CHROMOSOME_V', 'CHROMOSOME_III', 'CHROMOSOME_IV']
positions = ['4564564', '4564564', '45645', '456452', '456452']

correct_out = ['ttggcagttgggaccgttta\ncatcgagcagtgcaggaaga\n',
               'tgcccaggaaaatgtgacgt\ncatcccccatgtcgattcga\n',
               'ggagccaaagataacgccct\ncggtaaccggcaattttgga\n',
               'caaggagagttgtgccgact\natgggctctctctccctctc\n',
               'gacaggccgaggtatgtacg\nctgcaagttctcgggcagta\n']

score = 0
for i in range(len(chromosomes)):
    out = subprocess.run(['python', script_path, fasta_file, chromosomes[i], positions[i]], encoding='utf-8',
                         capture_output=True).stdout
    print(out)                    
    score += 2 * (out == correct_out[i])
print(f"Score: {score}/10")
