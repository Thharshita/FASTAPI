from app2.database import Base
from sqlalchemy import Column,Integer,String,Boolean,Date,DateTime
class Post(Base):   #this class name that python
    __tablename__ = 'posts' 

    id=Column(Integer, primary_key=True)
    title=Column(String, nullable=False)
    content=Column(String, nullable =False)
    published=Column(Boolean,default=True)