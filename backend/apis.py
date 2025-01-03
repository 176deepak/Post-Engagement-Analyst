# Fast API Server
# Define APIs Here

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.analyzer import run_flow

class ChatBody(BaseModel):
    msg: str
    
    
app = FastAPI()
# Enable CORS to make API call to another server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)


@app.post("/ask-to-analyzer")
def ask_to_analyst(data: ChatBody):
    response = run_flow(data.msg)
    print(response)
    return response["outputs"][0]["outputs"][0]["artifacts"]

if __name__ == "__main__":
    uvicorn.run("apis:app", host="0.0.0.0", port=8000, log_level="info", reload=True)