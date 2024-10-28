# Import the Union class from the typing module
from typing import Union

# Import the FastAPI class from the fastapi module
from fastapi import FastAPI

# Create an instance of the FastAPI class and assign it to the variable app
app = FastAPI()

# Define a path operation decorator for the path / that returns a dictionary
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a path operation decorator for the path /items/{item_id} that returns a dictionary
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
