from dotenv import load_dotenv
from  fastapi import FastAPI
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os


# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
os.environ['GOOGLE_API_KEY']=os.getenv("GOOGLE_API_KEY")
model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
app=FastAPI(
    title="Langchain erver",
    version="1.0",
    description="A simple Api server"
)


prompt1=ChatPromptTemplate.from_template("provide me an eaasay abut {topic}")
prompt2=ChatPromptTemplate.from_template("provide me an joke abut {topic}")
add_routes(
    app,
    model,
    path="/genai"
    
)
add_routes(
    app,
   prompt1|model,
    path="/essay"
    
)

add_routes(
    app,
   prompt2|model,
    path="/joke"
    
)
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
