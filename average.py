#!/usr/bin/env python
import sys
import pandas as pd

def main():
	filename = sys.argv[1]
	year_spec = sys.argv[2]
	factor = sys.argv[3]
	print('File is ', filename, ' the year is ', year_spec, ' the factor is ', factor)

	input=pd.read_csv(filename)
	year_spec = int(year_spec)
	
	subset_input = input[input.year == year_spec]
	grouped_input = subset_input.groupby(factor).mean()
	weight_input = grouped_input['weight']
	weight_input.to_csv('final.csv')

	print('analysis complete, final file as final.csv, results: ', weight_input)

if __name__ == "__main__":
	main()
