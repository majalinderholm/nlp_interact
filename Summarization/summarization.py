import os
import openai

#Access the API-key
key = open("Keys/key_gpt3.txt", "r")
openai.api_key = key.read()

#Open the file containing text that is about to be summarized
file = open("Summarization/prompts/example_1.txt", "r", encoding='utf-8')
example_1 = file.read()
file = open("Summarization/prompts/example_2.txt", "r", encoding='utf-8')
example_2 = file.read()
file = open("Summarization/prompts/example_3.txt", "r", encoding='utf-8')
example_3 = file.read()
file = open("Summarization/prompts/example_5.txt", "r", encoding='utf-8')
example_5 = file.read()
file = open("Summarization/prompts/prompt_4.txt", "r", encoding='utf-8')
prompt = file.read()
prompt = "Generera en sammanfattning med det viktigaste i texten \n###\n" + example_1 + "\n" + example_2 + "\n" + example_5 + "\n" + prompt + "\"\n###" #\nSammanfattning: \n###"
print(prompt)

response = openai.Completion.create(
                                    engine = "davinci-instruct-beta",
                                    prompt = prompt,
                                    temperature = 0.3,
                                    max_tokens = 400,
                                    top_p = 1.0,
                                    frequency_penalty = 0.0,
                                    presence_penalty = 0.0,
                                    stop=["###"]
                                    )

print(response.choices)