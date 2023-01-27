#!/usr/bin/env python
# coding: utf-8

# In[6]:


x=int(input("enter marks \n"))
if 0<=x<25:
    y="F"
if 25<=x<45:
    y="E"
elif 45<=x<50:
    y="D"
elif 50<=x<60:
    y="C"
elif 60<=x<80:
    y="B"
elif 80<=x<=100:
    y="A"
else:
    print("invalid marks")
print("Grade: ",y)
    


# In[11]:


x=int(input("ENTER YEAR IN THOUSANDS \n"))
if x%4==0 and x%100!=0:
    print(x," is a leap year")
elif x%100==0 and x%400==0:
    print(x," is a leap year")
elif x%100==0 and x%400!=0:
    print(x," is not a leap year")
elif x%4!=0:
    print(x," is not a leap year")
elif x<1000:
    print("year not in thousands")


# In[20]:



import random
l=1
while l<11:
    x=random.randint(1,10)
    y=random.randint(1,10)
    print("question",l,":",x,"X",y,"=")
    a=int(input())
   
    if a==x*y:
        print("Right")
    else:
        print("Wrong,the answer is",x*y)
    l=l+1
    


# In[26]:


for x in range(200):
    if x%5==2 and x%6==3 and x%7==2:
        print(x)


# In[ ]:




