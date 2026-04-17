from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class RetainRequest(BaseModel):
    bank_id: str
    content: str

class RecallRequest(BaseModel):
    bank_id: str
    query: str
    top_k: Optional[int] = 3

class ReflectRequest(BaseModel):
    bank_id: str
    query: str

class UserProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    role: Optional[str] = None
    agent_style: Optional[str] = "The Closer"
    negotiation_goals: Optional[str] = None
