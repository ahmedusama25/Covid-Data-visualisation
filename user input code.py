#!/usr/bin/env python
# coding: utf-8

# In[248]:


import requests
from bs4 import BeautifulSoup as BS
import re
import ast
import matplotlib.pyplot as plt                                             
country = input("Enter a country name in lower case: ")
url = "https://www.worldometers.info/coronavirus//country/"+country+"/"    
page = requests.get(url)
soup = BS(page.content,"html.parser")
y=soup.find_all("script")
z=y[19].text
dateString=z.split("\n")
date = dateString[22].strip()[12:-10]
date=ast.literal_eval(date)
bla=soup.find_all(type="text/javascript")
x=bla[8].text
caseString=x.split("\n")[38].strip()[6:-10]
caseString=ast.literal_eval(caseString)
caseString
plt.plot(caseString,date)
plt.yticks(['Mar 31, 2020', 'Apr 5, 2020', 'May 10, 2020', 'Jun 15, 2020'], [
           'Mar 31, 2020', 'Apr 5, 2020', 'May 10, 2020', 'Jun 15, 2020'], rotation='horizontal')
plt.show()

 


    
    


# In[ ]:





# In[ ]:




