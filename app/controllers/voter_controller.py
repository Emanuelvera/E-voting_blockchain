from fastapi import HTTPException
from models.voter import Voter
from database import voters_collection
from bson import ObjectId

async def register_voter(voter: Voter):
    voter = voter.dict(by_alias=True)
    new_voter = await voters_collection.insert_one(voter)
    created_voter = await voters_collection.find_one({"_id": new_voter.inserted_id})
    return created_voter

async def get_voters():
    voters = await voters_collection.find().to_list(100)
    return voters