# from .routers import status
# from routers import commands, messages, devices
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status

import models
from database import engine

# Create an instance of the fastapi framework
app = FastAPI(
    title="Backend Auth Project",
    description="This is the backend api auth implementation.",
    version="1.0",
)

# To create all of our models
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    """
    Home endpoint.

    Returns:
        dict: A welcome message.
    """
    return {"Message": "Welcome to the http api wrapper for mqtt devices"}


if __name__ == "__main__":
    # Run the FastAPI app using uvicorn
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=5000, reload=True)
