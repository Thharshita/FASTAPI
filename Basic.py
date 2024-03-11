# FastAPI is a tool that helps developers create web applications with Python really quickly.
#  It's especially good at handling lots of requests at the same time, so it's fast. 
#  It's also easy to use because it gives you helpful tools to make sure your code works properly and documents it automatically.
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

# #our frontend is sending the exact data that we expect
# class Post(BaseModel):
#     title:str
#     content : str
#     published:bool=True
#     rating:Optional[int]=None

@app.get("/")   #act like an api--turns the code in path operation
async def root():       #its function, async is only needed if u r performing async task--things like talking to db 
    return {"message":"Hello World"}  #we r sending dic, which fast api will covert to json which is the main universal langusge of api


@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

#noramlly we send https get request and our api give us all the data that we tryna get
#but wth the post request we can send data to the api server. so posst request is used to creating things
@app.post("/createposts")
def create_post(payload:dict= Body(...)):  #Body(..) days that body must have values
    print(payload)
    # return {"message":"successfully created post"}
    return {"new_post":f"title {payload['title']} content: {payload['content']}"} 

# @app.post("/createposts")
# def create_post(post:Post):  
#     print(post)
#     print(post.model_dump)
#     # return {"message":"successfully created post"}
#     return {"new_post":f"title {post.title} content: {post.content}"}  







# post: Post------> indicates the expected type of the parameter post.
# payload = Body(...) ------------>assigns the extracted value from the request body to the parameter payload.