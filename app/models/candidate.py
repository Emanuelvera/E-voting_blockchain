from bson import ObjectId
from pydantic import BaseModel, Field



class Candidate(BaseModel) :
    id: str = Field (default_factory=lambda: str(ObjectId()), alias="_id")
    name:str
    position: str