import pandas as pd
import numpy as np
import math
import random

def recommend(a):
    print("\n-----------------------------------------------------------------------------------------\nWe recommend:\n")
    x = []
    y = []
    z = []
    for p in range(2):
        for i in a:
            rating = i[1]
            rank = 0
            while (rating <= i[1]):
                k = random.random()
                rating = raw['Rating'][movies_genre[i[0]-1][math.floor(k*len(movies_genre[i[0]-1]))]-1]
                rank = movies_genre[i[0]-1][math.floor(k*len(movies_genre[i[0]-1]))]
                x.append(raw['Title'][movies_genre[i[0]-1][math.floor(k*len(movies_genre[i[0]-1]))]-1])
                y.append(raw['Genre'][movies_genre[i[0]-1][math.floor(k*len(movies_genre[i[0]-1]))]-1])
                z.append(raw['Rating'][movies_genre[i[0]-1][math.floor(k*len(movies_genre[i[0]-1]))]-1])
    reco = pd.DataFrame(np.column_stack([x, y, z]), columns=['Title', 'Genre', 'Rating'])
    reco = reco.sort_values(by='Rating', ascending=False)
    reco = reco.drop_duplicates(subset = 'Title')
    reco = reco[['Title', 'Genre']]
    print(reco.head().to_string(index=False))
            #print(raw['Title'][movies_genre[i[0]-1][math.floor(k*len(movies_genre[i[0]-1]))]-1], '   [ Genre: ', raw['Genre'][movies_genre[i[0]-1][math.floor(k*len(movies_genre[i[0]-1]))]-1], '   IMDb Rating:', raw['Rating'][movies_genre[i[0]-1][math.floor(k*len(movies_genre[i[0]-1]))]-1],']')
    print("-----------------------------------------------------------------------------------------\nNew Recommendations? (y/n)")
    z = input()
    if(z == 'y' or z=='Y'):
        recommend(a)

fname = 'IMDB-Movie-Data-2006to2016.csv'

raw = pd.read_csv(fname)

genre = ["Action","Adventure","Animation","Biography","Comedy","Crime","Drama","Family","Fantasy","Fiction","History","Horror","Musical","Mystery","Romance","Sci-Fi","Sport","Thriller","War","Western"]

print('-----------------------------------------------------------------------------------------')
print('                                     RecoME!')
print('-----------------------------------------------------------------------------------------')

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

print ("\nPlease input the numbers corresponding to your 5 favourite genres: \n[1]\tAction\n[2]\tAdventure\n[3]\tAnimation\n[4]\tBiography\n[5]\tComedy\n[6]\tCrime\n[7]\tDrama\n[8]\tFamily\n[9]\tFantasy\n[10]\tFiction\n[11]\tHistory\n[12]\tHorror\n[13]\tMusical\n[14]\tMystery\n[15]\tRomance\n[16]\tSci-Fi\n[17]\tSport\n[18]\tThriller\n[19]\tWar\n[20]\tWestern")

fav_genres = []
for i in range (5):
    fav_genres.append(int(input()))

print ("\nPlease rate the following movies on 10: (0 or skip for Not Watched)\n")

user_rating = []
for i in range (5):
    for j in range (3):
        k = random.random();
        print(raw['Title'][movies_genre[fav_genres[i]-1][math.floor(k*len(movies_genre[fav_genres[i]-1]))]-1])
        x = input()
        if (x != ''):
            x = (int)(x);
            if (x>=1 and x<=10):
                user_rating.append([movies_genre[fav_genres[i]-1][math.floor(k*len(movies_genre[fav_genres[i]-1]))], x])

a = []
n = []

if (user_rating != []):
        a=[]
        b = pd.DataFrame(columns=['Genre','Rating'])
        for i in user_rating:
            if (i[1] >= raw['Rating'][i[0]-1]):
                x = raw['Genre'][i[0]-1].split(',')
                y = raw['Rating'][i[0]-1]
                for j in x:
                    a.append([j,y])
                    n.append(j)
        b = pd.DataFrame(a,columns=['Genre','Rating'])

        if (len(b) == 0):
            for i in fav_genres:
                a.append([genre[i-1],7])
                n.append(genre[i-1])
            b = pd.DataFrame(a,columns=['Genre','Rating'])

        g = b.groupby('Genre')['Rating'].mean().values
        n = list(set(n))
        x_genre = []
        #print (len(g))
        #print(n)
        print('-----------------------------------------------------------------------------------------')
        for i in n:
            for j in range(len(genre)):
                if (genre[j] == i):
                    x_genre.append(j+1)
        a=[]
        #print(len(x_genre))
        #print(x_genre)
        for i in range(len(g)):
            a.append([x_genre[i],g[i]])
        recommend(a)