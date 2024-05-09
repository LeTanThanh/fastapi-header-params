from fastapi import FastAPI
from fastapi import Header

from typing import Annotated

app = FastAPI()

# Declare Header parameters
@app.get("/headers/user_agent")
async def read_user_agent(user_agent: Annotated[str | None, Header()] = None):
  return {"User-Agent": user_agent}
