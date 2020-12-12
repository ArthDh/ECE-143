# MR. HyPE: Music Recommendation <br> based on Hyper-dimensional Python Embedding

ECE143 Group 20

## Installation

Requires python 3.3+

Some main third-party modules:

pandas 1.1.4

sklearn 0.0

plotly 4.13.0

spotipy 2.16.1

Clone the repository using
```
git clone https://github.com/ArthDh/ECE-143/
```

Create a python virtual environment
```python
python -m venv env
```
Activate the environment
```
source  env/bin/activate
```

Install dependencies
```
pip install requirements.txt
```

Deactivate when done making changes
```
deactivate
```

## Usage

All the data we used and generated are stored in [data](https://github.com/ArthDh/ECE-143/tree/main/data) folder, and the clustering model we generated are stored in [model](https://github.com/ArthDh/ECE-143/tree/main/model) folder.

### Data Visualization

Visualizations of the correlation between raw features from dataset are presented in final notebook in [notebooks](https://github.com/ArthDh/ECE-143/tree/main/notebooks) folder.

### Clustering

We used K-mean for clustering and all visualizations regarding K-mean are also showed in final notebook. The original data used for hyper dimensional visualization are stoed in [data](https://github.com/ArthDh/ECE-143/tree/main/data) folder, named df_cleaned.tsv and df_cleaned_genre_10.tsv.

### Hyper Dimensional Visualization

PCA

![PCA](https://github.com/ArthDh/ECE-143/blob/main/images/PCA.gif)

UMAP

![UMAP](https://github.com/ArthDh/ECE-143/blob/main/images/UMAP.gif)

In order to see the 3D visualization of the dataset with predicted genres and artist names as index, use the following link:
https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/ArthDh/804b7297af76e5d0e626c8c01af2d158/raw/0d0c110e2ca731df7a63dcc7e8e0370d9dd29dd0/projector_config.json

### Artist Recommendation

Go to the final notebook, change the sample name to your favorite artist and change the lim to the length of the recommendation list you want, and run the notebook.
