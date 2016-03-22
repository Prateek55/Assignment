from bs4 import BeautifulSoup

map_file=open('data/semantic_map','w')
xml_file=open('data/data.xml','r')
soup = BeautifulSoup(xml_file.read())
sem_map={}
print "Soup ready"
for unit in soup.findAll('unit'):
	text=unit.term.text
	sem_map[text]=[]
	polarity=unit.polarity.text
	print text,polarity
	toWrite=text+"#"
	for semantic in unit.findAll('semantics'):
		term=(semantic.get('rdf:resource')).split("/")[-1]
		term=term.replace("_"," ")
		sem_map[text].append(term)
		toWrite+=term+"#"
	toWrite+=polarity+"\n"
	print toWrite
	map_file.write(toWrite)

	