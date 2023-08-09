#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### int,float


# In[4]:


x=10.101
print(x,type(x))

# type casting---> changing the value's type
 
x=int(x)
print(x,type(x))

x=int(x)
print(x, type(x))

x= '5'
x=int(x)
print(x, type(x))

x= float(x)
print(x, type(x))


# In[5]:


x=5-3j
print(x, type(x))


# In[6]:


# x= int(x) #uncomment to see the code


# In[7]:


x.real,x.imag


#  ### bin,oct&hexa

# In[9]:


x=5 
print(x, type(x))

x=bin(x)
print(x,type(x))


# ### octa

# In[13]:


x=17
print(x,type(x))
 
x=oct(x)
print(x,type(x))
x=5
print(x,type(x))
 
x=oct(x)
print(x,type(x))
x=-17
print(x,type(x))
 
x=oct(x)
print(x,type(x))


# ## hexa

# x=17
# print(x,type(x))
# 
# x=hex(x)
# print(x,type(x))

# In[17]:


'''
x='17'
print(x,type(x))
 
x=hex(x)
print(x,type(x))
''' # uncomment to see the error


# #### converting bin,oct,hex values to int

# In[21]:


print (int ('0x11',0),int('011',16))


# In[22]:


help(int)


# In[31]:


print(int('0o11',0),int("011",8))


# In[32]:


print(int('0b11',0),int("011",2))


# ### int() with user defined  bases

# In[35]:


int('0011',3),int('0011',17),int('0011',32)


# In[36]:


int('0011',3),int('0011',17),int('0011',32),int('0011',37) # uncomment to see error


# In[ ]:




