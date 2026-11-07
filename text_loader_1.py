"""
Document (
          page_content = 'The actual text content.' , 
          metadata = {'source' : 'filename.pdf' , ......}
)
"""

from langchain_community.document_loaders import TextLoader

loader = TextLoader('cricket.txt' , encoding = 'utf-8')

# To load document in the memory
docs = loader.load()

print(docs) # Type of docs will be a list. 

print(docs[0]) # To get the content of txt

print(docs[0].page_content)

print(docs[0].metadata)



