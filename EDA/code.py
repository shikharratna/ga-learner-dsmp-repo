# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(path)


data=data[data['Rating']<=5]
#Code starts here


#Code ends here


# --------------
# code starts here


# code ends here
total_null=(data.isnull().sum())
total_null=pd.Series(total_null)
percent_null=(total_null/data.isnull().count())
percent_null=pd.Series(percent_null)
missing_data=pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
data=data.dropna()



total_null_1=data.isnull().sum()
total_null_1=pd.Series(total_null_1)

percent_null_1=total_null_1/data.isnull().count()
percent_null_1=pd.Series(percent_null_1)
missing_data_1=pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])






# --------------

#Code starts here


sns.catplot(x='Category',y='Rating',data=data,kind='box',height=10)


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
data['Installs']=data['Installs'].str.replace('+','')
data['Installs']=data['Installs'].str.replace(',','')

data['Installs']=data['Installs'].astype('int64')


le=LabelEncoder()
data['Installs']=le.fit_transform(data['Installs'])
sns.regplot(x='Installs',y='Rating',data=data)
print(data['Installs'])
#Code ends here



# --------------
#Code starts here

data.Price.value_counts()
data['Price']=data.Price.str.replace('$','')

data['Price']=data.Price.astype(float)

#Code ends here


# --------------

#Code starts here

data.Genres.unique()
data['Genres']=data['Genres'].str.split(";",n=1,expand=True)

gr_mean= data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

gr_mean.describe()

gr_mean=gr_mean.sort_values(by=['Rating'])
#Code ends here


# --------------

#Code starts here

#Series Containing Dates
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date=data['Last Updated'].max()
data['Last Updated Days']=max_date-data['Last Updated']
data['Last Updated Days']=data['Last Updated Days'].dt.days

sns.regplot(x="Last Updated Days",y='Rating',data=data)

#Code ends here


