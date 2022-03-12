#!/usr/bin/env python
# coding: utf-8

# In[29]:


import time


# In[30]:


t=int(input(' saisir la durée du compte à rebours en secondes : '))


# In[31]:


int(t)


# In[32]:



  

def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!') 
  
  
 


# In[33]:


countdown(t)


# In[ ]:




