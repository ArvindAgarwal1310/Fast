from fastapi import FastAPI

app=FastAPI(title="Testing")


# initating app
app = FastAPI(title="Paper Brokerage & Data",redoc_url=None)
@app.get("/")
def read_root():
    return {"message": "Invsto - Paper Brokerage & Data "}


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

if(__name__=="__app_"):
    uvicorn.run(app,host="0.0.0.0",port=8080)
