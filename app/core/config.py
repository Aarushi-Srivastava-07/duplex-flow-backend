from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    LIVEKIT_URL: str
    LIVEKIT_API_KEY: str
    LIVEKIT_API_SECRET: str
    GOOGLE_API_KEY: str
    LK_PROVIDER: str = "gemini2_5"
    FRONTEND_URL: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
