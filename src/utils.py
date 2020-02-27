import os

import numpy as np
import pandas as pd

# Paths to text files
ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT_DIR, 'data')
DATA_PATH = os.path.join(DATA_DIR, 'data.txt')
TRAIN_DATA_PATH = os.path.join(DATA_DIR, 'train.txt')
TEST_DATA_PATH = os.path.join(DATA_DIR, 'test.txt')
MOVIES_PATH = os.path.join(DATA_DIR, 'movies.txt')

PLOTS_DIR = os.path.join(ROOT_DIR, 'plots')

# Text file columns
MOVIES_COLUMNS = [
    'movie_id',
    'title',
    'unknown',
    'action',
    'adventure',
    'animation',
    'childrens',
    'comedy',
    'crime',
    'documentary',
    'drama',
    'fantasy',
    'film_noir',
    'horror',
    'musical',
    'mystery',
    'romance',
    'sci_fi',
    'thriller',
    'war',
    'western'
]
DATA_COLUMNS = ['user_id', 'movie_id', 'rating']

def reindex(df, columns=['user_id', 'movie_id']):
    df = df.copy()
    for col in columns:
        if col in df:
            df[col] -= 1
    return df

def load_data():
    """Load the entire (train + test) dataset as a Pandas DataFrame."""
    df = pd.read_csv(DATA_PATH, names=DATA_COLUMNS, delimiter='\t')
    return reindex(df)

def load_train_data():
    """Load the train dataset as a Pandas DataFrame."""
    df = pd.read_csv(TRAIN_DATA_PATH, names=DATA_COLUMNS, delimiter='\t')
    return reindex(df)

def load_test_data():
    """Load the test dataset as a Pandas DataFrame."""
    df = pd.read_csv(TEST_DATA_PATH, names=DATA_COLUMNS, delimiter='\t')
    return reindex(df)

def load_movies():
    """Load the movie info as a Pandas DataFrame."""
    df = pd.read_csv(MOVIES_PATH, names=MOVIES_COLUMNS, delimiter='\t')
    return reindex(df)

def add_missing_ratings(df, movie_ids, user_id=None):
    """"Add a single rating of 2.5 to all movies with no ratings in the
    given dataframe. The rating is made by the provided user id or the next
    user id."""
    user_id = user_id if user_id is not None else np.max(df.user_id) + 1
    missing = set(movie_ids) - set(df.movie_id.values)

    df_add = pd.DataFrame(
        [[user_id, movie_id, 2.5] for movie_id in missing],
        columns=df.columns
    )
    return pd.concat((df, df_add))

def save_fig(fig, name):
    fig.savefig(os.path.join(PLOTS_DIR, name), dpi=300, bbox_inches='tight')
