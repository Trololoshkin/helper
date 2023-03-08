import openai
import os

openai.api_key = os.environ["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"]

# Теперь можно использовать OpenAI API, например:
response = openai.Completion.create(
    engine="davinci",
    prompt="Какой самый высокий город в мире?",
    max_tokens=5,
    n=1,
    stop=None,
    temperature=0.5,
)

print(response.choices[0].text)
