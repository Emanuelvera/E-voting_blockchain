
from app.models.candidate import Candidate
from app.database import candidates_collection


async def register_candidate(candidate: Candidate):
    candidate_dict = candidate.dict(by_alias=True)
    new_candidate = await candidates_collection.insert_one(candidate_dict)
    created_candidate = await candidates_collection.find_one({"_id":new_candidate.inserted_id})
    created_candidate["_id"] = str(created_candidate["_id"])
    return created_candidate

async def get_candidates():
    candidates = await candidates_collection.find().to_list(100)
    for candidate in candidates:
        candidate["_id"] = str (candidate["_id"])
        return candidates
    