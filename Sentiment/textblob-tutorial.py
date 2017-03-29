from textblob import TextBlob
text = TextBlob("Florida culture is so unique influences and multiple inheritance; Native American, European American, Hispanic and Latino, and African American heritages can be found in the architecture and cuisine.")
text2 = TextBlob(" From our awesome culture, to the amazing food, to the gorgeous scenery, there are plenty of things about Florida that make it just plain awesome. ")
# print(text.tags)
# print(text.noun_phrases)
# print(text.sentiment)
#print(text.sentiment.polarity)
# print (text2.sentiment)
#print(text2.sentiment.polarity)

#######################################################
# sing = TextBlob("computer crisis man mouse tooth")
# print(sing.words)
# print(sing.words.pluralize())
# #######################################################
# test = TextBlob("Havv a goood tim witt Python")
# print(test.correct())
# ########################################################
en = TextBlob('simple is better than complex')
print(en.translate(to='es'))
print(en.translate(to='zh-CN'))