import openai
from .config import get_api_key


def chat_completion(messages, model="gpt-4o", **kwargs):
    openai.api_key = get_api_key()
    return openai.ChatCompletion.create(model=model, messages=messages, **kwargs)
