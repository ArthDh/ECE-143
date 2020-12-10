import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import copy
import seaborn as sns
import time
import random
from sklearn.metrics import mean_squared_error as mse
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans 
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import joblib
import plotly.graph_objects as go

def FeaturePlot(features,genres,name,color):
    flag = features['predicted_genres'] == '0'
    for i in genres:
        flag = flag | (features['predicted_genres'] == i)
    target = features[flag]
    temp = target[['acousticness', 'danceability', 'energy','liveness',\
                  'loudness', 'mode','tempo', 'valence', 'instrumentalness', 'key', 'explicit','speechiness']]
    temp.mean()
    categories = ['acousticness', 'danceability', 'energy','liveness',\
                  'loudness', 'mode','tempo', 'valence', 'instrumentalness', 'key','explicit','speechiness' ]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
          r=temp.mean(),
          theta=categories,
          fill='toself',
          name=name,
          marker=dict(
                color=color
                )
    ))
    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, 1]
        )),
      showlegend=False
    )
    fig.show()

def Kmean():
    path = '../data/df_cleaned__by_artist.csv'
    df = pd.read_csv(path)
    # Data cleaning
    del df['Unnamed: 0']
    vc = df['artists'].value_counts()
    vc_gt100 = vc[vc.values >= 100].index
    df = df[df['artists'].isin(vc_gt100)]
    df = df[~df.duplicated()==1]
    # Preprocessing data
    X = copy.deepcopy(df)
    song_features = pd.DataFrame()
    scaler = MinMaxScaler() # normalizer instance
    for col in X.columns: 
        if col not in ['artists','predicted_genres']:
            scaler.fit(X[[col]])
            song_features[col] = scaler.transform(X[col].values.reshape(-1,1)).ravel() 
    # KMeans instance
    km = KMeans()
    k_rng = range(1,100)  # k value
    sse = [] # sse value for each k
    for i in k_rng:
        km = KMeans(n_clusters = i)
        km.fit(song_features.sample(1000))
        sse.append(km.inertia_) # calculating sse
    plt.plot(k_rng,sse)
    plt.xlabel('K value')
    plt.ylabel('SSE Error')
    plt.title('Best K value')
    plt.show()
    # Train for k = 10
    np.random.seed(3)
    k = 10
    km = KMeans(n_clusters=k)
    predicted_genres = km.fit_predict(song_features)
    # Adding predicted genre back to the dataset
    song_features['predicted_genres'] = predicted_genres
    song_features['predicted_genres'] = song_features['predicted_genres'].apply(lambda x: 'Genre'+ str(x))
    joblib.dump(km , '../model/km_%d_freq_artists.pkl'%k)
    song_features.head(10000).drop(labels=['predicted_genres'],axis=1).to_csv('../data/df_cleaned.tsv',sep='\t', index=False,header=False)
    ind = pd.concat([song_features['predicted_genres'].head(10000),X.reset_index()['artists'].head(10000)],axis=1)
    ind.to_csv('../data/df_cleaned_genre_10.tsv',sep='\t', index=False)
    # plot features for different genres
    FeaturePlot(song_features,['Genre6','Genre8'],'rap','green')
    FeaturePlot(song_features,['Genre1','Genre3','Genre9'],'rock','red')
    FeaturePlot(song_features,['Genre0'],'classical','blue')
    FeaturePlot(song_features,['Genre7'],'opera','darkviolet')