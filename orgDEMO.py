#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[3]:


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} 
webpage = requests.get('https://books.toscrape.com/catalogue/category/books_1/index.html',headers=headers).text


# In[4]:


get_ipython().run_line_magic('pip', 'install lxml')
import lxml
print("lxml installed successfully!")


# In[5]:


get_ipython().run_line_magic('pip', 'install --upgrade pip')


# In[6]:


soup = BeautifulSoup(webpage, 'lxml')



# In[7]:


info=soup.find_all('article',class_="product_pod")


# In[8]:


len(info)


# In[15]:


name=[]
rating=[]
price=[]
Availibility=[]
for i in info:
    name.append(i.find('h3').text.strip())
    rating.append(i.find('p', class_='star-rating')['class'][1])
    price.append(i.find('p',class_='price_color').text.strip())
    Availibility.append(i.find('p',class_='instock').text.strip())


# In[16]:


name
rating
price
Availibility


# In[11]:


d={'Name':name,'Ratings':rating,'Price':price,'Availibility':Availibility}
df=pd.DataFrame(d)


# In[12]:


df


# In[17]:


final=pd.DataFrame()

for j in range (1,16):
    url ='https://books.toscrape.com/catalogue/category/books_1/page-{}.html'.format(j)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} 
    webpage = requests.get(url,headers=headers).text
    soup = BeautifulSoup(webpage, 'lxml')
    info=soup.find_all('article',class_="product_pod")
    name=[]
    rating=[]
    price=[]
    Availibility=[]
    for i in info:

        name.append(i.find('h3').text.strip())
        rating.append(i.find('p', class_='star-rating')['class'][1])
        price.append(i.find('p',class_='price_color').text.strip())
        Availibility.append(i.find('p',class_='instock').text.strip())
    d={'Name':name,'Ratings':rating,'Price':price,'Availibility':Availibility}
    df=pd.DataFrame(d)
    final = pd.concat([final, df], ignore_index=True)


# In[18]:


final


# In[ ]:




