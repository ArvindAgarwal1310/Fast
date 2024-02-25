from fastapi import FastAPI

app=FastAPI(title="Testing")

app.get("/")
def ans():
    return "Hello"

