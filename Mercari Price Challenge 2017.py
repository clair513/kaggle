# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 07:36:58 2017
Data Source: https://www.kaggle.com/c/mercari-price-suggestion-challenge/data
Purpose: Predict product Selling Price
Data Fields: The files (train.tsv & test.tsv) consist of a list of product listings. These files are tab-delimited.

train_id or test_id: The id of the listing
name: the title of the listing.
item_condition_id: Condition of the items provided by the seller
category_name: Category of the listing
brand_name
price - Price (USD) that the item was sold for. This is the target variable to predict.
shipping: 1 if shipping fee is paid by seller and 0 by buyer
item_description: Full description of the item.

@author: Alok Kumar
"""

# Importing Libraries:
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline

# Reading Data Files:

train = pd.read_csv('train.tsv/train.tsv', sep = '\t')
test = pd.read_csv('test.tsv/test.tsv', sep = '\t')

# Analyzing Training Dataset:

train.head()
train.dtypes
train = train.rename(columns = {'train_id':'id'})
train.apply(lambda x: x.nunique())
train.isnull().sum(),train.isnull().sum()/train.shape[0]

test.head()
test.dtypes
test = test.rename(columns = {'test_id':'id'})
test.apply(lambda x: x.nunique())
test.isnull().sum(),train.isnull().sum()/train.shape[0]
"""
print("There are",len(train.brand_name.unique()),"brand names")
print("There are",len(train.category_name.unique()),"categories")
train.item_condition_id.unique()

def display_all(df):
    with pd.option_context("display.max_rows", 1000):
        with pd.option_context("display.max_columns", 1000):
            display(df)

display_all(train.describe(include='all').transpose())

# Visualizing Dataset (Trying to find Top20 selling categories & their proportion in entire training data provided. Then we shall shift focus on Top20 selling Brands.)

f,ax = plt.subplots(1, 1, figsize=(15,20))
hist = train.groupby(['category_name'], as_index=False).count().sort_values(by='id', ascending=False)[0:25]
sns.barplot(y=hist['category_name'], x=hist['id'], orient='h')
matplotlib.rcParams.update({'font.size': 22})
plt.show()

hist['id'].values[0]/np.sum(hist['id'].values[1:])

labels = hist['category_name'].values[0], hist['category_name'].values[1], hist['category_name'].values[2], hist['category_name'].values[3], 'Others'
sizes = [hist['id'].values[0], hist['id'].values[1], hist['id'].values[2], hist['id'].values[3],np.sum(hist['id'].values[4:])]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','brown']
explode = (0.1, 0, 0, 0, 0)  # Exploding 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

f,ax = plt.subplots(1, 1, figsize=(15,20))
hist = train.groupby(['brand_name'], as_index=False).count().sort_values(by='id', ascending=False)[0:25]
sns.barplot(y=hist['brand_name'],x=hist['id'], orient='h')
matplotlib.rcParams.update({'font.size': 22})
plt.show()
"""
# Cleaning Dataset (Combining train & test dataset to normalize & then segregate):

train['is_train'] = 1
test['is_train'] = 0

train_test_combine = pd.concat([train.drop(['price'],axis =1),test],axis = 0)

train_test_combine.category_name = train_test_combine.category_name.astype('category')
train_test_combine.item_description = train_test_combine.item_description.astype('category')

train_test_combine.name = train_test_combine.name.astype('category')
train_test_combine.brand_name = train_test_combine.brand_name.astype('category')

train_test_combine.name = train_test_combine.name.cat.codes
train_test_combine.category_name = train_test_combine.category_name.cat.codes

train_test_combine.brand_name = train_test_combine.brand_name.cat.codes
train_test_combine.item_description = train_test_combine.item_description.cat.codes

train_test_combine.head()
train_test_combine.dtypes

df_train = train_test_combine.loc[train_test_combine['is_train']==1]
df_test = train_test_combine.loc[train_test_combine['is_train']==0]

df_train = df_train.drop(['is_train'],axis=1)
df_test = df_test.drop(['is_train'],axis=1)
df_train['price'] = train.price
df_train['price'] = df_train['price'].apply(lambda x: np.log(x) if x>0 else x)

df_train.head()  # Checking my resultant training dataset
df_train_wid = df_train.iloc[:, 1:]
df_train_wid = df_train_wid.dropna()

df_test_wid = df_test.iloc[:, 1:]

# Splitting Dataset:

X = df_train_wid.drop('price', axis=1)
y = df_train_wid['price']

# Building Model (Neural net regressor with Keras on top of TensorFlow):

def regressor_model():  #Keras wrapper always requires function as an argument so creating this function.
	# Creating my model:
    model = Sequential()
    model.add(Dense(20, input_dim=6, init='uniform', activation='relu'))
    model.add(Dense(20, init='uniform', activation='relu'))
    model.add(Dense(20, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform'))
	# Compiling my model:
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
    return model

# Setting Random seed, epochs, etc. & then evaluating model:


seed = 4
np.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn= regressor_model, epochs=100, batch_size=20000, verbose=1)))
pipeline = Pipeline(estimators)
"""
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, y, cv= kfold)
print("Standardized: %.2f (%.2f) MSE" % (results.mean(), results.std()))
"""
# Predicting Selling Price of Products in Test set:

pipeline.fit(X, y)
pred = pipeline.predict(df_test_wid)

submission = pd.DataFrame(data= test['id'], index=None)
submission['price'] = pred
submission.columns = ['test_id','price']
submission.to_csv('mps_submission1.csv', index=False)
