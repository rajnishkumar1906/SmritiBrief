from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    profile: Mapped[dict] = mapped_column(JSON, default={
        "full_name": "",
        "role": "Sales Executive",
        "agent_style": "The Closer",
        "negotiation_goals": "Closing high-value B2B deals with a focus on ROI"
    })
