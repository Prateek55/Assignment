# Semantics-Polarity-Generator	

The code consist of set of scripts that can be used for extracting new positice and negative concepts, generating their semantics, polarity and mood tags given an existing concept lexicon and a new data corpus. 

### About the code

The file structure for the directory is as follows:

1. **data**: Contain files have list of all the concepts with positive or negative polarity
	1. **data.xml**: Concept lexicon but with slight tag renaming for easy reading
	2. **negative-words.txt/positve-words.txt**: Contain a new set of words with negative/positive polarity downloaded from https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/blob/master/data/opinion-lexicon-English/
	3. **semantic_map**: All concepts mentioned in the XML file are stored in the following format: 
		concept#semantic1#semantic2#semantic3#semantic4#semantic5#polarity
		The file is used for fast extraction of data
	4. **neg/pos/neut_word_corpus**: Stores list of all concepts with positive/negative/neutral polarity that are present in concept lexicon.
The program reads the file 'sample.txt' (you can change the filename in main.c if required) and parse each line as a seperate SQL command. If the syntax is valid, it builds and output a Parse Tree. Otherwise, it throws an error

2. **moods**: Contain files that both compute the concept-related moods as well as store the concepts in different files depending on positive or negative polarity
	1. **find_(pos/neg)_mood.py**: The file extracts all the NEW concepts of pos/neg polarity and allocate mood based on similarity score from related moods. It then stores them in the following files
	2. **neg/pos_moody_words.py** : The file contains list of all the concepts for which appropriate distinct score was generated in the following format 
		concept mood1 mood2
	3. **neg/pos_moody_words.py**: Same as above but store similarity score as well

3. **new_words**: Contains files for extracting new words as well as storing them
	1. **hunt_new_words.py**: From the new set of words, it extract words not present in concept lexicon
	2. **negative/positive**: List of new pos/neg concepts not present in concept lexicon

4. **polarity**: Contain files that deal with polarity calculation
	1. **nltk_pol_calc.py**: sample code for polarity calculation using nltk
	2. **polarity_classifier.py**: create the files neg/pos/neut_corpus in data folder by classifying on the basis of polarity given in concept lexicon
	3. **twitter_pol_check**: Find the words that have different polarities in new Twitter data and concept lexicon. Store them in a file in collision folder
	4. find_pol_er.py : find all the concepts of concept lexicon that have opposite polarities of semantics

5. **semantics** : Contain files responsible for computing related semantics of the new concepts. The semantics are picked up from the concepts of concept lexicon itself
	1. **pos/neg_semantics**: Store 10 most closely related semantics for new concepts for which appropriate mood could be generated
	2. **find_sem.py**: Generate the above file

6. **compile** : Contain file responsible for combining moods and semantics of the new words and storing them in appropriate file
	1. **neg/pos_concepts**: Contain the new concepts in the appropraite format
	2. **reviewed_neg/pos_concepts**: The above file, after manual inspection for verb inflections/plurals and removing inappropriate concepts
	3. **compilation.py**: Create the above file by combining moods and semantics from their files in the moods and semantics directory

7. **collisions**: Contains all the concepts with opposite polarities in different lexicons. Also include the file that generate new sementics for the concepts with problematic concepts
	1. **collision_polarity_finder.py**: Find all the stored concepts that have opposite polarities in conecept lexicon and NLTK and stores them
	2. **find_pol_er.py**: Find all concepts which have problematic semantics, i.e. opposite polarity and stores them in error files
	3. **error/error_log**: Store problematic concepts in different format
	4. **find_unknow.py**: Find all semantics and there corresponding concepts where semantic is not itself a concept in concept lexicon
	5. **pos/neg_correction.py**: For all possible problematic concepts, the file find appropraite list of semantics from concept lexicon
	6. **suggest_semantics.py**: Find the appropriate semantics from the above result that can act as substitution for problematic substitution
	7. **nltk_collision_N/P**: Concepts with opposite polarities in nltk and concept lexicon. The format is "Concept <- P" if the concept is positive in concept lexicon and negative in NLTk. "Concept<-N" is for vice-verse
	8. **tweet_collision_N/P**: Similar as above, just for the new data
	9. **reviewed/reviewed_nltk_coll_N/P**: Same as above file, but after reviewing the concepts manually
	10. **reviewed/reviewed_tweeter_coll_N/P**: Same as above file, but after reviewing the concepts manually
	11. **pos/neg_correction**: Contain the list of similar semantics from concept lexicon for problematic concepts
	12. **suggested_semantics**: Contains the suggested semantics for problematic concepts.