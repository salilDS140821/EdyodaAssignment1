#!/usr/bin/env python
# coding: utf-8

# ## Write a Python program to get the Fibonacci series between 0 to 50.

# In[5]:


a=0   # assigning the first value
b=1   # assigning the second value

print(a)
print(b)

for i in range (0,8):
  
    c = a+b   # adding the value of a and b
    a=b       # now a will take the value of b i.e the value of a will change from 0 to 1
    b=c       # now b will take the value of c i.e the value of b will change from 1 to 1 again. 
              # And again of iteration new values will assigned.
    print(c)
    


# ## Write a Python program that accepts a word from the user and reverse it.

# In[50]:


name = input("The name is:")
l= len(name)    # l save the length of the name entered

for i in range(l-1,-1,-1): # l-1 idicates the last index value. Eg: The length of "apple" is 5 and the last index value is 4.
    print(name[i],end="")
       


# In[2]:


name = input("The name is:")
print(name[::-1])


# ## Write a Python program to count the number of even and odd numbers from a series of numbers.

# In[1]:


x = [1,2,3,4,5,6,7,8,9,10]

Odd=0
Even= 0

for i in x:
    if i%2==0:
        Even= Even+1   # increasing the count of even numbers
    else:
        Odd= Odd+1     # increasing the count of odd numbers
       
print("The count of Even numbers is:", Even)
print("The count of Odd numbers is:", Odd)


# In[22]:


Odd=0
Even= 0


for i in input().split(','):
    if int(i)%2==0:
        Even= Even+1
    else:
        Odd= Odd+1
print("The count of Even numbers is:", Even)
print("The count of Odd numbers is:", Odd)


# In[ ]:




