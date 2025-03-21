from fastapi import APIRouter
from app.controllers.candidate_controller import get_candidate, get_candidates, register_candidate
from app.models.candidate import Candidate


router = APIRouter()

@router.post("/register_candidate/", response_model=Candidate, summary="Register a new candidate", description="Register a new cadidate for the election.")
async def register_candidate_view(candidate:Candidate):
    return await register_candidate(candidate)

@router.get("/candidates", response_model=list[Candidate], summary="Get all candidates", description="Retrieve a list of all registered candidates.")
async def get_candidates_view():
    return await get_candidates()


