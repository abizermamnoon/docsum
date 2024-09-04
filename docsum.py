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

