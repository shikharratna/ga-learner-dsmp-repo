# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
#path of the data file- path

#Code starts here 
data.Gender.replace('-','Agender',inplace=True)
gender_count=data.Gender.value_counts()
gender_count.plot(kind='bar')



# --------------
#Code starts here
alignment=data.Alignment.value_counts()
alignment.plot(kind='pie')


# --------------
#Code starts here
sc_df=pd.DataFrame(data,columns=['Strength','Combat'])
sc_covariance=sc_df.cov()
sc_strength=sc_df.Strength.std()
sc_combat=sc_df.Combat.std()
sc_pearson=sc_df.corr(method='pearson',min_periods=1)
sc_pearson=sc_pearson.Combat[0]
sc_covariance=sc_covariance.Combat[0]



ic_df=pd.DataFrame(data,columns=['Intelligence','Combat'])
ic_covariance=ic_df.cov()
ic_intelligence=ic_df.Intelligence.std()
ic_combat=ic_df.Combat.std()
ic_pearson=ic_df.corr(method='pearson',min_periods=1)
ic_pearson=ic_pearson.Combat[0]
ic_covariance=ic_covariance.Combat[0]


# --------------
#Code starts here


total_high=data.Total.quantile(q=.99)


super_best=data[data.Total>total_high]
super_best_names=list(super_best.Name[:])
print(super_best_names)


# --------------
#Code starts here

fig,(ax_1,ax_2,ax_3)=plt.subplots(1,3,figsize=(20,8))

data.Intelligence.plot(kind='box',ax=ax_1)
data.Speed.plot(kind='box',ax=ax_2)
data.Power.plot(kind='box',ax=ax_3)
ax_1.set_title=('Intelligence1')


