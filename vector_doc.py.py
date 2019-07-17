#!/usr/bin/env python
# coding: utf-8

# In[51]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd


# In[79]:


doc_list=[]
word_bg={}  
for i in range(1,11):
    f=open("C:/Users/Admin/Desktop/India"+str(i)+".txt",'r',encoding='utf-8',errors='replace')
    doc_list.append(word_tokenize(f.read().lower()))
stop_words=set(stopwords.words('english'))

for i in range(1,11):
    for j in doc_list[i-1]:
        
        if  j not in stop_words and j.isalpha(): #Removing stopwords and unwanted Regular Expressions
            word_bg.setdefault(j,[])
            
            

for i in range(len(doc_list)):
    for j in word_bg.keys():
        if j in doc_list[i]:
            word_bg[j].append(1)
        else:
                word_bg[j].append(0)
word_df=pd.DataFrame(word_bg,index=["Doc1","Doc2","Doc3","Doc4","Doc5","Doc6","Doc7","Doc8","Doc9","Doc10"])
word_df
            


# In[84]:


#Count of each word(Column sum)
Col_sum=word_df.sum(axis=0)
print("Count of each word\n",Col_sum.head(20))


# In[85]:


#Number of words(Row sum)
Row_sum=word_df.sum(axis=1)
print("Number of words\n",Row_sum)


# In[ ]:




