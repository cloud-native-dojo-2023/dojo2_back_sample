from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 返却されるDataModel
# {"sortNum":"", "Title":"", "Description":"", "URL", ""}