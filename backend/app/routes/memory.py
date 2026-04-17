from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_current_user
from app.schemas.schemas import RetainRequest, RecallRequest, ReflectRequest
from app.services.hindsight import hindsight_service
from app.models.user import User

router = APIRouter()

@router.post("/retain")
async def retain_memory(request: RetainRequest, current_user: User = Depends(get_current_user)):
    try:
        user_bank_id = f"{request.bank_id}-{current_user.username}"
        result = hindsight_service.retain(bank_id=user_bank_id, content=request.content)
        return {"status": "success", "message": "Memory retained", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/recall")
async def recall_memory(request: RecallRequest, current_user: User = Depends(get_current_user)):
    try:
        user_bank_id = f"{request.bank_id}-{current_user.username}"
        result = hindsight_service.recall(bank_id=user_bank_id, query=request.query, top_k=request.top_k)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/reflect")
async def reflect_memory(request: ReflectRequest, current_user: User = Depends(get_current_user)):
    try:
        user_bank_id = f"{request.bank_id}-{current_user.username}"
        profile = current_user.profile
        
        # Personalize the query with the user's role and agent style
        agent_style = profile.get("agent_style", "The Closer")
        role = profile.get("role", "Sales Executive")
        
        # Build a personalized query context
        personalized_query = f"Act as {agent_style} for a {role}. Based on your memory, analyze this: {request.query}"
        
        result = hindsight_service.reflect(bank_id=user_bank_id, query=personalized_query)
        return {
            "status": "success", 
            "agent_personality": agent_style,
            "report": result.text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
