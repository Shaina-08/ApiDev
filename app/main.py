

from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"Welcome to my world": "Hello World"}


@app.post("/posts")
def get_posts(payload: dict = Body(...)):
    print(payload)
    return {"posts": "This is a post"}



# Order does matter , first written function is called first becuase it starts from top of file



