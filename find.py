# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os

question = input("Please enter a question: ")  # Python 3


os.environ['OPENAI_API_KEY'] = ''

# Loading from a directory
documents = SimpleDirectoryReader('wiki').load_data()

# Construct a simple vector index
index = GPTSimpleVectorIndex(documents)

# Save your index to a index.json file
index.save_to_disk('index.json')
# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Querying the index
response = index.query(question)
print(response)