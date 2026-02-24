from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import auth, situations

app = FastAPI(title="Coach Speech API")

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(situations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Coach Speech API"}
