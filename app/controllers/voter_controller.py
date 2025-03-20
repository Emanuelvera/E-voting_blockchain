from fastapi import HTTPException
from app.models.voter import Voter
from app.database import voters_collection
from bson import ObjectId

async def register_voter(voter: Voter):
    voter_dict = voter.dict(by_alias=True)
    new_voter = await voters_collection.insert_one(voter_dict)
    created_voter = await voters_collection.find_one({"_id": new_voter.inserted_id})
    created_voter["_id"] = str(created_voter["_id"])
    return created_voter

async def get_voters():
    voters = await voters_collection.find().to_list(100)
    for voter in voters:
        voter["_id"] = str(voter["_id"])
    return voters