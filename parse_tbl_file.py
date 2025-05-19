#!/usr/bin/env python3

import sys
import csv
import pandas as pd

def dict_ids(positives,negatives):
	#for positives = 1, negatives = 0 (kunitz/notkunitz)
	id_dict = {}
	
	with open(positives,"r") as p:
		for line in p:
			protein_id = line.strip()
			if protein_id: # for empty lines
				id_dict[protein_id] = 1

	with open(negatives,"r") as n:
		for line in n:
			protein_id = line.strip()
			if protein_id:
				id_dict[protein_id] = 0

	return id_dict

def parse(hmm_result, id_dict):
	#get e-values and ids from hmm_result file
	results = []
	
	with open(hmm_result,"r") as hmm:
		for line in hmm:
			if line.startswith("#"):
				continue
			parts = line.strip().split()
			if len(parts) < 5:
				continue
			long_id = parts[0]
			if "|" in long_id:
				protein_id = long_id.split("|")[1]
			else:
				protein_id = long_id
			
			if protein_id in id_dict:
				e_value = float(parts[4])
				label = id_dict[protein_id]
				results.append((protein_id,e_value,label))
	return results

def create_csv(result,output="final_hmm_model_results.csv"):
	
	with open(output,"w",newline="") as file:
		writer = csv.writer(file)
		writer.writerow(["ID","E-value","Label"])
		for row in result:
			writer.writerow(row)

	
	
	
if __name__ == "__main__":
	hmm_result = sys.argv[1]
	positives = sys.argv[2]
	negatives = sys.argv[3]
	
	id_dict = dict_ids(positives,negatives)
	results = parse(hmm_result,id_dict)
	create_csv(results)
	df = pd.read_csv("final_hmm_model_results.csv")
	df_shuffled = df.sample(frac=1,random_state=42).reset_index(drop=True)
	df_shuffled["E-value"] = df_shuffled["E-value"].apply(lambda x: f"{x:.2e}")
	df_shuffled.to_csv("final_hmm_model_results.csv", index=False)










