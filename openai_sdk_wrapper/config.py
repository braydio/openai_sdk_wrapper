import os


def get_api_key():
    # central place to update API key logic
    return os.getenv("OPENAI_API_KEY")
