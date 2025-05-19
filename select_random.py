#!/usr/bin/env python3

import random
from Bio import SeqIO
import sys

"""
we have to do this because if we work with large negative dataset, the training of hmm getting 
slower, also overfitting increase, thats why positive data and negative data should be in balance

"""


def select_random(file):
	records = list(SeqIO.parse("pdb_not_kunitz_Achain.fasta", "fasta"))
	sampled = random.sample(records, 400) # select 400 samples because we have 3998 positive sample, it should be in balance.
	
	with open("not_kunitz_random_400.fasta","w") as final:
		SeqIO.write(sampled, final, "fasta")




if __name__ == '__main__':
	file = sys.argv[1]
	select_random(file)
