#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
print("Match found:", match.group() if match else "No match")


# In[2]:


import re
pattern = r"cat"
text="The cat sat on the mat."
match = re.search(pattern, text)
print("Match found:", match.group() if match else "No match")


# In[3]:


pattern = r"c.t"
text = "The cat sat."
match = re.search(pattern, text)
print("Match found:", match.group() if match else "No match")


# In[4]:


pattern = r"[a-z]+"
text = "Hello World 123"
matches = re.findall(pattern,text)
print("Matches found:", matches)


# In[9]:


#pattern = r"[a-z A-Z 0-9]+"
pattern = r"[a-zA-Z\d]+"
text = "Hello World 123"
matches = re.findall(pattern, text)
print("Matches found:", matches)


# In[12]:


pattern = r".+"
text = "content"
match = re.search(pattern, text)
print("Greedy match:", match.group())
 
pattern_lazy = r".+?"
match_lazy = re.search(pattern_lazy, text)
print("Lazy match:", match_lazy.group())


# In[13]:


pattern = r"(\d{3})-(\d{2})"
text = "Phone number: 123-45"
match = re.search(pattern, text)
print("Area code:", match.group(1))
print("Local code:", match.group(2))


# In[15]:


pattern = r"cat"
text = "The cat sat on the mat."
result = re.sub(pattern, "dog", text)
print("After substitution:", result)


# In[16]:


pattern = re.compile(r"\d+")
text = "123 apples, 456 bananas"
matches = pattern.findall(text)
print("matches:", matches)


# In[18]:


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-\.[a-zA-Z]{2,}'


# In[ ]:


#write a program that takes a list of email and print whether its valid or invalid


# In[19]:


#check for strong password
# Python program to check validation of password
# Module of regular expression is used with search()
import re
password = "R@m@_f0rtu9e$"
flag = 0
while True:
    if (len(password)<=8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]" , password):
        flag = -1
        break
    elif re.search("\s" , password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password ")


# In[ ]:




