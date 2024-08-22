
# CRUD Operations using FastAPI


from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
my_posts = [{"title": "Hello World", "content": "This is a post", "published": True , "id":1},
             {"title": "Hello World", "content": "This is a post", "published": True, "id":2},]

class Post(BaseModel):
    title: str
    content: str
    published:bool = False
    rating:Optional[int] = None




def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post
    return None

def find_post_index(id):
    for i, post in enumerate( my_posts):
        if i == id:
            return i
    return None


@app.get("/")
def root():
    return {"Welcome to my world": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"posts": my_posts}

@app.post("/posts" , status_code = status.HTTP_201_CREATED)
# For creation status code should be 201
def create_post(post: Post ):
    
    post_dict = (post.model_dump())
    post_dict['id'] = len(my_posts) + 1
    my_posts.append(post_dict)
    return {"data": post_dict}



# Order does matter , first written function is called first becuase it starts from top of file

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return {"data": post}


# Path retrival could result in error if latest is taken as id 
@app.get("/posts/{id}")
def get_post(id : int ):
    post = find_post(id)
    if not post :
       raise HTTPException(status_code=404, detail="Post not found")
       
    return {"data": post}


# HTTPException is a class that is used to raise exceptions with status codes.


@app.delete("/posts/{id}" , status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_post_index(id)
    if index is None:
        raise HTTPException(status_code=404, detail="No such post exists")
    my_posts.pop(index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    index = find_post_index(id)
    if index is None:
        raise HTTPException(status_code=404, detail="No such post exists")
    my_posts[index] = post.model_dump()
   
   
    return {"data": my_posts[index]}


