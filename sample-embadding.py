import openai
import pandas as pd
import numpy as np

from openai.embeddings_utils import get_embedding, cosine_similarity


openai.api_key ="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"

# If you have not run the "Obtain_dataset.ipynb" notebook, you can download the datafile from here: https://cdn.openai.com/API/examples/data/fine_food_reviews_with_embeddings_1k.csv
datafile_path = "data/fine_food_reviews_with_embeddings_1k.csv"

df = pd.read_csv(datafile_path)
df["babbage_search"] = df.babbage_search.apply(eval).apply(np.array)

# search through the reviews for a specific product
def search_reviews(df, product_description, n=3, pprint=True):
    embedding = get_embedding(
        product_description,
        engine="text-search-babbage-query-001"
    )
    
    df["search"] = df.babbage_search.apply(lambda x: cosine_similarity(x, embedding))

    res = (
        df.sort_values("search", ascending=False)
        .head(n)
        .combined.str.replace("Title: ", "")
        .str.replace("; Content:", ": ")
    )
    if pprint:
        for r in res:
            print(r[:200])
            print()
    return res


res = search_reviews(df, "delicious beans", n=3)