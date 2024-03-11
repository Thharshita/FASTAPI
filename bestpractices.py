from fastapi import FastAPI,Response,status,HTTPException
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
    return {"data":my_posts} #passing the array and it is automatically convt to json
#json also has a concept of array

#observe
#also,when u dont run post then u will get my_posts with 2 dict in arr , but after running app.post then the new post will be appended and u will get 3 dict in arr
    

#please
@app.post("/posts")
def create_post(post:Post):  
    print(post)  
    post_dict=post.model_dump()  
    print(post_dict)
    post_dict["id"]=randrange(0,100000)  #adding id to post_dict
    my_posts.append(post_dict)
    return {"data":my_posts}


    

#retrieveing 1 individual post
@app.get("/posts/{id}")  #id== path parameter   #id u insert is str
def get_post(id:int):  #fast api will automatically extract this id ,mind u that u have to mention that ur id can be converetd t int by id:int
    post=find_post(id)  
    return {"post_detail":post}  



#15 --- Python tutorial ,go to timeline 6:29

#how can we validate the data that user send is validate?--->Pydantic


@app.delete('/posts/{id}')
def delete_post(id: int):
    index=get_index(id)
    my_posts.pop(index)



@app.put('/posts/{id}')
def update_post(id:int,post:Post):
    index=get_index(id)
    updated_post=post.model_dump()
    updated_post["id"]=id
    my_posts[index]=updated_post
    return {"data":"updated_post"}



#ORDERS MATTERS
#get latest post, here u will get error since path api is going to follow all the path and it will 
#find the first match -i.e post/id. fast api doesnt know that that request specifically ment for this path, so u can move this above post/id path.
@app.get('post/latest')
def get_latest_post():
    n=len(my_posts)
    return my_posts[n-1]