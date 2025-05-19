#!/usr/bin/env python3
import sys

def clean(file):
	aa="ACDEFGHIKLMNPQRSTVWY"
	clean_file = open("kunitz_clean_cdhit.fasta","w")
	
	with open(file,"r") as read:
		name = ""
		seq = ""
		for line in read:
			line = line.strip()
			if line.startswith(">"):
				if seq:
					if 30<= len(seq) <=100:
						a=True
						for j in seq:
							if j not in aa:
								a = False
								break
						if a is True:
							clean_file.write(f"{name}\n")
							clean_file.write(f"{seq}\n")
				name = line
				seq = "" #for starting new sequence
			else:
				seq += line.upper()
				
		if seq: #for last line
			if 30<= len(seq) <=100:
				a=True
				for j in seq:
					if j not in aa:
						a = False
						break
				if a is True:
					clean_file.write(f"{name}\n")
					clean_file.write(f"{seq}\n")
					
	clean_file.close()
	




	
	
if __name__ == '__main__':
	file = sys.argv[1]
	clean(file)
