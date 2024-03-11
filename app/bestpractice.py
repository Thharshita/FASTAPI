#Go to admin pgi , then create table of the name post --- and column ....


from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2 
from psycopg2.extras import RealDictCursor
import time

app=FastAPI()

#our frontend is sending the exact data that we expect
class Post(BaseModel):
    title:str
    content : str
    published:bool=True
while True:                                                                                                  #cursor_factory: gonna make a dic mappin rows with the content
    try:
        conn=psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="****",cursor_factory=RealDictCursor) #this lib is little bit weird when u make a query to retreive bunch of rows from database , it just gives values without column
        cursor=conn.cursor()
        print("Database Connection is successfull")
        break

    except Exception as error:
        print("Connecting to Database failed")
        print("Error",error)
        time.sleep(2)

#READ

@app.get("/posts")
def get_posts():
    cursor.execute("Select * from posts")
    post= cursor.fetchall()
    print(post)
    return {"data":post} 

#Create
@app.post("/posts")
def create_post(post:Post):  
    #cursor.execute(f"Insert into post (title,content,published) Values ({post.title},{post.content},{post.published}")  #is vulnerable to SQL Injection, hence not use this.
    cursor.execute("""Insert into posts (title,content,published) Values (%s,%s,%s) Returning *""",(post.title,post.content,post.published))
    new_post=cursor.fetchone()
    conn.commit()
    return {"data":new_post}


    
#READ
@app.get("/posts/{id}")  
def get_post(id:int):  
    cursor.execute("""Select * from posts where id=%s""", (str(id),))
    fetch=cursor.fetchone() 
    if not fetch:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not found")
    return {"post_detail":fetch}  




#DELETE
@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""Delete from posts where id=%s returning *""",(str(id)))
    delete_it= cursor.fetchone()
    conn.commit()
    if delete_it==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#Update
@app.put('/posts/{id}')
def update_post(id:int,post:Post):
    cursor.execute("""Update posts set title=%s,content=%s,published=%s where id=%sreturning*""",(post.title,post.content,post.published,str(id)))
    update_it= cursor.fetchone()
    conn.commit()
    if  update_it== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} does not exist")
    return {"data":update_it}
