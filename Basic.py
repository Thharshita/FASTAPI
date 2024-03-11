from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

# to ensure that our frontend is sending the exact data that we expect
# class Post(BaseModel):
#     title:str
#     content : str
#     published:bool=True
#     rating:Optional[int]=None

@app.get("/")   #act like an api--turns the code in path operation
async def root():       #its like a simple function, async is only needed if u r performing async task--eg like talking to db 
    return {"message":"Hello World"}  #we r sending dictionary, which fast api will covert to json which is the main universal language of api


@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}




#Please give title and content in postman Api body
#noramlly we send https get request and our api give us all the data that we trying to fetch.
#but wth the post request we can send data to the api server and will get the respond. so post request is used to creating things
@app.post("/createposts")
def create_post(payload:dict= Body(...)):  #Body(..) says that body must have values
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