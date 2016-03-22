#Sample code for calculating polarity using NLTK
import nltk.sentiment.vader as sentiment

text="written text"
sn=sentiment.SentimentIntensityAnalyzer()
print sn.polarity_scores(text)