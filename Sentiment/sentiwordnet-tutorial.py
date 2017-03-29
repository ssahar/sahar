import sentlex
import sentlex.sentanalysis

text1 = "Florida culture is a reflection of influences and multiple inheritance; Native American, European American, Hispanic and Latino, and African American heritages can be found in the architecture and cuisine."
text = "From our awesome culture, to the amazing food, to the gorgeous scenery, there are plenty of things about Florida that make it just plain awesome. "
SWN = sentlex.SWN3Lexicon()
classifier = sentlex.sentanalysis.BasicDocSentiScore()
cls = classifier.classify_document(text, tagged=False, L=SWN, a=True, v=True, n=False, r=False, negation=False, verbose=False)
print(cls)
# cls1 = classifier.classify_document(text1, tagged=False, L=SWN, a=True, v=True, n=False, r=False, negation=False, verbose=False)
# print(cls1)


