from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.schemas import UserProfileUpdate
from app.models.user import User

router = APIRouter()

@router.get("/profile")
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user.profile

@router.patch("/profile")
async def update_profile(
    profile_update: UserProfileUpdate, 
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    profile = current_user.profile.copy()
    update_data = profile_update.dict(exclude_unset=True)
    profile.update(update_data)
    
    current_user.profile = profile
    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)
    
    return {"message": "Profile updated successfully", "profile": current_user.profile}

@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "email": current_user.email}
