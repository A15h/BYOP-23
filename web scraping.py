#!/usr/bin/env python
# coding: utf-8

# In[4]:


from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='862c6dd645dd4a78ab20df9e09bc6705')
news_sources = newsapi.get_sources()
for source in news_sources['sources']:
    print(source['name']) #prints the sources we are gonnna get our news from
    



data = newsapi.get_everything(q='Salman Khan',language='en',)
print(data)
#print(type(data))
#print(data.keys())

#print(type(data['articles']))
print(data['articles'][0])




for article in data['articles']:
    print('Title : ',article['title'])
    print('Description : ',article['description'],'\n\n')
    print('publised at :' ,article['publishedAt'])
    



def get_data(keyword):
  news = []
  allarticles = newsapi.get_everything(
    q=keyword,
    language='en',   
  )
  articles = allarticles["articles"]
  for i in articles:
    article = {'title':i["title"],'description' : i["description"],'link':i['url'],'published':i['publishedAt']}
    news.append(article)
  return news

data = get_data('salman khan')
data



date_time = data[0]["published"]
date_time



import datetime
format = "%Y-%m-%dT%I%M53Z"
from dateutil import parser
DT = parser.parse(date_time)
print(DT)




import pandas as pd
df = pd.DataFrame(data)
df




get_ipython().system('pip install bs4')
get_ipython().system('pip install beautifulsoup4')
from bs4 import BeautifulSoup
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install nltk')





import requests
import re
url= 'https://indianexpress.com/article/entertainment/web-series/johnny-lever-and-saurabh-shukla-parody-pathaan-scene-ft-shah-rukh-salman-khan-kapil-sharma-diss-8475319/'



#for i in df:
r= requests.get(url)
htmlcontent = r.content
soup= BeautifulSoup(htmlcontent, 'html.parser')
soup.prettify





print(soup.find_all('p'))


# In[98]:


for element in soup.find_all('p'):
    final_data= element.get_text()
    print(final_data)


# In[88]:


import spacy
from spacy.lang.en.examples import sentences 

nlp = spacy.load("en_core_web_sm")
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()




get_ipython().system('pip install -U spacy')
get_ipython().system('python -m spacy download en_core_web_sm')


# In[84]:


nlp = spacy.load("en_core_web_sm")




