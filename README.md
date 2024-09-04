# Document Summarizer

[![](https://github.com/abizermamnoon/docsum/workflows/tests/badge.svg)](https://github.com/abizermamnoon/docsum/actions?query=workflow%3Atests)

`docsum.py` is a simple Python script that extracts text from a file, summarizes it using the Groq API, and prints the summary at a first-grade reading level.

## Features

- **Text Extraction**: Extracts text from various file formats using the `fulltext` library.
- **Text Summarization**: Summarizes the extracted text using the Groq API and outputs the summary.
- **First-Grade Reading Level**: Summaries are simplified to a first-grade reading level.

## Setup

Create a python virtual environment for packages.
```
$ python3 -m venv venv
$ . ./venv/bin/activate
$ echo venv > .gitignore
```

Install packages.
```
$ pip3 install groq fulltext
$ pip3 freeze > requirements.txt
``` 

Create a .env file and add your GROQ_API_KEY
```
GROQ_API_KEY=your_api_key_here
```

## Usage

```
$ python3 docsum.py <file_path>
```

For example:
```
$ python3 docsum.py docs/'Abizer Mamnoon Resume.pdf'
```

```
Here is a summary of the text in one paragraph, written at a 1st-grade reading level:

Abizer is a student at Claremont McKenna College who is very smart in computer science and economics. He has worked on many projects and helped write articles about important topics like economics. Abizer is good at coding languages like Python and R, and he has even built big data models to help people make better decisions. He is also good at designing things like websites and chatbots. Abizer likes to learn new things and build new projects, and he is very good at what he does.
```

