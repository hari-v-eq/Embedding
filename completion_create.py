import openai
import os

# openai.api_key =os.getenv("OPENAI_API_KEY")


def gpt3(stext):
    openai.api_key ="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"
    response=openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=stext,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
    content=response.choices[0].text.split('.')
    # print(content)
    return response.choices[0].text

query="shopify cart data retrive"
response=gpt3(query)
print(response)



