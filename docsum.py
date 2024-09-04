def split_document_into_chunks(text, chunk_size=512):
    r"""
    Split text into smaller chunks so an LLM can process those chunks individually.

    Args:
        text (str): The input text to split into chunks.
        chunk_size (int): The maximum size of each chunk in terms of characters.

    Returns:
        List[str]: A list of text chunks.

    Examples:
    >>> split_document_into_chunks('This is a sentence.\\n\\nThis is another paragraph.')
    ['This is a sentence.', 'This is another paragraph.']
    
    >>> split_document_into_chunks('This is a very long sentence that goes on and on and needs to be split into chunks. ' * 10, chunk_size=100)
    ['This is a very long sentence that goes on and on and needs to be split into chunks. This is a very long ', 'sentence that goes on and on and needs to be split into chunks. This is a very long sentence that goes on ']
    
    >>> split_document_into_chunks('Short text.')
    ['Short text.']
    
    >>> split_document_into_chunks('First part.\\n\\nSecond part.\\n\\nThird part.')
    ['First part.', 'Second part.', 'Third part.']
    """
    # Split the text by paragraphs (assuming paragraphs are separated by double newlines)
    paragraphs = text.split('\n\n')
    
    # Further split paragraphs into smaller chunks if they exceed the chunk size
    chunks = []
    for paragraph in paragraphs:
        start = 0
        while start < len(paragraph):
            chunks.append(paragraph[start:start + chunk_size].strip())
            start += chunk_size

    return chunks


import os
from groq import Groq
#from dotenv import load_dotenv
import argparse
import fulltext
#filename = 'docs/declaration'
#with open(args.filename) as f:
#    text = f.read()
# Load environment variables from .env file
# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# Use fulltext to extract text from the file
text = fulltext.get(args.filename)
#print(os.environ.get("GROQ_API_KEY"))
# Initialize Groq client with API key
client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "summarize input text below. limit summary to 1 paragraph and use a 1st grade reading level",
        },
        {
            "role": "user",
            "content":text, 
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)

