from pydantic import BaseModel,Field
from typing import TypedDict

class Blog(BaseModel):
    title:str=Field(description="the title of the Blog post")
    content:str=Field(description="The main content of the blog post")

class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str
    