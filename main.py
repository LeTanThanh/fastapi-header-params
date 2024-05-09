from fastapi import FastAPI
from fastapi import Header

from typing import Annotated

app = FastAPI()

# Declare Header parameters
@app.get("/headers/user_agent")
async def read_user_agent(user_agent: Annotated[str | None, Header()] = None):
  return {"User-Agent": user_agent}

# Automatic conversion
@app.get("/headers/under_score")
async def read_under_score(under_score: Annotated[str | None, Header(convert_underscores = False)] = None):
  return {"under_score": under_score}

# Duplicate headers
@app.get("/header/x_tokens")
async def read_x_tokens(x_tokens: Annotated[list[str] | None, Header()] = None):
  return {"x_tokens": x_tokens}
