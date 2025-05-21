# Create Hidden Markov Model For Detecting Kunitz Domain

This project aims to determine the Kunitz domain found in various proteins using the Hidden Markov Model.


## 1. Project Overview

1. Data Collection
Download protein structure data containing kunitz domain from Protein Data Bank. For .csv format use bash code for converting .fasta file. For .json format use python script to convert .fasta file.

2. Data Preparation
Use .fasta file for 'cd-hit' to removing repeated and identical sequences. The aim is decrease the redundancy.

3. Multiple Sequence Alignment
For creating model, HMMER tool uses aligned data. Thats why we have to align .fasta file from cd-hit.

4. Building a Hidden Markov Model
Create HMM with aligned file using HMMER tool. 

5. Model Test
Get some positive and negative data from UniProt and PDB. Then applied some machine learning approaches for test the model.


### Requirements
- Python 3.xx
* Python Libraries: NumPy, pandas, scikit-learn, matplotlib
- CD-HIT
- HMMER Tool
- Clustal Omega
- For Windows Ubuntu or any kind of Linux environment

## 2. Usage
1. Initial Data Preparation

Inside the initial_data/ folder, you will find PDB data containing proteins with and without the Kunitz domain, as well as UniProt data used for model testing.
To clean and format these .fasta files, run the appropriate Bash commands. The cleaned files will be saved in the clean_data/ folder.

2. Removing Redundant Sequences with CD-HIT

Use the cd-hit command (included in the bash_codes.sh script) to reduce redundancy and retain only representative sequences.
Then run get_clean_cd-hit.py to further format the CD-HIT output for multiple sequence alignment.

3. Multiple Sequence Alignment (MSA)

Use Clustal Omega to perform MSA on the cleaned sequences. This step is also included in the bash_codes.sh script.
Ensure Clustal Omega is installed and run the alignment command in a Linux environment.

4. Building the HMM

Once you have the aligned .fasta file, use the hmmbuild command from the HMMER suite to create your Hidden Markov Model.
This model will capture the conserved features of the Kunitz domain.

5. Model Testing and Evaluation

* Before testing, run the final Bash command to generate a .tbl file using HMMER output (to 'kunitz_notkunitz_test.fasta' this file).
* Extract protein IDs for Kunitz and non-Kunitz sequences.
* Use parse_tbl_file.py to convert the .tbl results into a structured .csv file.
* Run ML_tests_and_confusion_matrix.py on this .csv to evaluate model performance.
* The machine learning script will return:
- Accuracy
- Precision
- F1-score
- Confusion Matrix
- Learning Curve / Training Progress
