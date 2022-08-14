#!/usr/bin/env python
# coding: utf-8

# # Python Data Types

# In programming we classify data as types for variables. \
# __Variables can store data of different types__, and different types can do different things.\
# Python has the following data types __built-in__ by default, in these categories:

#         Text Type:	str 
#     Numeric Types:	int, float, complex 
#     Boolean Type:	bool
#     Binary Types:	bytes, bytearray, memoryview
#     
#     Sequence Types:	list, tuple, range 
#     Mapping Type:	dict
#     Set Types:	    set, frozenset
#     None Type:	    NoneType

# Getting the Data Type\
# You can get the data type of any object by using the __type()__ function:

# Example\
# Print the data type of the variable e:

# In[1]:


e = 2.718
print( type(e))


# Setting the Data Type\
# In Python, the data type is __set automatically when you assign a value__ to a variable:

# In[2]:


a = 'Hello ITCS-159'; print( type(a))


# In[3]:


a = 20; print( type(a))


# In[4]:


a = ["apple", "banana", "cherry"]; print( type(a))


# In[5]:


a = {"name" : "John", "age" : 36}; print( type(a))


# In[6]:


a = True; print( type(a))


# In[7]:


a = b"Hello"; print( type(a))


# In[ ]:





# # Python Number

# Three numeric types in Python

# - int
# - float
# - complex

# Variables of numeric types are created automatically when you assign a value to them:

# In[8]:


temp = 25    # int
e = 2.718  # float
z = 1+1j   # complex


# To verify the type of any object in Python, use the __type()__ function:

# Example: 

# In[9]:


print( type(temp))
print( type(e))
print( type(z))


# ### Int or Integer Number
# A whole number, positive or negative, without decimals, of unlimited length.

# #### Example
# Integers:

# In[10]:


a = 9
b = 34879283457
c = -10000000000

print( type(a))
print( type(b))
print( type(c))


# ### Float
#  __floating point number__ is a number, positive or negative, containing one or more decimals.

# Example \
# Float:

# In[ ]:





# In[11]:


e = 2.718
pi = 3.14
x = -35.59

print( type(e))
print( type(pi))
print( type(x))


# Float can also be scientific numbers with an __e__ to indicate the power of __10__.

# Example \
# Scientific number:

# In[12]:


a = 15e-1
b = 15e2
c = -15.16e-2

print( type(a))
print( type(b))
print( type(c))


# ### Complex 
# Complex numbers are written with a "j" as the imaginary part:

# Example\
# Complex:

# In[13]:


a = 1 + 2j
b = 1.5j
c = -5j

print( type(a))
print( type(b))
print( type(c))


# ### Type Conversion
# You can convert from one type to another with the __int()__, __float()__, and __complex()__ methods:

# Example \
# Convert from one type to another:

# In[14]:


x = 7    # int
y = 3.14  # float
z = 4j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# ### Random Number
# To make a random number, but Python has a  module called __random__ that can be used to make random numbers:

# In[15]:


import random

print(random.randrange(1, 10))


# In[ ]:





# In[ ]:





# ## Python Indentation
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




