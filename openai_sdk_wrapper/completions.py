import openai
from .config import get_api_key


def completion(prompt, model="gpt-3.5-turbo-instruct", **kwargs):
    openai.api_key = get_api_key()
    return openai.Completion.create(model=model, prompt=prompt, **kwargs)
