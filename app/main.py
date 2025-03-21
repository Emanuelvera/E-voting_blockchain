from fastapi import FastAPI
from app.views.voter_view import router as VoterRouter
from app.views.candidate_view import router as CandidateRouter


app = FastAPI()

app.include_router(VoterRouter, prefix="/voters", tags=["voters"])
app.include_router(CandidateRouter, prefix="/candidate", tags=["candidate"])

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido al sistema de votación!"}