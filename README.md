# openai_sdk_wrapper

Central OpenAI API SDK wrapper for all my projects.  
Change or patch OpenAI usage in one place and import it from here.

## Usage

```python
from openai_sdk_wrapper.chat import chat_completion

response = chat_completion([
    {"role": "user", "content": "Hello, world!"}
])
print(response['choices'][0]['message']['content'])
```

In requirements.txt:

```
pip install git+https://github.com/braydio/openai_sdk_wrapper.git
```

And on updates:

```
pip install -U -e ./openai_sdk_wrapper
```
