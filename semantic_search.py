import pandas as pd
import numpy as np
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity

openai.api_key ="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"


datafile_path="https://cdn.openai.com/API/examples/data/fine_food_reviews_with_embeddings_1k.csv"
df=pd.read_csv(datafile_path)
df.head

#print(df)

#print(type(df.loc[0]['Translated_Review']))

df['Sentiment_Polarity']=df.Sentiment_Polarity.apply(eval).apply(np.array)
#print(type(df.loc[0]['Sentiment_Polarity']))


def search_reviews(df, search_query, n=3):
    embedding = get_embedding(
        search_query,
        engine="text-search-babbage-query-001"
    )
   
    df["similarities"] = df.Sentiment_Polarity.apply(lambda x: cosine_similarity(x, embedding))

    top_n =df.sort_values("similarities", ascending=False).head(n)
    # res = top_n.combined.str.replace("Title: ", "").str.replace("; Content:", ": ")
    return top_n

res=search_reviews(df, "great", n=3)
var = res["Sentiment_Polarity"].to_list()

print(var)