from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2 
from psycopg2.extras import RealDictCursor
from app2 import models  # Importing models.py directly
from app2.database import  engine,get_db
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)




# whe we run api , db:Session=Depends(get_db) going to give access to db,it will create a session to our database and perform operation then close it
app=FastAPI()

# we use get_db in sqlalchemy instead of below code
# our frontend is sending the exact data that we expect
class Post(BaseModel): 
    title:str
    content : str
    published:bool=True

# try:
#     conn=psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="alone",cursor_factory=RealDictCursor)
#     cursor=conn.cursor()
#     print("Database Connection is successfull")

# except Exception as error:
#     print("Connecting to Database failed")
#     print("Error",error)

#READ

@app.get("/posts")
def get_posts(db:Session=Depends(get_db) ):
    posts= db.query(models.Post).all()   #models.Post allow us access the model to make query to our posts tabel
    # print(posts) #after removing .all(), u will see the sql query here
    return {"data":posts} 

# @app.get("/posts")
# def get_posts():
#     cursor.execute("Select * from posts")
#     post= cursor.fetchall()
#     print(post)
#     return {"data":post} 




#Create
@app.post("/posts")
def create_post(post:Post,db:Session=Depends(get_db)):  
    
    new_post = models.Post(title=post.title, content=post.content, published=post.published)
    #what if we have more feild , itis not reliable to write all columns andit values hence
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {"data":new_post} 

# @app.post("/posts")
# def create_post(post:Post):  
#     #cursor.execute(f"Insert into posts (title,content,published) Values ({post.title},{post.content},{post.published}")  #is vulnerable to SQL Injection, hence not use this.
#     cursor.execute("""Insert into posts (title,content,published) Values (%s,%s,%s) Returning *""",(post.title,post.content,post.published))
#     new_post=cursor.fetchone()
#     conn.commit()
#     return {"data":new_post}


    
#READ

@app.get("/sqlalchemy_posts/{id}")  
def get_post(id:int,db:Session=Depends(get_db)):  
    post= db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not found")
    return {"post_detail":post}  

# @app.get("/posts/{id}")  
# def get_post(id:int):  
#     cursor.execute("""Select * from posts where id=%s""", (str(id),))
#     fetch=cursor.fetchone() 
#     if not fetch:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not found")
#     return {"post_detail":fetch}  




#DELETE

@app.delete('/sqlalchemy_posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)

    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{id} does not exist")
    post.delete(synchronize_session=False)
    db.commit()


# @app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""Delete from posts where id=%s returning *""",(str(id)))
#     delete_it= cursor.fetchone()
#     conn.commit()
#     if delete_it==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"{id} does not exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)



#UPDATE
@app.put('/sqlalchemy_posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(updated_post:Post,id: int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)
    post_first=post.first()
    if post_first==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{id} does not exist")
    post.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()

# @app.put('/posts/{id}')
# def update_post(id:int,post:Post):
#     cursor.execute("""Update posts set title=%s,content=%s,published=%s where id=%sreturning*""",(post.title,post.content,post.published,str(id)))
#     update_it= cursor.fetchone()
#     conn.commit()
#     if  update_it== None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"{id} does not exist")
#     return {"data":update_it}
