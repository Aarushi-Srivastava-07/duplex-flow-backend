import uuid
from livekit import api
from app.core.config import settings

def generate_room_token(participant_identity: str = "live-hackathon-user", participant_name: str = "Hackathon Judge") -> dict:
    room_name = f"live-voice-{uuid.uuid4().hex[:6]}"
    token = (
        api.AccessToken(settings.LIVEKIT_API_KEY, settings.LIVEKIT_API_SECRET)
        .with_identity(participant_identity)
        .with_name(participant_name)
        .with_grants(api.VideoGrants(room_join=True, room=room_name))
        .to_jwt()
    )
    return {"url": settings.LIVEKIT_URL, "token": token, "room": room_name}
