#----------------------------------------------
# Author: Gokul Dinesh
# Month: Oct, 2018
# Title: RecoME - Movie Recommendation Algorithm
#----------------------------------------------

import pandas as pd
import numpy as np
import math
import random

#Recommendation Algorithm based on Rating and Genre
def recommend(ratings):
    print("\n-----------------------------------------------------------------------------------------\nWe recommend:\n")
    x = []
    y = []
    z = []
    for p in range(2):
        for i in ratings:
            rating = i[1]
            rank = 0
            
            if(len(movies_genre[i[0]-1]) > 0):
                while (rating <= i[1]):
                    k = random.random()
                    k1 = math.floor(k*len(movies_genre[i[0]-1]))
                    rank = movies_genre[i[0]-1][k1]
                    rating = raw['Rating'][rank-1]
            x1 = str(raw['Title'][rank-1]) + " (" + str(raw['Year'][rank-1])+")"
            x.append(x1)
            y.append(raw['Genre'][rank-1])
            z.append(rating)
                
    reco = pd.DataFrame(np.column_stack([x, y, z]), columns=['Title', 'Genre', 'Rating'])
    reco = reco.sort_values(by='Rating', ascending=False)
    reco = reco.drop_duplicates(subset = 'Title')
    reco = reco[['Title', 'Genre']]
    
    print(reco.head().to_string(index=False))
    print("-----------------------------------------------------------------------------------------\nNew Recommendations? (y/n)")
    z = input()
    if(z == 'y' or z=='Y'):
        recommend(ratings)

#Fetching Dataset
fname = 'IMDB-Movie-Data-2006to2016.csv'
raw = pd.read_csv(fname)

genre = []

#Fetching Genres from Dataset
for i in raw['Genre']:
    k = i.split(',')
    for j in k:
        genre.append(j)
genre = list(set(genre))
genre.sort()

print('-----------------------------------------------------------------------------------------')
print('                                     RecoME!')
print('-----------------------------------------------------------------------------------------')

#Classifying the dataset based on Genre
Action = []
Adventure = []
Animation = []
Biography = []
Comedy = []
Crime = []
Drama = []
Family = []
Fantasy = []
Fiction = []
History = []
Horror = []
Musical = []
Mystery = []
Romance = []
SciFi = []
Sport = []
Thriller = []
War = []
Western = []

for i in range (len(raw)):
    for j in (raw['Genre'][i].split(',')):
        if (j=="Action"):
            Action.append(i+1)
        if (j=="Adventure"):
            Adventure.append(i+1)
        if (j=="Animation"):
            Animation.append(i+1)
        if (j=="Biography"):
            Biography.append(i+1)
        if (j=="Comedy"):
            Comedy.append(i+1)
        if (j=="Crime"):
            Crime.append(i+1)
        if (j=="Drama"):
            Drama.append(i+1)
        if (j=="Family"):
            Family.append(i+1)
        if (j=="Fantasy"):
            Fantasy.append(i+1)
        if (j=="Fiction"):
            Fiction.append(i+1)
        if (j=="History"):
            History.append(i+1)
        if (j=="Horror"):
            Horror.append(i+1)
        if (j=="Musical"):
            Musical.append(i+1)
        if (j=="Mystery"):
            Mystery.append(i+1)
        if (j=="Romance"):
            Romance.append(i+1)
        if (j=="Sci-Fi"):
            SciFi.append(i+1)
        if (j=="Sport"):
            Sport.append(i+1)
        if (j=="Thriller"):
            Thriller.append(i+1)
        if (j=="War"):
            War.append(i+1)
        if (j=="Western"):
            Western.append(i+1)
            
movies_genre = [Action,Adventure,Animation,Biography,Comedy,Crime,Drama,Family,Fantasy,Fiction,History,Horror,Musical,Mystery,Romance,SciFi,Sport,Thriller,War,Western]

print ("\nPlease input the numbers corresponding to your 5 favourite genres:")
for i in range(len(genre)):
    print("[",i+1,"]\t",genre[i])

fav_genres = []
c = 0
while (c<5):
    x = input()
    if (x != ''):
        try:
            x = (int)(x)
            if (x>=1 and x<=20):
                if (x not in fav_genres):
                    fav_genres.append(x)
                    c = c+1
                else:
                   print('Genre already added') 
            else:
                print('Invalid input')
        except:
            print('Invalid input')
    else:
        print('Invalid input')

print ("\nPlease rate the following movies on 10: (0 or skip for Not Watched)")

user_rating = []
temp1 = []
for i in range (5):
    if (len(movies_genre[fav_genres[i]-1]) > 0):
        for j in range (3):
            k = random.random()
            temp1.append(movies_genre[fav_genres[i]-1][math.floor(k*len(movies_genre[fav_genres[i]-1]))]-1)

temp1 = list(set(temp1))
i=0
while (i < len(temp1)):
    print (str(raw['Title'][temp1[i]])+" ("+str(raw['Year'][temp1[i]])+")")
    x = input()
    if (x != '' and x != '0'):
        try:
            x = (int)(x)
            if (x>=1 and x<=10):
                user_rating.append([temp1[i], x])
            else:
                flag = True
                while (flag):
                    print("Invalid input. Please rate again. (0 or skip for Not Watched)")
                    x = input()
                    if (x != '' and x != '0'):
                        x = (int)(x)
                        if (x>=1 and x<=10):
                            user_rating.append([temp1[i], x])
                            flag = False
                    else:
                        flag = False
        except:
            print("Invalid input. Please rate again. (0 or skip for Not Watched)")
            i = i-1
    i = i+1
usr_rank = []
usr_genre = []

##### Fetching user's rating and analysing the mean rating per genre
if (user_rating != []):
    usr_rank=[]
    temp2 = pd.DataFrame(columns=['Genre','Rating'])
    for i in user_rating:
        if (i[1] >= raw['Rating'][i[0]-1]):
            x = raw['Genre'][i[0]-1].split(',')
            y = raw['Rating'][i[0]-1]
            for j in x:
                usr_rank.append([j,y])
                usr_genre.append(j)
    temp2 = pd.DataFrame(usr_rank,columns=['Genre','Rating'])
    
    if (len(temp2) == 0):
        for i in fav_genres:
            usr_rank.append([genre[i-1],7])
            usr_genre.append(genre[i-1])
        temp2 = pd.DataFrame(usr_rank,columns=['Genre','Rating'])

    usr_mean = temp2.groupby('Genre')['Rating'].mean().values
    usr_genre = list(set(usr_genre))
    
    x_genre = []
    print('-----------------------------------------------------------------------------------------')
    for i in usr_genre:
        for j in range(len(genre)):
            if (genre[j] == i):
                x_genre.append(j+1)
    
    usr_rank=[]
    for i in range(len(usr_mean)):
        usr_rank.append([x_genre[i],usr_mean[i]])
        
    recommend(usr_rank)   