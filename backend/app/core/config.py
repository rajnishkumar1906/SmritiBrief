import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "The Closer - AI Deal Intelligence Agent"
    HINDSIGHT_API_KEY: str = os.getenv("HINDSIGHT_SMRITIBRIEF_API_KEY")
    _database_url: str = os.getenv("DATABASE_URL", "")
    
    @property
    def DATABASE_URL(self) -> str:
        # Automatically fix the scheme for asyncpg if it's just 'postgresql://'
        if self._database_url.startswith("postgresql://"):
            return self._database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
        return self._database_url

    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-for-jwt-change-it")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 # 1 day

settings = Settings()
