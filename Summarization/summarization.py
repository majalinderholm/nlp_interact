import os
import openai

#Access the API-key
key = open("Keys/key_gpt3.txt", "r")
openai.api_key = key.read()

#Open the file containing text that is about to be summarized
file = open("Summarization/prompt.txt", "r")
prompt = file.read()
print(prompt)

response = openai.Completion.create(
                                    engine = "davinci",
                                    prompt = prompt,
                                    temperature = 0,
                                    max_tokens = 200,
                                    top_p = 1.0,
                                    frequency_penalty = 0.0,
                                    presence_penalty = 0.0,
                                    stop=["###"]
                                    )

print(response.choices)