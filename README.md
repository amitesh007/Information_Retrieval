# Information_Retrieval
Setup Instruction
1.	Create a directory C:\ir_assignment

2.	Download and Unzip the IR_ASSIGNMENT_AMITESH_RANJAN_SRIVASTAVA_2017HT12082.zip in that directory


3.	Open a Python IDE – such as spider (or any) and set the workspace to the following path –
“C:\ir_assignment\IR_ASSIGNMENT_AMITESH_RANJAN_SRIVASTAVA_2017HT12082\executable”

WITH_PRE_PROCESSING
4.	Now in your python IDE , execute the following python scrips in following sequence:
- Inverted_Index_WITH_PRE_PROCESSING.py  - it will create a following file in the same path –“ inverted_index_file_with_pre_processing.csv”

5.	Now run the script – “QuerySearch_WITH_PRE_PROCESSING.py” – it will generate following files   

 –“ output_test_file_with_pre_processed.csv”: This is the output file running against the preprocessed inverted index   
   
-“output_test_evaluation_with_pre_processed.csv” : This is evaluation file created from confusion matrix by using “input_test_file.csv” and  “output_test_file_with_pre_processed.csv”.  “input_test_file.csv” contains column “WORD1” and “ WORD2” and since we know that if both the words are present in different documents therefore by taking there intersection they should return the matching documents . So the 3rd column “OUTPUT_INTERSECTION” is 1  if intersection returns at least one common document  otherwise  it is 0. “input_test_file.csv” is already known to us.     

 WITHOUT_PRE_PROCESSING                                                                                                                  
6.	Now in your python IDE , execute the following python scrips in following sequence:
- Inverted_Index_WITHOUT_PRE_PROCESSING.py  - it will create a following file in the same path –“ inverted_index_file_without_pre_processing.csv”

7.	Now run the script – “QuerySearch_WITHOUT_PRE_PROCESSING.py” – it will generate following files    

–“ output_test_file_with_pre_processed.csv”: This is the output file running against the preprocessed inverted index   
   
-“output_test_evaluation_without_pre_processed.csv” : This is evaluation file created from confusion matrix by using “input_test_file.csv” and  “output_test_file_without_pre_processed.csv”.  “input_test_file.csv” contains column “WORD1” and “ WORD2” and since we know that if both the words are present in different documents therefore by taking there intersection they should return the matching documents . So the 3rd column “OUTPUT_INTERSECTION” is 1  if intersection returns at least one common document  otherwise  it is 0. “input_test_file.csv” is already known to us.    
                                                     

