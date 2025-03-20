from fastapi import FastAPI
from app.views.voter_view import router as VoterRouter

app = FastAPI()

app.include_router(VoterRouter, prefix="/voters", tags=["voters"])

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido al sistema de votación!"}