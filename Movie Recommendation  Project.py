#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Import required Libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as pls
import re
import sklearn
import nltk
from sklearn.metrics.pairwise import cosine_similarity


# In[20]:


# Read csv file
df = pd.read_csv("movies.csv")


# In[21]:


# Visualising first five rows of dataframe
df.head()


# In[22]:


# check the size of the dataframe 
df.shape


# In[23]:


# information of dataframe
df.info()


# In[24]:


# Replace null values in the following selected features
selected_features = [ "genres", "keywords", "tagline", "cast", "director"]
for feature in selected_features:
    df[feature] = df[feature].fillna("")
    


# In[25]:


df["genres"].value_counts()


# In[26]:


# Combining all the features in the selected feaqtures
combined_feature = ""
for feature in selected_features:
    combined_feature= combined_feature + " " +df[feature]


# In[27]:


# print Combined features
print(combined_feature)


# In[28]:


# Vectorization using TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_feature)
print(feature_vectors)


# In[29]:


# Getting similarity score
#from sklearn.metrics.pairwise import cosine_similarity
Similarity = cosine_similarity(feature_vectors)


# In[30]:


print(Similarity)


# In[39]:


# User Input
# getting miovie name
movie_name = input("Enter your fav movie\n")


# In[40]:


# creating a list with all the movies name given in the data set
list_of_titles = df["title"].tolist()
print(len(list_of_titles))
print(list_of_titles)


# In[41]:


# finding close match
import difflib
close_match = difflib.get_close_matches(movie_name, list_of_titles)


# In[42]:


# Printing close match
print(close_match)


# In[43]:


# finding the index of the first movie in the close match
index_of_the_movie = df[df.title ==close_match[0]]["index"].values[0]
print(index_of_the_movie)


# In[44]:


# getting list of similar movies
similarity_score = list(enumerate(Similarity[index_of_the_movie]))
print(similarity_score)


# In[59]:


# sorting in order from higher similarity to lower
similarity_score.sort( key= lambda x : x[1], reverse= True)
print((similarity_score))


# In[55]:


# list of top 10 recomonded movies
i=1
while i <=10:
        print(df["title"].iloc[similarity_score[i][0]])
        i+=1


# ## Complete code to recommond movies

# In[58]:



Movie = input("Enter your fav movie or genre\n")
Genres = ["action", "Action", "Drama", "drama", "Love", "love", "Comedy", "comedy", "Horror", "horror", "adventure", "Adventure", "Fantasy", "fantasy", "Roamnce", "romance","Crime", "crime", "Thriller", "thriller", "Science fiction", "Science Fiction", "science fiction", "Musical", "musical", "Documentary", "documentary", "War", "war", "Biographical", "Biography", "biographical", "biography", "Sports", "sports", "Art", "art", "childrensfilm", "chindren film", "Childrens film", "Chindren film"]

i = 0
while i <1:
    if Movie in Genres:
        T = 1
        break
    else:
        T = 0 
        break
    
if T == 1:
    list_of_genres = df["genres"].tolist()
    
    Close_Match = difflib.get_close_matches(Movie, list_of_genres)
    print(Close_match)
    Index_of_the_movie = df[df.genres ==Close_match[0]]["index"].values[0]
    Similarity = cosine_similarity(feature_vectors)
    Similarity_score = list(enumerate(Similarity[Index_of_the_movie]))
    Similarity_score.sort( key= lambda x : x[1], reverse= True)
    print("")
    print("Hey!, Movies That you can watch. Enjoy watching🥰 ")
    print("---------------------------------------------------")
    i =1 
    while i <=10:
        print(df["title"].iloc[Similarity_score[i][0]])
        i+=1
    
else :
    Close_match = difflib.get_close_matches(Movie, list_of_titles)
    print(Close_match)
    Index_of_the_movie = df[df.title ==Close_match[0]]["index"].values[0]
    Similarity = cosine_similarity(feature_vectors)
    Similarity_score = list(enumerate(Similarity[Index_of_the_movie]))
    Similarity_score.sort( key= lambda x : x[1], reverse= True)
    print("")
    print("Hey!, Movies That you can watch. Enjoy watching🥰 ")
    print("---------------------------------------------------")
    i =1 
    while i <=10:
        print(df["title"].iloc[Similarity_score[i][0]])
        i+=1

