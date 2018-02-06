import sys
import numpy as np

f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'w')


def change_amino_acid(codon):
	if codon[0] == "U":
		if codon[1] == "U":
			if codon[2] == "U":
				return "C"

class AminoAcid(str):

	def identify(codon):
		if 

	phenylalanine = ["UUU", "UUC"]
	leucine = ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]

	class isoleucine

	class methionine

	class valine

	class serine

	class proline

	class threonine

	class alanine

	class tyrosine

	class stop

	class histidine

	class glutamine

	class asparagine

	class lysine

	class aspartate

	class glutamate

	class cysteine

	class tryptophan

	class arginine

	class glycine


n = int(f.readline()) # number of test cases
while n > 0 :
	rna_input = f.readline()
	n_intervals = f.readline()
	while n_intervals > 0 :
		rsites = f.readline().split(" ")
		xsite = rsites[0]
		ysite = rsites[1]
		if ysite >= 3 :
			g.writeline("-1") # Not possible to change start codon
		n_intervals -= 1