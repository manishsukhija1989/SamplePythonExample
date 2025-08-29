import uvicorn
from fastapi import FastAPI


# FastAPI app instance
app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}


# Run Uvicorn server
if __name__ == "__main__":
    uvicorn.run("SampleFile:app", host="0.0.0.0", port=8000, reload=True)