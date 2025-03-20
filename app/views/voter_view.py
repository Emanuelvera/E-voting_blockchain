from fastapi import APIRouter
from app.models.voter import Voter
from app.controllers.voter_controller import register_voter, get_voters

router = APIRouter()

@router.post("/register/")
async def register_voter_view(voter: Voter):
    return await register_voter(voter)

@router.get("/voters/")
async def get_voters_view():
    return await get_voters()