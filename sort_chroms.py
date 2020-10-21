#!/usr/bin/python3

def sorted_chroms(chroms):
	chr_name_count = sum([c.startswith('chr') for c in chroms])
	if chr_name_count == len(chroms):
		chroms = [c[3:] for c in chroms]
	elif chr_name_count > 0:
		raise ValueError("Inconsistent naming scheme of chromosomes (some begin with 'chr', others do not)")
	
	num_chroms = []
	alpha_chroms_X = []
	alpha_chroms_Y = []
	alpha_chroms_M = []
	alpha_chroms_other = []
	for split_chrom in [c.split('_', 1) for c in chroms]:
		if split_chrom[0].isdigit():
			num_chroms.append([int(split_chrom[0])] + split_chrom[1:])
		elif split_chrom[0] == 'X':
			alpha_chroms_X.append(split_chrom)
		elif split_chrom[0] == 'Y':
			alpha_chroms_Y.append(split_chrom)
		elif split_chrom[0] == 'M':
			alpha_chroms_M.append(split_chrom)
		else:
			alpha_chroms_other.append(split_chrom)

	num_chroms.sort()
	alpha_chroms_X.sort()
	alpha_chroms_Y.sort()
	alpha_chroms_M.sort()
	alpha_chroms_other.sort()

	num_chroms = [[str(c[0])] + c[1:] for c in num_chroms]

	ordered_chroms = ['_'.join(sc) for sc in \
	num_chroms + alpha_chroms_X + alpha_chroms_Y + alpha_chroms_M + alpha_chroms_other]
	
	if chr_name_count > 0:
		ordered_chroms = ['chr'+c for c in ordered_chroms]

	return ordered_chroms
