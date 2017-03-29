
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

text1 = "Florida culture is a reflection of influences and multiple inheritance; Native American, European American, Hispanic and Latino, and African American heritages can be found in the architecture and cuisine."
text = "From our awesome culture, to the amazing food, to the gorgeous scenery, there are plenty of things about Florida that make it just plain awesome. "
analyzer = SentimentIntensityAnalyzer()
# vs = analyzer.polarity_scores(text1)
# print(vs)
vs1 = analyzer.polarity_scores(text)
print(vs1)





