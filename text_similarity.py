import pandas as pd
import openai, numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity


openai.api_key ="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"

"----------------Text similarity---------------"

resp=openai.Embedding.create(
    input=["eating food", "i am hungry", "i am travelling", "exploring new places", "i am happy"],
    engine="text-similarity-davinci-001")

#print(type(resp['data']))    #type of the response

#print(len(resp['data']))      #length of the list

#print(type(resp['data'][0]))     #type of openai object

#print(resp['data'][0].keys())     #output=dict_keys(['object', 'index', 'embedding'])

#print(resp['data'][0]["embedding"])      #print the embedded data i.e 0.04153420403599739, 0.00906651932746172, 0.00694781681522727, -0.0020741650369018316, 

embedding_a=resp['data'][0]["embedding"]
embedding_b=resp['data'][1]["embedding"]
embedding_c=resp['data'][2]["embedding"]
embedding_d=resp['data'][3]["embedding"]
embedding_e=resp['data'][4]["embedding"]
#print(embedding_a)

match1=np.dot(embedding_a,embedding_b)         #it will show the match% of the 2 lists
match2=np.dot(embedding_a,embedding_c)  
match3=np.dot(embedding_c,embedding_d)          
print(match2)




