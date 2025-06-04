# setup.py
from setuptools import setup, find_packages

setup(
    name="openai_sdk_wrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A wrapper for OpenAI API to centralize and simplify usage.",
    url="https://github.com/braydio/openai_sdk_wrapper",
)
