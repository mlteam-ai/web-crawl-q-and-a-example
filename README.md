# Web  Q&A with Embeddings

Learn how to crawl your website and build a Q/A bot with the OpenAI API. You can find the full tutorial in the [OpenAI documentation](https://platform.openai.com/docs/tutorials/web-qa-embeddings). However official tutorial is not up-to-date and compatible with Ptyhon 3.12.1 and latest [openai python library](https://github.com/openai/openai-python) 1.9.0 (as of 21 January 2024).

# Overview
This tutorial walks through a simple example of crawling a website (in this example, the OpenAI website), turning the crawled pages into embeddings using the Embeddings API, and then creating a basic search functionality that allows a user to ask questions about the embedded information. This is intended to be a starting point for more sophisticated applications that make use of custom knowledge bases.

# Installation
This project is tested in Python 3.12.1 and openai python library 1.9.0.

## 1. Setting up the '.env' file
You need to subscribe to [OpenAI](https://platform.openai.com/docs/quickstart/account-setup), configure your [billing settings](https://platform.openai.com/account/billing/overview), get your API key and create an '.env' file containing 'OPENAI_API_KEY'.

Here is a sample '.env' file:
```
OPENAI_API_KEY=12345
```

## 2. Installing the dependencies
Open a terminal window, change your working directory to [web-crawl-q-and-a](.), run the following commands. This will create and activate a virtual environment and install all the dependencies into it.
```sh
    chmod +x setup.sh
    ./setup.sh
```

# Execution
To start the application run the following command in [web-crawl-q-and-a](.) folder.
```sh
    python3 main.py
```
