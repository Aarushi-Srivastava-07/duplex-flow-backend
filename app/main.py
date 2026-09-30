import subprocess
import os
from dotenv import load_dotenv
load_dotenv()
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.config import settings

agent_process = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global agent_process
    print(" Starting LiveKit Agent Worker...")
    agent_script = os.path.join(os.path.dirname(__file__), "ai", "lk_agent_tool.py")
    if os.path.exists(agent_script):
        agent_process = subprocess.Popen([sys.executable, agent_script, "dev"], env=os.environ.copy())
    yield
    if agent_process:
        print(" Shutting down LiveKit Agent Worker...")
        agent_process.terminate()

# 1. Initialize app FIRST so 'app' exists
app = FastAPI(title="DuplexFlow Backend", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# 2. Define routes AFTER 'app' is created
@app.get("/api/live-logs")
async def get_live_logs(room: str = None):
    return {
        "calls": [
            {"function": "search_flights", "args": {"destination": "Dubai", "date": "April 10"}},
            {"function": "book_flight", "args": {"passenger_name": "Aarushi"}},
            {"function": "update_identity_doc", "args": {"doc_type": "passport", "doc_number": "E772211"}}
        ],
        "transcripts": [
            "Searching flights to Dubai on April 10...",
            "Booking flight for Aarushi...",
            "Updating passport document successfully."
        ]
    }

@app.get("/")
def root():
    return {"message": "DuplexFlow Backend API is running."}