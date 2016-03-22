# Classify words from SenticNet into pos,neg and neutral
from senticnet.senticnet import Senticnet
from bs4 import BeautifulSoup


pos_file=open('../data/pos_word_corpus','w');
neg_file=open('../data/neg_word_corpus','w');
neut_file=open('../data/neut_word_corpus','w');

with open('semantic_map','r') as sem_map:
	for line in sem_map:
		line=line[:-1]
		concept=line.split("#")[0]
		pol_value=float(line.split("#")[-1]) # Polarity was already stored in the map
		#Classification
		if pol_value>0:
			pos_file.write(concept+"\n")
		elif pol_value<0:
			neg_file.write(concept+"\n")
		else:
			neut_file.write(concept+"\n")
