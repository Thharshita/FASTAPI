from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app=FastAPI()

#our frontend is sending the exact data that we expect
class Post(BaseModel):
    title:str
    content : str
    published:bool=True
    rating:Optional[int]=None

my_posts=[{"title":"tiltle of post 1","content":"content 1","id":1},
        {"title":"tiltle of post 2","content":"content 2","id":2}]  #lets just hardcode our code, arroay of dict


def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def get_index(id):
    for i,p in enumerate(my_posts):
        if p["id"]==id:
            return i


@app.get("/posts")
def get_posts():
    return {"data":my_posts} #passing the array and it is automatically covert to json


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post:Post):  
    print(post)  
    post_dict=post.model_dump()  
    print(post_dict)
    post_dict["id"]=randrange(0,100000)
    my_posts.append(post_dict)
    return {"data":my_posts}

    


#Try to request post that doesnt exist
@app.get("/posts/{id}")  
def get_post(id:int, response: Response): 
    post=find_post(id)  
    if not post:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return{f"post with id {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    return {"post_detail":post} 
 

#it gives u null which is doesnt give u much idea about what the probleme, hence there is a specific http status code that says the exact problem.

@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index=get_index(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"id:{id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put('/posts/{id}')
def update_post(id:int,post:Post):
    index=get_index(id)
    if  index== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} does not exist")
    updated_post=post.model_dump()
    updated_post["id"]=id
    my_posts[index]=updated_post
    return {"data":"updated_post"}


