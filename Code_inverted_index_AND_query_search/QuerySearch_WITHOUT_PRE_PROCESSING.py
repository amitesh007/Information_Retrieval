

import csv
import pandas as pd

dictionary={}
input_file = csv.DictReader(open("inverted_index_file_without_pre_processing.csv"))
for row in input_file:
    dictionary=row
    


def getDocListForGivenWord(word):
    word=str(word).strip()
    list_1=[]   
    value_text=""
    doc_list=[]
    if word in dictionary:
        value_text=dictionary.get(word)
        value_text
        value_text=value_text.replace("{","")
        value_text=value_text.replace("}","")
        list_1=value_text.split(",")
        for i in range(len(list_1)):
            newList_1=[]
            new_value_text=list_1[i]
            newList_1=new_value_text.split(":")
            text=newList_1[0].replace("'","")
            text=text.strip()
            doc_list.append(text)
    return set(doc_list)


'''
Main Method to get the inverted index and create an ouput cv file for Inverted Index
''' 
dataset = pd.read_csv("input_test_file.csv")
word1 = dataset.WORD1
list_word1=list(word1)

word2 = dataset.WORD2
list_word2=list(word2)

actual_op = dataset.OUTPUT_INTERSECTION
list_actual_op=list(actual_op)
list_predicted_output=[]

output_result=[]

for i in range(len(dataset)): 
    output=[]
    result=[]
    li1={}
    li2={}
    li1=getDocListForGivenWord(list_word1[i])
    li2=getDocListForGivenWord(list_word2[i])  
    result=list(li1.intersection(li2))
    
    if(len(result) == 0):
        output.append(list_word1[i])
        output.append(list_word2[i])
        output.append(0)
        list_predicted_output.append(0)
    else:
        output.append(list_word1[i])
        output.append(list_word2[i])
        output.append(1)
        list_predicted_output.append(1)
    
    output_result.append(output)

header = ["WORD1", "WORD2", "OUTPUT_INTERSECTION"]
df = pd.DataFrame.from_records(output_result,columns = header)
df.to_csv("output_test_file_without_pre_processed.csv", sep=',')


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
    
tn, fp, fn, tp = confusion_matrix(list_actual_op, list_predicted_output).ravel()

accuracy = ((tp+tn)/(tp+fn+fp+tn))*100

precision = (tp/(tp+fp))*100

recall=(tp/(tp+fn))*100

fmeasure = 2*tp+fn+fp/tp

evaluation_list=[]
listEva=[]
print("accuracy: ",accuracy)
print("precision: ",precision )
print("recall: ",recall)
print("fmeasure: ",fmeasure)
listEva.append(str(accuracy))
listEva.append(str(precision))
listEva.append(str(recall))
listEva.append(str(fmeasure))
evaluation_list.append(listEva)

header = ["accuracy", "precision", "recall","fmeasure"]
df1 = pd.DataFrame.from_records(evaluation_list,columns = header)
df1.to_csv("output_test_evaluation_without_pre_processed.csv", sep=',',index=False)
   
