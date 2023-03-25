#!/usr/bin/env python
# coding: utf-8

# In[125]:


import nltk
import spacy
import bs4
from bs4 import BeautifulSoup
nlp=spacy.load('en_core_web_sm')
import requests 
url= 'https://indianexpress.com/article/entertainment/web-series/johnny-lever-and-saurabh-shukla-parody-pathaan-scene-ft-shah-rukh-salman-khan-kapil-sharma-diss-8475319/' 
r= requests.get(url)
htmlcontent = r.content
soup= BeautifulSoup(htmlcontent, 'html.parser')
soup.prettify
rawd= soup.find_all('p')
for element in rawd:
    data= element.get_text()
    #print(data)
    #print(type(data))
    #tokenise para into sentences using nltk.sent_tokenize
    sentence= nltk.sent_tokenize(data) ##sent_tokenize splits our paragraph into many sentences
#print(type(sentence))
    for sent in sentence:
        print(sent)
        

 


# In[100]:





# In[82]:





# In[93]:


name = "Salman Khan"
name_list = name.split("K")
print(name_list)


# In[131]:





# In[132]:


import nltk
import spacy
import requests 
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup

nlp = spacy.load('en_core_web_sm')

#for url in df: #this loop will be applied on all the articles present in our dataframe df and will store the relevant sentences in 'news' for every article

url = 'https://indianexpress.com/article/entertainment/web-series/johnny-lever-and-saurabh-shukla-parody-pathaan-scene-ft-shah-rukh-salman-khan-kapil-sharma-diss-8475319/' 
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
rawd = soup.find_all('p')

for element in rawd:
    data = element.get_text()
    sentence = nltk.sent_tokenize(data) 
    
    news = ""
    name='Salman Khan'
    
    for i in sentence:
        article = nlp(i)  #this code applies ner to the elements of the list 'sentences' and if the name of the person 
        for ent in article.ents:
            if (ent.label_=="PERSON") & ((ent.text == name) | (ent.text in name.split(' '))): ## this block of code identifies the  sentences that contain the name of our interest and adds it to the news string on which sentiment analysis will be applied
                news = news + " " + i
                print(news)



# In[ ]:





# In[ ]:




