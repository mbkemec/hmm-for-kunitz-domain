#!/usr/bin/python3

import json

def convert(file_name):
	with open(file_name,"r") as file:
		json_data = json.load(file)
	
	fasta_format_file = "pdb_notkunitz.fasta"
	with open(fasta_format_file, "w") as fasta_format:
		for entry in json_data:
			if "data" in entry and "rcsb_entry_container_identifiers" in entry["data"]:
				pdb_id = entry["data"]["rcsb_entry_container_identifiers"].get("entry_id", None)
				polymer_entities = entry["data"].get("polymer_entities", [])
				
				if pdb_id and polymer_entities:
					for protein in polymer_entities:
						entity_poly = protein.get("entity_poly", {})
						sequence = entity_poly.get("pdbx_seq_one_letter_code_can", None)
						
						instances = protein.get("polymer_entity_instances", [])
						
						for inst in instances:
							instance_id = inst.get("rcsb_polymer_entity_instance_container_identifiers", {})
							chain_id = instance_id.get("auth_asym_id", None)
							
							if sequence and chain_id == "A":
								fasta_format.write(f">{pdb_id}_{chain_id}\n")
								fasta_format.write(sequence + "\n")
								


if __name__ == '__main__':
	file_name = input("Write your json file name: ")
	convert(file_name)
