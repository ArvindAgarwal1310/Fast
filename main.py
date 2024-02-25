import json
from fastapi import FastAPI,Request
from views import verify,handle_message
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app=FastAPI(title="Data Dine",redoc_url=None)

@app.get("/")
def read_root():
    return {"message": "DataDive -Data "}

@app.get("/webhook")
def webhook_get(request: Request):
    print("request",request)
    raw_body = request.body()
    raw_body = json.loads(raw_body)
    print(raw_body)
    return verify(raw_body)

@app.post("/webhook")
def webhook_post(request: Request):
    raw_body = request.body()
    raw_body=json.loads(raw_body)
    print(raw_body)
    return handle_message(body=raw_body)

# creating origin list
origins = ['*']

# config CORSM
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

