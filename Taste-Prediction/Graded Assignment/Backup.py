import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv(r"Book1.csv")
df['Momo'].head()
