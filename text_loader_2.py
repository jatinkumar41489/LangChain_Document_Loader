from langchain_community.document_loaders import TextLoader 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.7
)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt' , encoding = 'utf-8')

# To load document in the memory
docs = loader.load()

#print(docs) ---> Type of docs will be a list. 

#print(docs[0]) ---> To get the content of txt

chain = prompt | model | parser

result = chain.invoke(
    {'poem' : docs[0].page_content}
)

print(result)



