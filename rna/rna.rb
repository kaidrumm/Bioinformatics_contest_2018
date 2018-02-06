input = File.open(ARGV[0].to_s, "r")
output = File.open(ARGV[1].to_s, "w")

def change_amino_acid(codon)

end

aa_unique = [:Met, :Trp]

aa_dictionary = {:Phe => ["UUU", "UUC"], :Leu => ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
	:Ser => ["UCU", "UCC", "UCA", "UCG"], :Stop => ["UAA", "UAG", "UGA"], :Arg => ["CGG", "CGA", "CGC", "CGU", "AGG", "AGA"]}


n = input.gets.to_i # number of test cases
n.times do |variable|
	rna_input = input.gets
	codons = []
	(rna_input.length / 3).times do |i|
		puts rna_input.slice(i*3, 3)
		codons << rna_input.slice(i*3, 3)
	end
	codons = rna_input.split()
	n_intervals = input.gets.to_i
	intervals = []
	n_intervals.times do
		intervals << input.gets.split(" ")

		# xsite = rsites[0]
		# ysite = rsites[1]
		# if ysite <= 3
		# 	output.puts("-1")
		# end
	end
	puts intervals
	puts codons
end