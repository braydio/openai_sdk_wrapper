# openai_sdk_wrapper

Central OpenAI API SDK wrapper for all your projects.  
Change or patch OpenAI usage in one place.

## Usage

```python
from openai_sdk_wrapper.chat import chat_completion

response = chat_completion([
    {"role": "user", "content": "Hello, world!"}
])
print(response['choices'][0]['message']['content'])
```
