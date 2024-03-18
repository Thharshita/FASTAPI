#Creating our pydantic model here

from pydantic import BaseModel,EmailStr
# our frontend is sending the exact data that we expect
from datetime import datetime

class PostBase(BaseModel): 
    title:str
    content : str
    published:bool=True


#different class for different routes to define excat shape of the response
class PostCreate(PostBase):
    pass




#define the shape of the response, normally we return all the post that we from table to the usre, but there is time we dont want to transfer all post detail and want to do the cleanup

#Response to look like:
class Post(PostBase):  #Postbase will give title, content and published to show it to user
    #add columns that u want to show to the user
    id: int


    class Config:       #because pydantic model only know to work with dic and the data it got was not dictonary it was sqlalchemy model and hence by using this we r telling it to even work even if it not a dict
        orm_mode=True  
    
class UserCreate(BaseModel):

    email:EmailStr
    password:str

#response
class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    