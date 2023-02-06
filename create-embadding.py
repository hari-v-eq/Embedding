import openai
import pandas as pd
from openai.embeddings_utils import get_embedding, cosine_similarity
openai.api_key ="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"

input_datapath = 'data/jj-sample-product-csv.csv'  # to save space, we provide a pre-filtered dataset
df = pd.read_csv(input_datapath)
df = df[['products']]
df = df.dropna()

# This will take just between 5 and 10 minutes(to create embedding)
df['ada_similarity'] = df.products.apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
df['ada_search'] = df.products.apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))

df.to_csv('data/jj_sample_product_csv_with_embeddings_1k.csv')