from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class DataRequest(BaseModel):
    data: List[str]

class DataResponse(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_lowercase_alphabet: List[str] 

@app.get('/bfhl')
def get_bfhl():
    data = {"operation_code":1}
    return  JSONResponse(content=data, status_code=200)


@app.post('/bfhl', response_model=DataResponse)
def post_bfhl(request: DataRequest):
    numbers = []
    alphabets = []
    highest_lowercase = None

    for item in request.data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower() and (highest_lowercase is None or item >highest_lowercase):
                highest_lowercase = item
    
    return DataResponse(
        is_success=True,
        user_id="Devrishi Sikka",
        email="devrishisikka@gmail.com",
        roll_number="21BCE1036",
        numbers=numbers,
        alphabets=alphabets,
        highest_lowercase_alphabet=[highest_lowercase] if highest_lowercase else []
    )