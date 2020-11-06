#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


df_50   = pd.read_csv('tables/out50_nclim.csv')
df_100  = pd.read_csv('tables/out100_nclim.csv')
df_200  = pd.read_csv('tables/out200_nclim.csv')
df_500  = pd.read_csv('tables/out500_nclim.csv')
df_1000 = pd.read_csv('tables/out1000_nclim.csv')
df_3000 = pd.read_csv('tables/out3000_nclim.csv')


# In[3]:


dfList = [df_50, df_100, df_200, df_500, df_100, df_3000]


# In[4]:


def getData(df, column):
    '''
    Parameters:
        df(DataFrame): DataFrame.
        column(str): DataFrame's column name.

    Returns:
        columnData(list): Extracted data from the DataFrame's column.
    '''
    
    columnData = []
    
    for i in range(10):
        columnData.append(df[df['run'] == (i + 1)][column])
        
    return columnData


# In[5]:


def generateBoxPlots(subPlots, attr):
    '''
    Parameters:
        subPlots(numpy.ndarray): Array with empty subplots.
        attr(str): Column name to extract data from DataFrames.
    '''
    
    for i in range(6):
        subPlots[i].boxplot(getData(dfList[i], attr), showfliers = False, vert = False)


# In[6]:


plt.rc('xtick', labelsize = 15);
px = 1 / plt.rcParams['figure.dpi']


# In[8]:


mainPlot, subPlots = plt.subplots(6, 4, figsize = (1800*px, 1800*px), gridspec_kw = {'hspace': 0, 'wspace': .1})

(cmass_50,   aleaf_cwm_50,   awood_cwm_50,   aroot_cwm_50), (cmass_100,  aleaf_cwm_100,  awood_cwm_100,  aroot_cwm_100), (cmass_200,  aleaf_cwm_200,  awood_cwm_200,  aroot_cwm_200), (cmass_500,  aleaf_cwm_500,  awood_cwm_500,  aroot_cwm_500), (cmass_1000, aleaf_cwm_1000, awood_cwm_1000, aroot_cwm_1000), (cmass_3000, aleaf_cwm_3000, awood_cwm_3000, aroot_cwm_3000) = subPlots

subPlotsCmass    = subPlots[:, 0]
subPlotsAleafCwm = subPlots[:, 1]
subPlotsAwoodCwm = subPlots[:, 2]
subPlotsArootCwm = subPlots[:, 3]

generateBoxPlots(subPlotsCmass,    'cmass')
generateBoxPlots(subPlotsAleafCwm, 'aleaf_cwm')
generateBoxPlots(subPlotsAwoodCwm, 'awood_cwm')
generateBoxPlots(subPlotsArootCwm, 'aroot_cwm')

subPlotsCmass[0].set_title(   '(a) Total C.',        size = 15, loc = 'left')
subPlotsAleafCwm[0].set_title('(b) Leaf Alloc.',     size = 15, loc = 'left')
subPlotsAwoodCwm[0].set_title('(c) ABGW Alloc.',     size = 15, loc = 'left')
subPlotsArootCwm[0].set_title('(d) F. Roots Alloc.', size = 15, loc = 'left')

subPlotsCmass[0].set_ylabel('50 PLS',   size = 15)
subPlotsCmass[1].set_ylabel('100 PLS',  size = 15)
subPlotsCmass[2].set_ylabel('200 PLS',  size = 15)
subPlotsCmass[3].set_ylabel('500 PLS',  size = 15)
subPlotsCmass[4].set_ylabel('1000 PLS', size = 15)
subPlotsCmass[5].set_ylabel('3000 PLS', size = 15)

for subPlot in enumerate(subPlots.flat):
    subPlot[1].set_yticks([])
    
    if(subPlot[0] >= 20):
        x1, x2 = subPlot[1].get_xbound()
        subPlot[1].set_xticks(np.arange(x1, x2, ((x2 - x1) / 5)))
        subPlot[1].tick_params(labelrotation = 45)
    
    subPlot[1].label_outer()
    
mainPlot.savefig('plot-01.png', dpi = 600)


# In[9]:


mainPlot, subPlots = plt.subplots(6, 4, figsize = (1800*px, 1800*px), gridspec_kw = {'hspace': 0, 'wspace': .1})

(cmass_50, tleaf_cwm_50,   twood_cwm_50,   troot_cwm_50), (cmass_50, tleaf_cwm_100,  twood_cwm_100,  troot_cwm_100), (cmass_50, tleaf_cwm_200,  twood_cwm_200,  troot_cwm_200), (cmass_50, tleaf_cwm_500,  twood_cwm_500,  troot_cwm_500), (cmass_50, tleaf_cwm_1000, twood_cwm_1000, troot_cwm_1000), (cmass_50, tleaf_cwm_3000, twood_cwm_3000, troot_cwm_3000) = subPlots

subPlotsCmass    = subPlots[:, 0]
subPlotsTleafCwm = subPlots[:, 1]
subPlotsTwoodCwm = subPlots[:, 2]
subPlotsTrootCwm = subPlots[:, 3]

generateBoxPlots(subPlotsCmass,    'cmass')
generateBoxPlots(subPlotsTleafCwm, 'tleaf_cwm')
generateBoxPlots(subPlotsTwoodCwm, 'twood_cwm')
generateBoxPlots(subPlotsTrootCwm, 'troot_cwm')

subPlotsCmass[0].set_title(   '(a) Total C.',       size = 15, loc = 'left')
subPlotsTleafCwm[0].set_title('(d) Leaf R. T.',     size = 15, loc = 'left')
subPlotsTwoodCwm[0].set_title('(e) ABGW R. T.',     size = 15, loc = 'left')
subPlotsTrootCwm[0].set_title('(f) F. Roots R. T.', size = 15, loc = 'left')

subPlotsCmass[0].set_ylabel('50 PLS',   size = 15)
subPlotsCmass[1].set_ylabel('100 PLS',  size = 15)
subPlotsCmass[2].set_ylabel('200 PLS',  size = 15)
subPlotsCmass[3].set_ylabel('500 PLS',  size = 15)
subPlotsCmass[4].set_ylabel('1000 PLS', size = 15)
subPlotsCmass[5].set_ylabel('3000 PLS', size = 15)

for subPlot in enumerate(subPlots.flat):
    subPlot[1].set_yticks([])
    
    if(subPlot[0] >= 20):
        x1, x2 = subPlot[1].get_xbound()
        subPlot[1].set_xticks(np.arange(x1, x2, ((x2 - x1) / 5)))
        subPlot[1].tick_params(labelrotation = 45)
    
    subPlot[1].label_outer()
    
mainPlot.savefig('plot-02.png', dpi = 600)

