
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp


#train_df_raw = pd.read_csv('/media/sahar/201F64032690A3BE/FAU/Research/Sentiment/Python/deep-learning/Data/logistic/Train-data2.csv',header=None, names=['body','sentiment'])
#test_df_raw = pd.read_csv('/media/sahar/201F64032690A3BE/FAU/Research/Sentiment/Python/deep-learning/Data/logistic/Test-data2.csv',header=None, names=['body','sentiment'])
DataSet = pd.read_csv("/home/sahar/Projects/FAU/Research/Sentiment/Data/wordNet-rpl999.csv",header=None, names=['sentWordNet','label'])
predictions = [1 if x=='1' else 0 for x in DataSet['sentWordNet'].tolist()]
label = [1 if x=='1' else 0 for x in DataSet['label'].tolist()]

# fpr, tpr, thresholds = metrics.roc_curve(label, predictions, pos_label=1)
# roc_auc = auc(fpr,tpr)
#
# print 'Accuracy:', accuracy_score(label, predictions)
# print 'F1_Score:',(f1_score(label, predictions))
# print 'precision_score:', (precision_score(label, predictions))
# print 'recall_score:' , (recall_score(label, predictions))
# print 'ROC:' , (roc_auc_score(label, predictions))
# confusion_matrix = confusion_matrix(label, predictions)
# print(confusion_matrix)


fpr, tpr, thresholds = metrics.roc_curve(label, predictions, pos_label=1)
roc_auc = auc(fpr,tpr)
# print(fpr)
# print(tpr)
# print(thresholds)
accu = accuracy_score(label, predictions)
pre = precision_score(label, predictions)
rec = recall_score(label, predictions)
fone = f1_score(label, predictions)
rocScore = roc_auc_score(label, predictions)
print(pre)
print(accu)
print(rec)
print(fone)
print(rocScore)
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()