#!/usr/bin/

# For convert fasta file from csv file
cat kunitz_pdb_data.csv |tr -d '"' |awk -F ',' '{if (length($2)>0) {name=$2}; print name,$3,$4,$5,$6}' |grep PF00014 |awk '{print ">"$1"_"$3;print $2}'  > pdb_kunitz.fasta

# For cd-hit command
cd-hit -i pdb_kunitz.fasta -o kunitz_cdhit.fasta -c 0.95 -aL 0.9

# For Multiple Sequence Alignment
clustalo -i kunitz_clean_cdhit.fasta -o kunitz_aligned.fasta --outfmt=fasta

#For build HMM with using HMMER
hmmbuild detect_kunitz_model.hmm kunitz_aligned.fasta

#For apply HMM to data
hmmsearch --noali --max --tblout kunitz_notkunitz_results.tbl -Z 1 detect_kunitz_model.hmm kunitz_notkunitz_test.fasta
