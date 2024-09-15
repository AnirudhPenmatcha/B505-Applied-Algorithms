#!/usr/bin/env python
# coding: utf-8

# In[49]:


def xAyB(secret: str, guess: str) -> str:
    hash = {}; x = 0; y = 0
    length = len(secret)
    
    for i in range(length):
        if secret[i] not in hash.keys():
            hash[secret[i]] = 1
        elif secret[i] != guess[i]:
            hash[secret[i]] += 1
    print(hash)
    
    
    for j in range(length):
        if secret[j] == guess[j]:
            x += 1
        elif guess[j] in hash.keys() and hash[guess[j]] > 0:
#             print(guess[j])
            hash[guess[j]] -= 1
            y += 1
        
    return f"{x}A{y}B"


# In[50]:


xAyB(secret = "22105", guess = "12324") #1A2B


# In[51]:


xAyB("1123","0111") #1A1B


# In[52]:


xAyB("314159265358979","271828182845904") #1A7B

