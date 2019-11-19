#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns


# In[4]:


def clusters(df, yieldlvl = "medio"):
    anls = df.groupby(['Cluster','cultivo',"provincia"], as_index=True).max()
    anls = pd.DataFrame(anls)
    anls.reset_index(["cultivo","provincia"], inplace=True)
    pd.set_option('max_rows',300)
    anls.sort_values('rendimiento',ascending=False, inplace=True)
    if yieldlvl == "alto":
        i = 3
    if yieldlvl == "medioalto":
        i = 1
    if yieldlvl == "mediobajo":
        i = 4
    if yieldlvl == "bajo":
        i = 0
    if yieldlvl == "medio":
        i = 2  
    print(anls.loc[i])
#    i.clear()
#alto, medioalto, medio, mediobajo, bajo
#orden de mayor a menor producción 3,1,2,4,0


# In[6]:


def analisis(Data, ID, provincia = "BUENOS AIRES"):
    i = (ID.index[ID['provincia'] == provincia]).tolist()
    i = int(i[0])
    
    sns.pairplot(data = Data[i], palette='husl')
    plt.show()
    
    corr = Data[i].corr()
    f, ax = plt.subplots(figsize=(15, 15))
    sns.heatmap(corr, vmax=.8, square=True);
    plt.show()
    
    sns.set(rc={'figure.figsize':(15,15)})
    rcParams['axes.titlesize'] = 25
    sns.set_context("paper")
    ay = sns.boxplot(data = Data[i], palette='husl')
    ay.set_xticklabels(ay.get_xticklabels(), rotation=40, ha="right")
    plt.title("Variación de producción de cultivos con el tiempo")
    plt.show()


# In[ ]:




